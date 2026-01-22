from ast import pattern
import os
import datetime
import matplotlib.pyplot as plt
import numpy as np

dates = []
lengths = []
months = []

for dirpath, dirnames, filenames in os.walk('_posts/'):
    for filename in filenames:
        y, m, d, name = filename.split('-', 3)
        y = int(y)
        m = int(m)
        d = int(d)
        # print(y, m, d)
        date = datetime.datetime(y, m, d)
        dates.append(date)
        months.append(datetime.datetime(y, m, 1))
        
        # get content
        full_path = os.path.join(dirpath, filename)
        with open(full_path) as f:
            text = f.read()
            num_words = len(text.split())
            lengths.append(num_words)

###################### date gaps ######################
dates.sort()
distances = []
for i in range(1, len(dates)):
    distances.append((dates[i] - dates[i-1]).days)

# remove the first post
distances = distances[1:]
dates = dates[1:]
lengths = lengths[1:]

def moving_avg(lst: list[float], window: int) -> list[float]:
    buffer = []
    ret = []
    for x in lst:
        buffer.append(x)
        if len(buffer) > window:
            buffer = buffer[1:]
        ret.append(sum(buffer) / len(buffer))
    return ret
# print(distances)
plt.figure(figsize=(6, 4), dpi=150)
plt.axhline(7, label='"weekly basis" gap', color='gray')



# plt.plot(distances, alpha=0.5, label="raw")
# plt.plot(moving_avg(distances, 10), label="smoothened")
# plt.xlabel('post')
# xtick_gap = 15
# xticks = [i for i in range(1, len(dates), xtick_gap)]
# xlabels = [str(d)[:-9] for d in dates[1::xtick_gap]]
# plt.xticks(xticks, xlabels, rotation=45)

plt.plot(dates[1:], distances, alpha=0.5, label="raw")
plt.plot(dates[1:], moving_avg(distances, 10), label="smoothened")
plt.xticks(rotation=45)

plt.title('Post gaps over time')
plt.ylabel('gap length in days')
plt.legend()
plt.tight_layout()
plt.savefig('assets/260121_gaps.png')

###################### posts per month ######################

def linearize(dt: datetime.datetime):
    return dt.year * 12 + dt.month - 1

vals, cnts = np.unique(months, return_counts=True)
month_cnt = {val: cnt for val, cnt in zip(vals, cnts)}
start_month = min(vals)
end_month = max(vals)
xs, ys = [], []
for x in range(linearize(start_month), linearize(end_month) + 1):
    y = x // 12
    m = x % 12 + 1
    dt = datetime.datetime(y, m, 1)
    ys.append(month_cnt.get(dt, 0))
    xs.append(dt)
plt.figure(figsize=(6, 3), dpi=150)
plt.axhline(4, label='"weekly basis"', color='gray', linestyle=':')
plt.plot(xs, ys)
plt.title('Post count per month')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('assets/260121_posts_per_month.png')




###################### correlation between gap length and content length ######################
plt.figure(figsize=(6, 4), dpi=150)
x = distances
y = lengths[1:]
corr = np.corrcoef(x, y)
# print(corr)
plt.scatter(x, y, alpha=0.5)
plt.title(f'Date Gap vs. Post Length (pearson={corr[0, 1]:.4f})')
plt.xlabel('date gap (days)')
plt.ylabel('post length (characters)')
plt.tight_layout()
plt.savefig('assets/260121_corr_gap_content.png')