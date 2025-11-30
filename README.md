This website is created by [Jekyll](https://jekyllrb.com/), inspired by [Andrej Karpathy's blog](https://karpathy.github.io/).

## Install

Follow https://jekyllrb.com/docs/installation/.

For Ubuntu VM on GCP:
```bash
sudo apt-get install ruby-full build-essential zlib1g-dev

echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

gem install jekyll bundler
```

## Run
```bash
bundle exec jekyll serve --host 0.0.0.0 --livereload
```

## Backlog
- [x] Comment section
- [x] Filtering by tags
- [x] Estimated reading time (or word count)
