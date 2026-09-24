/**
 * Official CSE111: Fundamentals of Computing Midterm Mock Examination Suite
 * Contains Full-Length 30-Question Tests
 * Modelled on actual University Midterm Examination Papers & Exam Companion
 * Focuses strictly on Units 1-3:
 *   Unit 1: Computer Systems, Architecture, Caches, Storage & Buses
 *   Unit 2: Operating Systems, Process Lifecycle, CPU Scheduling & Memory Management
 *   Unit 3: Linux OS, FHS, Shell Commands, Permissions & Virtualization
 * Authentic +1 / -0.25 marking scheme and detailed step-by-step solutions.
 */

export const CSE111_MOCK_TESTS = [
  {
    id: 'cse111-midterm-paper-1',
    code: 'CSE111-SET-A',
    title: 'Midterm Examination • Paper 1 (Official University Blueprint)',
    courseCode: 'CSE111',
    courseName: 'Fundamentals of Computing',
    examType: 'Midterm Examination',
    durationMinutes: 90,
    totalQuestions: 30,
    marksPerQuestion: 1,
    negativeMarks: 0.25,
    maxMarks: 30,
    difficulty: 'Standard Exam',
    topics: ['Computer Architecture', 'Operating Systems', 'Linux CLI', 'Memory Management'],
    description: 'Comprehensive university midterm paper testing von Neumann architecture, cache hierarchy, OS scheduling algorithms, virtual memory paging, Linux FHS, and file permissions.',
    questions: [
      {
        id: 1,
        question: 'In the von Neumann computer model, the throughput bottleneck resulting from sharing a single physical bus for both instruction fetching and data transfers is called the:',
        options: ['von Neumann Bottleneck', 'Harvard Latency', 'Bus Skew', 'Cache Miss Penalty'],
        correctIndex: 0,
        topic: 'Computer Architecture',
        explanation: {
          steps: [
            'In the von Neumann architecture, both instructions and program data share the same physical bus and address space.',
            'Because the CPU cannot read an instruction and read/write data simultaneously, bus throughput limits the execution speed (von Neumann bottleneck).'
          ],
          keyConcept: 'von Neumann bottleneck occurs due to shared instruction and data buses.'
        }
      },
      {
        id: 2,
        question: 'Which level of the CPU cache hierarchy is typically the largest in storage capacity, shared among all cores on a multi-core silicon die, and incurs higher latency than L1 or L2 caches?',
        options: ['Level 3 (L3) Cache', 'Level 1 Instruction Cache (L1i)', 'Level 1 Data Cache (L1d)', 'Level 2 (L2) Cache'],
        correctIndex: 0,
        topic: 'Computer Architecture',
        explanation: {
          steps: [
            'L1 cache is split (instruction/data) and private to each core with fastest access (1-4 cycles).',
            'L2 cache is slightly larger and private per core (10-14 cycles).',
            'L3 cache (Last Level Cache) is shared across all CPU cores, holds several megabytes (16-64MB+), and incurs higher latency (30-50 cycles).'
          ],
          keyConcept: 'L3 cache is shared across cores and largest in the on-die hierarchy.'
        }
      },
      {
        id: 3,
        question: 'Static RAM (SRAM) is preferred over Dynamic RAM (DRAM) for building CPU caches because SRAM:',
        options: [
          'Does not require periodic capacitive refresh cycles and offers significantly lower access latency',
          'Has a much higher storage density per unit silicon area',
          'Consumes zero power at all times',
          'Is non-volatile when main power is removed'
        ],
        correctIndex: 0,
        topic: 'Computer Architecture',
        explanation: {
          steps: [
            'SRAM uses 6-transistor (6T) flip-flop bistable circuits, holding state continuously as long as power is applied without refreshing.',
            'DRAM stores charges in tiny capacitors that leak and require periodic refresh cycles every few milliseconds, making DRAM slower.'
          ],
          keyConcept: 'SRAM offers ultra-low latency without requiring refresh cycles.'
        }
      },
      {
        id: 4,
        question: 'The high-performance storage host controller protocol specifically architected to leverage the low latency and massive parallelism of solid-state storage across direct PCIe lanes is:',
        options: ['NVMe (Non-Volatile Memory Express)', 'SATA 3.0', 'SCSI-3', 'PATA IDE'],
        correctIndex: 0,
        topic: 'Computer Architecture',
        explanation: {
          steps: [
            'Legacy SATA was designed for rotating magnetic platters with a single command queue of 32 depth.',
            'NVMe connects directly to PCIe lanes and supports up to 64,000 parallel queues with 64,000 commands each, optimizing flash SSD concurrency.'
          ],
          keyConcept: 'NVMe utilizes direct PCIe lanes for ultra-high parallel SSD performance.'
        }
      },
      {
        id: 5,
        question: 'A storage administrator configures four 1 TB hard drives in a RAID 5 array. The usable capacity available to the operating system is:',
        options: ['3 TB (calculated as (N - 1) × Drive Capacity)', '4 TB', '2 TB', '1 TB'],
        correctIndex: 0,
        topic: 'Computer Architecture',
        explanation: {
          steps: [
            'RAID 5 employs distributed block-level striping with distributed parity.',
            'The parity storage overhead across the array is equivalent to the capacity of exactly one drive.',
            'Usable capacity = (N - 1) × Size = (4 - 1) × 1 TB = 3 TB.'
          ],
          keyConcept: 'RAID 5 usable capacity = (N - 1) × drive capacity.'
        }
      },
      {
        id: 6,
        question: 'Which central computer hardware unit coordinates and directs the flow of data, control signals, and instruction cycles between the ALU, registers, and memory?',
        options: ['Control Unit (CU)', 'Arithmetic Logic Unit (ALU)', 'Floating-Point Unit (FPU)', 'DMA Controller'],
        correctIndex: 0,
        topic: 'Computer Architecture',
        explanation: {
          steps: [
            'The Control Unit (CU) orchestrates the fetch-decode-execute cycle.',
            'It generates timing and control pulses directing data movement between ALU, registers, and buses.'
          ],
          keyConcept: 'Control Unit directs the fetch-decode-execute instruction cycle.'
        }
      },
      {
        id: 7,
        question: 'The principle of "Spatial Locality" in cache memory systems states that:',
        options: [
          'When a memory location is accessed, nearby contiguous memory addresses are highly likely to be accessed soon',
          'An accessed memory address will be referenced repeatedly within a short time window',
          'All cache lines are refreshed simultaneously every millisecond',
          'Data in cache is mirrored across two identical chips'
        ],
        correctIndex: 0,
        topic: 'Computer Architecture',
        explanation: {
          steps: [
            'Temporal Locality: A memory item referenced now will be referenced again soon (loops).',
            'Spatial Locality: If memory address x is referenced, adjacent addresses (x+1, x+2) will likely be referenced soon (arrays, sequential instructions).'
          ],
          keyConcept: 'Spatial locality means adjacent contiguous addresses are likely to be accessed.'
        }
      },
      {
        id: 8,
        question: 'Under the RAID 0 storage specification, data blocks are:',
        options: [
          'Striped across multiple member disks without parity or mirroring, providing no fault tolerance',
          'Mirrored identically across two disks',
          'Protected by double distributed parity',
          'Stored sequentially on magnetic tape'
        ],
        correctIndex: 0,
        topic: 'Computer Architecture',
        explanation: {
          steps: [
            'RAID 0 divides data into stripes written across multiple disks simultaneously for maximum throughput.',
            'However, it includes zero parity or redundancy; failure of a single disk results in total data loss.'
          ],
          keyConcept: 'RAID 0 is striping without redundancy.'
        }
      },
      {
        id: 9,
        question: 'Which CPU register holds the actual physical memory address from which data is to be read or to which data is to be written?',
        options: ['Memory Address Register (MAR)', 'Instruction Register (IR)', 'Accumulator (AC)', 'Program Counter (PC)'],
        correctIndex: 0,
        topic: 'Computer Architecture',
        explanation: {
          steps: [
            'PC stores the address of the next instruction to execute.',
            'IR holds the current instruction opcode being decoded.',
            'MAR holds the address in RAM currently being accessed on the address bus.',
            'MDR (Memory Data Register) holds the actual data read from or written to memory.'
          ],
          keyConcept: 'MAR holds the memory address being read/written.'
        }
      },
      {
        id: 10,
        question: 'What is the role of the Program Counter (PC) register in a microprocessor?',
        options: [
          'Stores the memory address of the next instruction to be fetched and executed',
          'Counts total instructions executed since reboot',
          'Performs arithmetic additions',
          'Stores output flags of the ALU'
        ],
        correctIndex: 0,
        topic: 'Computer Architecture',
        explanation: {
          steps: [
            'The Program Counter automatically increments after each instruction fetch, pointing to the subsequent instruction in memory sequence.'
          ],
          keyConcept: 'Program Counter points to the next instruction address.'
        }
      },
      {
        id: 11,
        question: 'In modern operating system architectures, the transition from unprivileged user space to privileged kernel space is triggered by executing a:',
        options: ['System Call (syscall / software interrupt)', 'Preprocessor directive', 'Memory compaction command', 'Standard C variable declaration'],
        correctIndex: 0,
        topic: 'Operating Systems',
        explanation: {
          steps: [
            'User programs run in Ring 3 (user mode) without direct hardware privileges.',
            'To request privileged services (disk I/O, network send, process creation), the CPU executes a system call trap into Ring 0 (kernel mode).'
          ],
          keyConcept: 'System call triggers transition from user mode to kernel mode.'
        }
      },
      {
        id: 12,
        question: 'Which operating system kernel architecture incorporates core services (file systems, memory management, device drivers, network protocols) within a single contiguous address space running in supervisor mode?',
        options: ['Monolithic Kernel', 'Microkernel', 'Exokernel', 'Hybrid Nano-Kernel'],
        correctIndex: 0,
        topic: 'Operating Systems',
        explanation: {
          steps: [
            'Monolithic kernels (e.g. Linux) run all system services and drivers inside kernel space for speed.',
            'Microkernels (e.g. Mach, QNX) run only minimal scheduling/IPC in kernel space and move file systems and drivers to user space.'
          ],
          keyConcept: 'Monolithic kernels execute core services in single kernel space.'
        }
      },
      {
        id: 13,
        question: 'In CPU process management, the state transition that occurs when a running process issues a blocking I/O request (such as reading a file from disk) is:',
        options: ['Running → Waiting (Blocked)', 'Running → Ready', 'Ready → Running', 'Waiting → Terminated'],
        correctIndex: 0,
        topic: 'Operating Systems',
        explanation: {
          steps: [
            'When a process requests an I/O operation that cannot be satisfied immediately, the CPU scheduler transitions it from Running to Waiting/Blocked.',
            'Once I/O completes, an interrupt moves it from Waiting to Ready.'
          ],
          keyConcept: 'Blocking I/O transitions a process from Running to Waiting.'
        }
      },
      {
        id: 14,
        question: 'A CPU scheduling algorithm assigns a fixed time slice (quantum q) to each process in the ready queue in a cyclical manner. This algorithm is known as:',
        options: ['Round Robin (RR)', 'Shortest Job First (SJF)', 'First-Come, First-Served (FCFS)', 'Priority Scheduling'],
        correctIndex: 0,
        topic: 'Operating Systems',
        explanation: {
          steps: [
            'Round Robin is a preemptive scheduling algorithm where each process receives a predetermined CPU time quantum q.',
            'If uncompleted, the process is preempted and returned to the tail of the ready queue.'
          ],
          keyConcept: 'Round Robin uses fixed time quantums in circular FIFO order.'
        }
      },
      {
        id: 15,
        question: 'Virtual memory systems implement "Demand Paging", which means that:',
        options: [
          'Pages are brought from secondary storage into physical RAM only when referenced by program execution',
          'All virtual pages must be allocated in physical RAM before execution begins',
          'Pages are locked in cache and never written to secondary storage',
          'Virtual addresses directly match physical RAM addresses'
        ],
        correctIndex: 0,
        topic: 'Operating Systems',
        explanation: {
          steps: [
            'With pure demand paging, a page is loaded into physical memory only when a page fault occurs upon referencing that page during execution.'
          ],
          keyConcept: 'Demand paging loads pages into memory on demand when accessed.'
        }
      },
      {
        id: 16,
        question: 'The hardware component within the CPU that intercepts virtual addresses generated by program execution and translates them into physical memory addresses is the:',
        options: ['Memory Management Unit (MMU)', 'Arithmetic Logic Unit (ALU)', 'Direct Memory Access (DMA) engine', 'Interrupt Vector Table (IVT)'],
        correctIndex: 0,
        topic: 'Operating Systems',
        explanation: {
          steps: [
            'The MMU consults the page table (aided by the TLB cache) to translate virtual page numbers to physical frame numbers.'
          ],
          keyConcept: 'MMU translates virtual memory addresses to physical memory addresses.'
        }
      },
      {
        id: 17,
        question: 'A severe operating system state where multiple processes are indefinitely blocked because each holds a resource while waiting for a resource held by another process in a closed loop is called:',
        options: ['Deadlock', 'Thrashing', 'Starvation', 'Livelock'],
        correctIndex: 0,
        topic: 'Operating Systems',
        explanation: {
          steps: [
            'Deadlock occurs when four Coffman conditions hold simultaneously: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait.'
          ],
          keyConcept: 'Deadlock is a circular wait state among blocked processes.'
        }
      },
      {
        id: 18,
        question: 'In the program compilation lifecycle, which software tool resolves external symbol references and binds object modules and static libraries into a standalone executable binary?',
        options: ['Linker', 'Compiler', 'Assembler', 'Preprocessor'],
        correctIndex: 0,
        topic: 'Operating Systems',
        explanation: {
          steps: [
            'Preprocessor expands macros and headers (#include).',
            'Compiler converts source code to assembly code.',
            'Assembler converts assembly to relocatable object code (.o).',
            'Linker resolves function addresses and binds libraries into the final executable binary.'
          ],
          keyConcept: 'Linker combines object files and resolves symbol addresses.'
        }
      },
      {
        id: 19,
        question: 'Which segment of a running process\'s memory layout stores local automatic variables, function call parameters, and return addresses in a Last-In, First-Out sequence?',
        options: ['Stack Segment', 'Heap Segment', 'Data Segment', 'Text (Code) Segment'],
        correctIndex: 0,
        topic: 'Operating Systems',
        explanation: {
          steps: [
            'Stack: Automatic function frames, local variables, return pointers (grows downward).',
            'Heap: Dynamically allocated memory via malloc()/new (grows upward).',
            'Data: Global and static initialized/uninitialized variables.',
            'Text: Compiled read-only machine instructions.'
          ],
          keyConcept: 'Stack segment manages function frames and local variables in LIFO order.'
        }
      },
      {
        id: 20,
        question: 'The condition known as "Thrashing" in an operating system occurs when:',
        options: [
          'The system spends more time servicing page faults and swapping pages than executing user processes',
          'CPU clock speed exceeds cooling capacity',
          'Disk sectors become corrupt',
          'Processes consume all network bandwidth'
        ],
        correctIndex: 0,
        topic: 'Operating Systems',
        explanation: {
          steps: [
            'When physical RAM is overcommitted and sum of working sets exceeds available frames, page faults occur continuously, driving CPU utilization down to near zero.'
          ],
          keyConcept: 'Thrashing is excessive page swapping degrading system throughput.'
        }
      },
      {
        id: 21,
        question: 'The Linux operating system kernel was initially created and released in 1991 by:',
        options: ['Linus Torvalds', 'Richard Stallman', 'Ken Thompson', 'Dennis Ritchie'],
        correctIndex: 0,
        topic: 'Linux OS',
        explanation: {
          steps: [
            'Linus Torvalds announced and released the Linux kernel as an open-source monolithic kernel in August 1991 at the University of Helsinki.'
          ],
          keyConcept: 'Linus Torvalds created the Linux kernel.'
        }
      },
      {
        id: 22,
        question: 'According to the Linux Filesystem Hierarchy Standard (FHS), host-specific, system-wide configuration files (such as passwd, fstab, and hosts) are stored in which directory?',
        options: ['/etc', '/bin', '/dev', '/proc'],
        correctIndex: 0,
        topic: 'Linux OS',
        explanation: {
          steps: [
            '/etc contains static host-specific system configuration files.',
            '/bin contains essential user binaries.',
            '/dev contains special device node files.',
            '/proc contains virtual kernel process telemetry.'
          ],
          keyConcept: '/etc contains system configuration files.'
        }
      },
      {
        id: 23,
        question: 'Which directory in a Linux system serves as a virtual pseudo-filesystem generated dynamically by the kernel to provide runtime diagnostic and process information?',
        options: ['/proc', '/var', '/usr', '/home'],
        correctIndex: 0,
        topic: 'Linux OS',
        explanation: {
          steps: [
            '/proc does not occupy disk space; it is a virtual filesystem populated in RAM by the kernel exposing process IDs and hardware state.'
          ],
          keyConcept: '/proc is a dynamic kernel pseudo-filesystem.'
        }
      },
      {
        id: 24,
        question: 'In Linux file permissions, executing the command "chmod 755 script.sh" assigns what permissions to the Owner, Group, and Others respectively?',
        options: [
          'Owner: rwx, Group: r-x, Others: r-x',
          'Owner: rwx, Group: rw-, Others: r--',
          'Owner: rw-, Group: r--, Others: ---',
          'Owner: r-x, Group: r-x, Others: r-x'
        ],
        correctIndex: 0,
        topic: 'Linux OS',
        explanation: {
          steps: [
            'Binary octal values: r = 4, w = 2, x = 1.',
            '7 = 4 + 2 + 1 = rwx (read, write, execute).',
            '5 = 4 + 0 + 1 = r-x (read, execute).',
            'chmod 755 gives Owner = rwx, Group = r-x, Others = r-x.'
          ],
          keyConcept: '755 octal permission = rwxr-xr-x.'
        }
      },
      {
        id: 25,
        question: 'What information does an Inode (index node) in a Linux filesystem store?',
        options: [
          'File metadata (size, permissions, owner, timestamps, data block pointers), but NOT the filename',
          'Only the human-readable filename',
          'The complete text content of the file',
          'The user password hashes'
        ],
        correctIndex: 0,
        topic: 'Linux OS',
        explanation: {
          steps: [
            'Inodes store file attributes, permissions, UID/GID, size, and pointers to disk blocks.',
            'The filename itself is stored inside the directory file, which maps the name string to the Inode number.'
          ],
          keyConcept: 'Inodes store all file metadata except the filename.'
        }
      },
      {
        id: 26,
        question: 'How does a Linux "Hard Link" differ from a "Symbolic (Soft) Link"?',
        options: [
          'A hard link shares the exact same Inode number and points directly to data blocks; a symbolic link has a distinct Inode containing the path string',
          'A hard link can span across different mounted filesystems',
          'A symbolic link cannot be deleted once created',
          'A hard link creates a duplicate copy of file contents on disk'
        ],
        correctIndex: 0,
        topic: 'Linux OS',
        explanation: {
          steps: [
            'Hard link: Points to the same Inode. Cannot link directories or cross filesystem boundaries.',
            'Soft link: A separate file with its own Inode containing the pathname pointer to another target.'
          ],
          keyConcept: 'Hard links share the same Inode; soft links contain the target path.'
        }
      },
      {
        id: 27,
        question: 'Which Bash command-line utility uses regular expressions to search text files for lines matching a specified pattern?',
        options: ['grep', 'sed', 'awk', 'find'],
        correctIndex: 0,
        topic: 'Linux OS',
        explanation: {
          steps: [
            'grep (Global Regular Expression Print) searches input files for lines matching a pattern and outputs them.'
          ],
          keyConcept: 'grep searches text using regular expressions.'
        }
      },
      {
        id: 28,
        question: 'In Linux input/output redirection, the standard file descriptor integer corresponding to Standard Error (stderr) is:',
        options: ['2', '0 (stdin)', '1 (stdout)', '3'],
        correctIndex: 0,
        topic: 'Linux OS',
        explanation: {
          steps: [
            '0 = Standard Input (stdin)',
            '1 = Standard Output (stdout)',
            '2 = Standard Error (stderr)',
            'Example: "command 2> error.log" redirects stderr to a file.'
          ],
          keyConcept: 'File descriptor 0 = stdin, 1 = stdout, 2 = stderr.'
        }
      },
      {
        id: 29,
        question: 'The special permission bit that, when set on a directory (such as /tmp, octal 1777), allows any user to create files but permits ONLY the file\'s owner or root to delete it is the:',
        options: ['Sticky Bit', 'SUID (Set User ID)', 'SGID (Set Group ID)', 'Immutable Bit'],
        correctIndex: 0,
        topic: 'Linux OS',
        explanation: {
          steps: [
            'The Sticky bit on directories prevents users from deleting each other\'s temporary files.',
            'Represented by "t" in permissions (e.g. drwxrwxrwt).'
          ],
          keyConcept: 'Sticky Bit restricts file deletion in shared public directories to file owners.'
        }
      },
      {
        id: 30,
        question: 'Which category of hypervisor runs directly on bare physical host hardware without an underlying host operating system (e.g., VMware ESXi, KVM)?',
        options: ['Type 1 Hypervisor (Bare-Metal)', 'Type 2 Hypervisor (Hosted)', 'Type 3 Hypervisor', 'Container Engine'],
        correctIndex: 0,
        topic: 'Linux OS',
        explanation: {
          steps: [
            'Type 1 (Bare-Metal): Directly interfaces with host hardware for maximum virtualization performance.',
            'Type 2 (Hosted): Runs as an application on top of an existing host OS (e.g. VirtualBox).'
          ],
          keyConcept: 'Type 1 Hypervisors run directly on bare metal.'
        }
      }
    ]
  }
];
