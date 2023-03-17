Team Name: `chAQalS`

Student Name of member 1: `Emad Zinoghli`
Student No. of member 1: `98103267`

Student Name of member 2: `Maziyar Shamsipoor`
Student No. of member 2: `98101844`

- [ ] Read Session Contents.

### Section 3.3.1
- [ ] Investigate the /proc/ directory
    1. [ ] ![3.3.1](https://github.com/alxelr2014/Notes/blob/oslab/3.3.1.png)

### Section 3.3.2

- [ ] Do 5 subtasks from 1 to 5:
    1. [ ] ![3.3.2-1](https://github.com/alxelr2014/Notes/blob/oslab/3.3.2-1.png)
    1. [ ] ![3.3.2-2.1](https://github.com/alxelr2014/Notes/blob/oslab/3.3.2-2.1.png)
    ![3.3.2-2.2](https://github.com/alxelr2014/Notes/blob/oslab/3.3.2-2.2.png)
    1. [ ] ![3.3.2-3](https://github.com/alxelr2014/Notes/blob/oslab/3.3.2-3.png)
    1. [ ] ![3.3.2-4](https://github.com/alxelr2014/Notes/blob/oslab/3.3.2-4.png)
    1. [ ] ![3.3.2-5](https://github.com/alxelr2014/Notes/blob/oslab/3.3.2-5.png)

## Section 3.3.3

- [ ] Write (in English or Persian) about each file in /proc/(PID) directory:
    1. `cmdline` contains the arguments passed to the process.
    1. `eviron` contains the environment variables.
    1. `stat` contains information about the process such as it is `pid`, `file name`, etc.
    
        ![3.3.3-1-3](https://github.com/alxelr2014/Notes/blob/oslab/3.3.3-1-3.png)
    
    1. `status` contains information about the process similar to `stat`, however, it is more human readable.
        
        ![3.3.3-4](https://github.com/alxelr2014/Notes/blob/oslab/3.3.3-1-4.png)
    1. `statm` contains information about the process' memory.

        ![3.3.3-5](https://github.com/alxelr2014/Notes/blob/oslab/3.3.3-5.png)
    1. `cwd` is a symbolic link to the working directory of the process.

        ![3.3.3-6](https://github.com/alxelr2014/Notes/blob/oslab/3.3.3-6.png)
    1. `exe` is a symbolic link that contains the pathname of the executed command. 
    1. `root` is a symbolic link to the process' root directory.

        ![3.3.3-8](https://github.com/alxelr2014/Notes/blob/oslab/3.3.3-8.png)

- [ ] Place your script for shwoing PID of running porcesses and their name here:
    - [ ] ![3.3.3-9.1](https://github.com/alxelr2014/Notes/blob/oslab/3.3.3-9.1.png)

    -    ![3.3.3-9.2](https://github.com/alxelr2014/Notes/blob/oslab/3.3.3-9.2.png)

- [ ] Place your source code for a program that shows details of a program by receiving PID:
    - [ ] ![3.3.3-10.1](https://github.com/alxelr2014/Notes/blob/oslab/3.3.3-10.1.png)

    -    ![3.3.3-10.2](https://github.com/alxelr2014/Notes/blob/oslab/3.3.3-10.2.png)

### Section 3.3.4

- [ ] Write (in English or Persian) about each file in /proc/ directory:
    1. `meminfo` contains information about the memory usages of the whole system.

        ![3.3.4-1](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-1.png)
    1. `version` contains information about the linux kernel version.

        ![3.3.4-2](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-2.png)
    1. `uptime` contains the uptime of the system and the amount of time spent in the idle process both in seconds.

        ![3.3.4-3](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-3.png)

    1. `stat` contains information about the kernel and the system.

        ![3.3.4-4](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-4.png)
    1. `mounts` contains the list of filesystems mounted on the system.

        ![3.3.4-5](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-5.png)
    1. `net` is directory containing files that have information about the networking layer.

        ![3.3.4-6](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-6.png)

    1. `loadavg` contains five fiels. The first three fields are the number of jobs in the run queue averaged over 1, 5, and 15 minutes. The fourth field itself contains two number. The first number denotes the nummber runnable kernel scheduling entities (processes, threads). The second number denotes the number of kernel scheduling entities the exist on the system. The last field is the `pid` of the last process created on the system.

        ![3.3.4-7](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-7.png)
    1. `interrupts` contains information about interrupts of CPUs and IO devices.

        ![3.3.4-8](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-8.png)
    1. `ioports` contains the list of input and output ports.

        ![3.3.4-9](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-9.png)
    1. `filesystem` contains the list of supported filesystems.

        ![3.3.4-10](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-10.png)
    1. `cpuinfo` contains information about the processors of the system.

        ![3.3.4-11](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-11.png)
    1. `cmdline` contains the arguments passed to kernel at boot time.

        ![3.3.4-12](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-12.png)

- [ ] Place your source code for a program that shows details of processor:
    - [ ] ![3.3.4-13.1](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-13.1.png)

    -    ![3.3.4-13.2](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-13.2.png)

- [ ] Place your source code for a program that shows details of memory management sub-system:
    - [ ] ![3.3.4-14.1](https://github.com/alxelr2014/Notes/blob/oslab/3.3.4-14.1.png)

    -    ![3.3.4-14.2](https://github.com/alxelr2014/Notes/blob/oslab/3.3.3-14.2.png)

- [ ] Write your description about five important files at /proc/sys/kernel:
    - [ ] `/threads_max` determines the maximum number of threads that can be on the system.
    - [ ] `/pid_max` determnies the maximum number that a processor can have as its `pid`.
    - [ ] `/reboot-cmd` gives the argument to the bootloader after rebooting.
    - [ ] `/modprobe` contains the path for the module loader.
    - [ ] `/ctrl-alt-del` determines how the kernel handles the key combniation Ctrl-Alt-Del.

- [ ] Write your description about /proc/self file
    - [ ] For any process accessing `/proc/self` file is like accessing the `/proc/pid`. Therefore, by accessing this link, the process ends up at its `/proc/pid` directory.


## Source Code Submission

please submit all your codes in a zip file

 - [ ] [codes](https://github.com/alxelr2014/Notes/blob/oslab/codes.zip)
