---
layout: post
title: Operating Systems -- Midterm Review
---
(This post is generated for me to review knowledge in CS5348 before the midterm)

Operating systems (OS's) are the silent workhorses of today's economy. They do so many complicated things silently, to the point where we take it for granted. Below is a tour of something that an OS does.

# What is an OS?
A computer is a complex engine with many functionalities. An OS is a *resource manager*, coordinating those functionalities and making them work seamlessly for an end user. In other words, it is an internface between hardware and applications, making programs[^program] run easily and 'fast'. In particular, it allows the sharing of CPU and memory among many apps (multiplexing), allows apps to interact, and isolate errors between apps.

Another view: An OS is a special program. 
- It gets run first on the hardware, and dictates how other normal programs use it. It has access to all the resources, but never abuse that power. Instead, it tries the best to give the resources to the other programs as efficiently as possible.
- As a program, it is also written in a programming language! The computer can runs code, therefore can run the OS program. The common language for OS is C. Such type of programming is complicated, and is called 'kernel programming'. (Read about kernel below). 

[^program]: Programs and applications are interchangeable in this post.

Popular OS's:
- Desktop: Linux, Windows, **MacOS**[^os]
- Smartphone: Android, **iOS**
- Embedded: RasberryPi OS?

[^os]: Bold = my current OS

# Processes: A unifying view of applications
Computer applications are endlessly diverse in shape and form. What is the commonalities between Google Chrome, Candy Crush Saga, and Settings? To the OS, the only thing that matter is *processes*. A process to the OS is like a train of thought to the human brain. It is a (unit) virtual entity that is doing an independent thing, manifesting into operations in the CPU and data on memory and devices. 

The data of a process is its manifestation in space (constrast to its CPU operations, which are in time). It includes:
- Its own code, directly or indirectly written by humans. That is the script that dictates how the process runs, like DNA in humans. So far, this cannot be changed by the process during run time. (It this a limitation of computers?)
- Static data: things that never disappear during the process' lifetime, like global variables.
- Heap (not the data structure heap): store user-controlled dynamic data, like arrays(?).
- Stack (not the data structure stack). Each element in the stack is usually storing the context of a function call, including local variables.

As mentioned earlier, OS is usually written in C. Therefore, there are C functions that perform process operations:
- `fork`: create a new process (duplicate everything, including IP), returns the pid of the child depending on which process that is. After that, two processes run on themselves.
    - How does `fork` look like in assembly language? Is it always a *system call* regardless of OS?
- `wait`: wait for the first child to terminate
- `getppid`: returns parent's id
- => Notice that these functions will eventually be run in *a process*!

The nice thing about process is that the OS now doesn't need to care about billions types of applications. It only deals with processes now. (How neat!) Next sections will show how the OS share the CPU and Memory among processes.

# CPU Virtualization
This problem is similar to sharing a toy between 100 kids, where each kid has a different *unknown* amount of time it wants to play with it. Naturally, we want to have (1) a *schedule* of CPU time for each process and (2) a mechanism to take the CPU away from a process and give it to another (context-switch).

## Scheduler
Instead of having a fixed schedule into the future, the OS takes back CPU control back every [few milliseconds](https://www.cs.unc.edu/~porter/courses/comp530/f16/slides/scheduling-intro.pdf) (i.e., *time slice*) or when the process goes to BLOCKED state, then decides which process to give the CPU to next (i.e., a *policy*).

- Nature of processes: different unknown running time, different arrival time, and may wait for I/O while being given the CPU.
- Optimization metrics (usually aggregated over all processes to evaluate the policy):
    - Turn Around Time = t_completion - t_arrival
    - Response Time = t_{given CPU} - t_arrival
- Some popular policies:
    - Naive: FIFO (non-interrupted running time)
    - For batch jobs (approximate the running time): Shortest Time to Completion First
    - For interactive jobs: Round Robin
    - For both: Multi-level Priority Scheduling
        1. Run everything in higher priority first
        2. Round robin for jobs within one level
        3. Place newly entering jobs at the top priority
        4. Downgrade jobs that use an entire time slice
        5. Every S slices, pump all processes to the highest level
        6. Keep track of CPU use time for each process to downgrade if needed
    - For privileging system: Loterry scheduler
    - => Time slice length is crucial and must be tuned.

## Context-switching with Dispatcher
- Context of a process is saved together in Process Control Block (PCB), which mainly(?) stays in RAM.
    - It contains the state of the process, which is mainly READY, RUNNING, or BLOCKED (waiting for something).
    - Context-switching essentially means saving the PCB of the previous process, 'loading' the PCB of the new one (including bringing the pointers to their places).
- CPU is only given to READY processes (which sounds obvious).
- Time slice is an important trigger of context-switch, and is supported by hardware interrupt.

## Privilege levels
Whenever a process, which is in *user* level,  wants to execute a restricted action (like accessing data), it makes a system call via software interupt (trap number `$64` in Linux). Then the control is back to the *kernel* level. Information of the action is stored in some register.

# Memory Virtualization
- We want virtual memory, which creates an illusion of the whole address space for each process. We want it to be easy to use, and fast.
- Naive solution -- Base and Bounds: Offset the *virtual address* (base) and limit its value (bounds) to get *physical address*. Problems are internal fragmentation (process does not use its allocated memory) and external fragmentation (unused spaces cannot be allocated because they are not contiguous).
- Spectrum of solutions:
    - Allocate a whole chunk, sufficient memory block for each process -> A huge process can take down the system.
    - Book-keeping each byte for each process. Hyper busy. Consume time and half a memory to do book-keeping.
- Best solution is paging, or ultimately, multi-level paging:
    - Each virtual address (of 64 bits in 64-bit processor) is separated into multiple sections. Each section is a key to a look-up table. The last look-up table is called page table, with page number as key, and frame number (physical address, up to 64-bit) as value.
    - All the lookup tables form a tree, all of which are saved in RAM.
    - Caching the memory reference with TLB (Translation Lookaside Buffer). It saves the most frequently/recently accessed virtual addresses and their corresponding physical address. Search in parallel using hardware.
        - Foundation: Locality of reference
        - Outcome: hit or miss
        - Metric: hit rate
        - Handling TLB miss: depending on the policy (random removal, FIFO, etc.)
- Given limited RAM to store all physical frames, we have Demand Paging -- only keeping the frequently used frames in RAM and putting others in external device.
    - 'Present' bit in page table entry to indicate whether the frame is in memory (1) or device (0).
    - If present bit is 0, that is a 'page fault'. OS chooses a frame to remove from memory and load the needed frame in.

# Appendix: C Programming Language
- `strtok_r`
- use of pointers
- `malloc` and `free`
- `extern` for global variable

# Appendix: Computer Architecture
- Components: CPU, Memory (RAM), I/O devices (disk, screen, keyboard)
- Hardware customization is very helpful in OS speed-up (interrupt, base and bounds, parallel search)