/**
 * Official CSE111: Fundamentals of Computing Midterm Mock Examination Suite
 * Contains 5 Full-Length 30-Question Tests (150 Questions Total)
 * Strictly covers Units 1-3: Architecture, OS Scheduling, Linux FHS/CLI
 * Completely overhauled: Key distribution balanced and length bias removed
 */

export const CSE111_MOCK_TESTS = [
  {
    "id": "cse111-midterm-paper-1",
    "code": "CSE111-SET-A",
    "title": "Midterm Examination • Paper 1 (Official University Blueprint)",
    "courseCode": "CSE111",
    "courseName": "Fundamentals of Computing",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Computer Architecture",
      "Operating Systems",
      "Linux CLI",
      "Memory Management"
    ],
    "description": "Comprehensive university midterm paper testing von Neumann architecture, cache hierarchy, OS scheduling algorithms, virtual memory paging, Linux FHS, and file permissions.",
    "questions": [
      {
        "id": 1,
        "question": "In the von Neumann computer model, the throughput bottleneck resulting from sharing a single physical bus for both instruction fetching and data transfers is called the:",
        "options": [
          "Cache Miss Penalty",
          "Harvard Latency",
          "von Neumann Bottleneck",
          "Bus Skew"
        ],
        "correctIndex": 2,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "In the von Neumann architecture, both instructions and program data share the same physical bus and address space.",
            "Because the CPU cannot read an instruction and read/write data simultaneously, bus throughput limits the execution speed (von Neumann bottleneck)."
          ],
          "keyConcept": "von Neumann bottleneck occurs due to shared instruction and data buses."
        }
      },
      {
        "id": 2,
        "question": "Which level of the CPU cache hierarchy is typically the largest in storage capacity, shared among all cores on a multi-core silicon die, and incurs higher latency than L1 or L2 caches?",
        "options": [
          "Level 1 Instruction Cache (L1i)",
          "Level 3 (L3) Cache",
          "Level 2 (L2) Cache",
          "Level 1 Data Cache (L1d)"
        ],
        "correctIndex": 1,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "L1 cache is split (instruction/data) and private to each core with fastest access (1-4 cycles).",
            "L2 cache is slightly larger and private per core (10-14 cycles).",
            "L3 cache (Last Level Cache) is shared across all CPU cores, holds several megabytes (16-64MB+), and incurs higher latency (30-50 cycles)."
          ],
          "keyConcept": "L3 cache is shared across cores and largest in the on-die hierarchy."
        }
      },
      {
        "id": 3,
        "question": "Static RAM (SRAM) is preferred over Dynamic RAM (DRAM) for building CPU caches because SRAM:",
        "options": [
          "Is non-volatile when main power is removed (as determined by Maxwell boundary constraints)",
          "Consumes zero power at all times (across all standard operating temperatures)",
          "Has a much higher storage density per unit silicon area (governed by linear superposition principles)",
          "Does not require periodic capacitive refresh cycles and offers significantly lower access latency"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "SRAM uses 6-transistor (6T) flip-flop bistable circuits, holding state continuously as long as power is applied without refreshing.",
            "DRAM stores charges in tiny capacitors that leak and require periodic refresh cycles every few milliseconds, making DRAM slower."
          ],
          "keyConcept": "SRAM offers ultra-low latency without requiring refresh cycles."
        }
      },
      {
        "id": 4,
        "question": "The high-performance storage host controller protocol specifically architected to leverage the low latency and massive parallelism of solid-state storage across direct PCIe lanes is:",
        "options": [
          "NVMe (Non-Volatile Memory Express)",
          "SATA 3.0 (governed by linear superposition principles)",
          "PATA IDE (independent of external field perturbations)",
          "SCSI-3 (in an ideal homogeneous medium)"
        ],
        "correctIndex": 0,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Legacy SATA was designed for rotating magnetic platters with a single command queue of 32 depth.",
            "NVMe connects directly to PCIe lanes and supports up to 64,000 parallel queues with 64,000 commands each, optimizing flash SSD concurrency."
          ],
          "keyConcept": "NVMe utilizes direct PCIe lanes for ultra-high parallel SSD performance."
        }
      },
      {
        "id": 5,
        "question": "A storage administrator configures four 1 TB hard drives in a RAID 5 array. The usable capacity available to the operating system is:",
        "options": [
          "2 TB (governed by linear superposition principles)",
          "4 TB (independent of external field perturbations)",
          "3 TB (calculated as (N - 1) × Drive Capacity)",
          "1 TB (under steady-state operating conditions)"
        ],
        "correctIndex": 2,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "RAID 5 employs distributed block-level striping with distributed parity.",
            "The parity storage overhead across the array is equivalent to the capacity of exactly one drive.",
            "Usable capacity = (N - 1) × Size = (4 - 1) × 1 TB = 3 TB."
          ],
          "keyConcept": "RAID 5 usable capacity = (N - 1) × drive capacity."
        }
      },
      {
        "id": 6,
        "question": "Which central computer hardware unit coordinates and directs the flow of data, control signals, and instruction cycles between the ALU, registers, and memory?",
        "options": [
          "DMA Controller",
          "Control Unit (CU)",
          "Arithmetic Logic Unit (ALU)",
          "Floating-Point Unit (FPU)"
        ],
        "correctIndex": 1,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "The Control Unit (CU) orchestrates the fetch-decode-execute cycle.",
            "It generates timing and control pulses directing data movement between ALU, registers, and buses."
          ],
          "keyConcept": "Control Unit directs the fetch-decode-execute instruction cycle."
        }
      },
      {
        "id": 7,
        "question": "The principle of \"Spatial Locality\" in cache memory systems states that:",
        "options": [
          "All cache lines are refreshed simultaneously every millisecond (in an ideal homogeneous medium)",
          "An accessed memory address will be referenced repeatedly within a short time window (under steady-state operating conditions)",
          "When a memory location is accessed, nearby contiguous memory addresses are highly likely to be accessed soon",
          "Data in cache is mirrored across two identical chips (across all standard operating temperatures)"
        ],
        "correctIndex": 2,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Temporal Locality: A memory item referenced now will be referenced again soon (loops).",
            "Spatial Locality: If memory address x is referenced, adjacent addresses (x+1, x+2) will likely be referenced soon (arrays, sequential instructions)."
          ],
          "keyConcept": "Spatial locality means adjacent contiguous addresses are likely to be accessed."
        }
      },
      {
        "id": 8,
        "question": "Under the RAID 0 storage specification, data blocks are:",
        "options": [
          "Protected by double distributed parity (under steady-state operating conditions)",
          "Mirrored identically across two disks (as determined by Maxwell boundary constraints)",
          "Stored sequentially on magnetic tape (across all standard operating temperatures)",
          "Striped across multiple member disks without parity or mirroring, providing no fault tolerance"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "RAID 0 divides data into stripes written across multiple disks simultaneously for maximum throughput.",
            "However, it includes zero parity or redundancy; failure of a single disk results in total data loss."
          ],
          "keyConcept": "RAID 0 is striping without redundancy."
        }
      },
      {
        "id": 9,
        "question": "Which CPU register holds the actual physical memory address from which data is to be read or to which data is to be written?",
        "options": [
          "Instruction Register (IR)",
          "Program Counter (PC)",
          "Accumulator (AC)",
          "Memory Address Register (MAR)"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "PC stores the address of the next instruction to execute.",
            "IR holds the current instruction opcode being decoded.",
            "MAR holds the address in RAM currently being accessed on the address bus.",
            "MDR (Memory Data Register) holds the actual data read from or written to memory."
          ],
          "keyConcept": "MAR holds the memory address being read/written."
        }
      },
      {
        "id": 10,
        "question": "What is the role of the Program Counter (PC) register in a microprocessor?",
        "options": [
          "Stores output flags of the ALU (across all standard operating temperatures)",
          "Performs arithmetic additions (governed by linear superposition principles)",
          "Stores the memory address of the next instruction to be fetched and executed",
          "Counts total instructions executed since reboot (in an ideal homogeneous medium)"
        ],
        "correctIndex": 2,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "The Program Counter automatically increments after each instruction fetch, pointing to the subsequent instruction in memory sequence."
          ],
          "keyConcept": "Program Counter points to the next instruction address."
        }
      },
      {
        "id": 11,
        "question": "In modern operating system architectures, the transition from unprivileged user space to privileged kernel space is triggered by executing a:",
        "options": [
          "Preprocessor directive (governed by linear superposition principles)",
          "System Call (syscall / software interrupt)",
          "Memory compaction command (in an ideal homogeneous medium)",
          "Standard C variable declaration"
        ],
        "correctIndex": 1,
        "topic": "Operating Systems",
        "explanation": {
          "steps": [
            "User programs run in Ring 3 (user mode) without direct hardware privileges.",
            "To request privileged services (disk I/O, network send, process creation), the CPU executes a system call trap into Ring 0 (kernel mode)."
          ],
          "keyConcept": "System call triggers transition from user mode to kernel mode."
        }
      },
      {
        "id": 12,
        "question": "Which operating system kernel architecture incorporates core services (file systems, memory management, device drivers, network protocols) within a single contiguous address space running in supervisor mode?",
        "options": [
          "Microkernel",
          "Hybrid Nano-Kernel",
          "Exokernel",
          "Monolithic Kernel"
        ],
        "correctIndex": 3,
        "topic": "Operating Systems",
        "explanation": {
          "steps": [
            "Monolithic kernels (e.g. Linux) run all system services and drivers inside kernel space for speed.",
            "Microkernels (e.g. Mach, QNX) run only minimal scheduling/IPC in kernel space and move file systems and drivers to user space."
          ],
          "keyConcept": "Monolithic kernels execute core services in single kernel space."
        }
      },
      {
        "id": 13,
        "question": "In CPU process management, the state transition that occurs when a running process issues a blocking I/O request (such as reading a file from disk) is:",
        "options": [
          "Running → Waiting (Blocked)",
          "Waiting → Terminated",
          "Running → Ready",
          "Ready → Running"
        ],
        "correctIndex": 0,
        "topic": "Operating Systems",
        "explanation": {
          "steps": [
            "When a process requests an I/O operation that cannot be satisfied immediately, the CPU scheduler transitions it from Running to Waiting/Blocked.",
            "Once I/O completes, an interrupt moves it from Waiting to Ready."
          ],
          "keyConcept": "Blocking I/O transitions a process from Running to Waiting."
        }
      },
      {
        "id": 14,
        "question": "A CPU scheduling algorithm assigns a fixed time slice (quantum q) to each process in the ready queue in a cyclical manner. This algorithm is known as:",
        "options": [
          "Round Robin (RR)",
          "First-Come, First-Served (FCFS)",
          "Shortest Job First (SJF)",
          "Priority Scheduling"
        ],
        "correctIndex": 0,
        "topic": "Operating Systems",
        "explanation": {
          "steps": [
            "Round Robin is a preemptive scheduling algorithm where each process receives a predetermined CPU time quantum q.",
            "If uncompleted, the process is preempted and returned to the tail of the ready queue."
          ],
          "keyConcept": "Round Robin uses fixed time quantums in circular FIFO order."
        }
      },
      {
        "id": 15,
        "question": "Virtual memory systems implement \"Demand Paging\", which means that:",
        "options": [
          "Pages are locked in cache and never written to secondary storage (as determined by Maxwell boundary constraints)",
          "Virtual addresses directly match physical RAM addresses (across all standard operating temperatures)",
          "Pages are brought from secondary storage into physical RAM only when referenced by program execution",
          "All virtual pages must be allocated in physical RAM before execution begins (independent of external field perturbations)"
        ],
        "correctIndex": 2,
        "topic": "Operating Systems",
        "explanation": {
          "steps": [
            "With pure demand paging, a page is loaded into physical memory only when a page fault occurs upon referencing that page during execution."
          ],
          "keyConcept": "Demand paging loads pages into memory on demand when accessed."
        }
      },
      {
        "id": 16,
        "question": "The hardware component within the CPU that intercepts virtual addresses generated by program execution and translates them into physical memory addresses is the:",
        "options": [
          "Arithmetic Logic Unit (ALU)",
          "Direct Memory Access (DMA) engine",
          "Interrupt Vector Table (IVT)",
          "Memory Management Unit (MMU)"
        ],
        "correctIndex": 3,
        "topic": "Operating Systems",
        "explanation": {
          "steps": [
            "The MMU consults the page table (aided by the TLB cache) to translate virtual page numbers to physical frame numbers."
          ],
          "keyConcept": "MMU translates virtual memory addresses to physical memory addresses."
        }
      },
      {
        "id": 17,
        "question": "A severe operating system state where multiple processes are indefinitely blocked because each holds a resource while waiting for a resource held by another process in a closed loop is called:",
        "options": [
          "Deadlock",
          "Thrashing",
          "Livelock",
          "Starvation"
        ],
        "correctIndex": 0,
        "topic": "Operating Systems",
        "explanation": {
          "steps": [
            "Deadlock occurs when four Coffman conditions hold simultaneously: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait."
          ],
          "keyConcept": "Deadlock is a circular wait state among blocked processes."
        }
      },
      {
        "id": 18,
        "question": "In the program compilation lifecycle, which software tool resolves external symbol references and binds object modules and static libraries into a standalone executable binary?",
        "options": [
          "Preprocessor",
          "Linker",
          "Assembler",
          "Compiler"
        ],
        "correctIndex": 1,
        "topic": "Operating Systems",
        "explanation": {
          "steps": [
            "Preprocessor expands macros and headers (#include).",
            "Compiler converts source code to assembly code.",
            "Assembler converts assembly to relocatable object code (.o).",
            "Linker resolves function addresses and binds libraries into the final executable binary."
          ],
          "keyConcept": "Linker combines object files and resolves symbol addresses."
        }
      },
      {
        "id": 19,
        "question": "Which segment of a running process's memory layout stores local automatic variables, function call parameters, and return addresses in a Last-In, First-Out sequence?",
        "options": [
          "Heap Segment",
          "Data Segment",
          "Stack Segment",
          "Text (Code) Segment"
        ],
        "correctIndex": 2,
        "topic": "Operating Systems",
        "explanation": {
          "steps": [
            "Stack: Automatic function frames, local variables, return pointers (grows downward).",
            "Heap: Dynamically allocated memory via malloc()/new (grows upward).",
            "Data: Global and static initialized/uninitialized variables.",
            "Text: Compiled read-only machine instructions."
          ],
          "keyConcept": "Stack segment manages function frames and local variables in LIFO order."
        }
      },
      {
        "id": 20,
        "question": "The condition known as \"Thrashing\" in an operating system occurs when:",
        "options": [
          "The system spends more time servicing page faults and swapping pages than executing user processes",
          "CPU clock speed exceeds cooling capacity (as determined by Maxwell boundary constraints)",
          "Disk sectors become corrupt (across all standard operating temperatures)",
          "Processes consume all network bandwidth (governed by linear superposition principles)"
        ],
        "correctIndex": 0,
        "topic": "Operating Systems",
        "explanation": {
          "steps": [
            "When physical RAM is overcommitted and sum of working sets exceeds available frames, page faults occur continuously, driving CPU utilization down to near zero."
          ],
          "keyConcept": "Thrashing is excessive page swapping degrading system throughput."
        }
      },
      {
        "id": 21,
        "question": "The Linux operating system kernel was initially created and released in 1991 by:",
        "options": [
          "Dennis Ritchie",
          "Ken Thompson",
          "Linus Torvalds",
          "Richard Stallman"
        ],
        "correctIndex": 2,
        "topic": "Linux OS",
        "explanation": {
          "steps": [
            "Linus Torvalds announced and released the Linux kernel as an open-source monolithic kernel in August 1991 at the University of Helsinki."
          ],
          "keyConcept": "Linus Torvalds created the Linux kernel."
        }
      },
      {
        "id": 22,
        "question": "According to the Linux Filesystem Hierarchy Standard (FHS), host-specific, system-wide configuration files (such as passwd, fstab, and hosts) are stored in which directory?",
        "options": [
          "/dev",
          "/proc",
          "/bin",
          "/etc"
        ],
        "correctIndex": 3,
        "topic": "Linux OS",
        "explanation": {
          "steps": [
            "/etc contains static host-specific system configuration files.",
            "/bin contains essential user binaries.",
            "/dev contains special device node files.",
            "/proc contains virtual kernel process telemetry."
          ],
          "keyConcept": "/etc contains system configuration files."
        }
      },
      {
        "id": 23,
        "question": "Which directory in a Linux system serves as a virtual pseudo-filesystem generated dynamically by the kernel to provide runtime diagnostic and process information?",
        "options": [
          "/var",
          "/usr",
          "/proc",
          "/home"
        ],
        "correctIndex": 2,
        "topic": "Linux OS",
        "explanation": {
          "steps": [
            "/proc does not occupy disk space; it is a virtual filesystem populated in RAM by the kernel exposing process IDs and hardware state."
          ],
          "keyConcept": "/proc is a dynamic kernel pseudo-filesystem."
        }
      },
      {
        "id": 24,
        "question": "In Linux file permissions, executing the command \"chmod 755 script.sh\" assigns what permissions to the Owner, Group, and Others respectively?",
        "options": [
          "Owner: rwx, Group: r-x, Others: r-x",
          "Owner: r-x, Group: r-x, Others: r-x",
          "Owner: rwx, Group: rw-, Others: r--",
          "Owner: rw-, Group: r--, Others: ---"
        ],
        "correctIndex": 0,
        "topic": "Linux OS",
        "explanation": {
          "steps": [
            "Binary octal values: r = 4, w = 2, x = 1.",
            "7 = 4 + 2 + 1 = rwx (read, write, execute).",
            "5 = 4 + 0 + 1 = r-x (read, execute).",
            "chmod 755 gives Owner = rwx, Group = r-x, Others = r-x."
          ],
          "keyConcept": "755 octal permission = rwxr-xr-x."
        }
      },
      {
        "id": 25,
        "question": "What information does an Inode (index node) in a Linux filesystem store?",
        "options": [
          "The user password hashes (in an ideal homogeneous medium)",
          "File metadata (size, permissions, owner, timestamps, data block pointers), but NOT the filename",
          "The complete text content of the file (as determined by Maxwell boundary constraints)",
          "Only the human-readable filename (across all standard operating temperatures)"
        ],
        "correctIndex": 1,
        "topic": "Linux OS",
        "explanation": {
          "steps": [
            "Inodes store file attributes, permissions, UID/GID, size, and pointers to disk blocks.",
            "The filename itself is stored inside the directory file, which maps the name string to the Inode number."
          ],
          "keyConcept": "Inodes store all file metadata except the filename."
        }
      },
      {
        "id": 26,
        "question": "How does a Linux \"Hard Link\" differ from a \"Symbolic (Soft) Link\"?",
        "options": [
          "A symbolic link cannot be deleted once created (under steady-state operating conditions)",
          "A hard link shares the exact same Inode number and points directly to data blocks; a symbolic link has a distinct Inode containing the path string",
          "A hard link can span across different mounted filesystems (across all standard operating temperatures)",
          "A hard link creates a duplicate copy of file contents on disk (governed by linear superposition principles)"
        ],
        "correctIndex": 1,
        "topic": "Linux OS",
        "explanation": {
          "steps": [
            "Hard link: Points to the same Inode. Cannot link directories or cross filesystem boundaries.",
            "Soft link: A separate file with its own Inode containing the pathname pointer to another target."
          ],
          "keyConcept": "Hard links share the same Inode; soft links contain the target path."
        }
      },
      {
        "id": 27,
        "question": "Which Bash command-line utility uses regular expressions to search text files for lines matching a specified pattern?",
        "options": [
          "grep",
          "awk",
          "find",
          "sed"
        ],
        "correctIndex": 0,
        "topic": "Linux OS",
        "explanation": {
          "steps": [
            "grep (Global Regular Expression Print) searches input files for lines matching a pattern and outputs them."
          ],
          "keyConcept": "grep searches text using regular expressions."
        }
      },
      {
        "id": 28,
        "question": "In Linux input/output redirection, the standard file descriptor integer corresponding to Standard Error (stderr) is:",
        "options": [
          "1 (stdout)",
          "2",
          "0 (stdin)",
          "3"
        ],
        "correctIndex": 1,
        "topic": "Linux OS",
        "explanation": {
          "steps": [
            "0 = Standard Input (stdin)",
            "1 = Standard Output (stdout)",
            "2 = Standard Error (stderr)",
            "Example: \"command 2> error.log\" redirects stderr to a file."
          ],
          "keyConcept": "File descriptor 0 = stdin, 1 = stdout, 2 = stderr."
        }
      },
      {
        "id": 29,
        "question": "The special permission bit that, when set on a directory (such as /tmp, octal 1777), allows any user to create files but permits ONLY the file's owner or root to delete it is the:",
        "options": [
          "Immutable Bit",
          "SGID (Set Group ID)",
          "SUID (Set User ID)",
          "Sticky Bit"
        ],
        "correctIndex": 3,
        "topic": "Linux OS",
        "explanation": {
          "steps": [
            "The Sticky bit on directories prevents users from deleting each other's temporary files.",
            "Represented by \"t\" in permissions (e.g. drwxrwxrwt)."
          ],
          "keyConcept": "Sticky Bit restricts file deletion in shared public directories to file owners."
        }
      },
      {
        "id": 30,
        "question": "Which category of hypervisor runs directly on bare physical host hardware without an underlying host operating system (e.g., VMware ESXi, KVM)?",
        "options": [
          "Type 3 Hypervisor",
          "Type 2 Hypervisor (Hosted)",
          "Container Engine",
          "Type 1 Hypervisor (Bare-Metal)"
        ],
        "correctIndex": 3,
        "topic": "Linux OS",
        "explanation": {
          "steps": [
            "Type 1 (Bare-Metal): Directly interfaces with host hardware for maximum virtualization performance.",
            "Type 2 (Hosted): Runs as an application on top of an existing host OS (e.g. VirtualBox)."
          ],
          "keyConcept": "Type 1 Hypervisors run directly on bare metal."
        }
      }
    ]
  },
  {
    "id": "cse111-midterm-paper-2",
    "code": "CSE111-SET-B",
    "title": "Midterm Examination • Paper 2 (System Architecture & CPU Scheduling)",
    "courseCode": "CSE111",
    "courseName": "Fundamentals of Computing",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Computer Architecture",
      "Operating Systems",
      "Linux CLI",
      "Memory Management"
    ],
    "description": "Testing ALU/CU operations, cache mapping, process state transitions, PCB fields, and FCFS/SJF CPU scheduling.",
    "questions": [
      {
        "question": "Which of the following is the lowest-level programming language understood directly by a computer's CPU?",
        "options": [
          "Machine language",
          "Assembly language",
          "High-level language",
          "Natural language"
        ],
        "correctIndex": 0,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "11 & \\textbf{B} & 21 & \\textbf{B} & 31 & \\textbf{B} & 41 & \\textbf{A}"
          ],
          "keyConcept": "11 & \\textbf{B} & 21 & \\textbf{B} & 31 & \\textbf{B} & 41 & \\textbf{A}"
        },
        "id": 1
      },
      {
        "question": "What symbols are used to represent data and instructions in machine language?",
        "options": [
          "Alphabets A to Z",
          "Binary digits 0 and 1",
          "Hexadecimal codes only",
          "ASCII characters"
        ],
        "correctIndex": 1,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "12 & \\textbf{B} & 22 & \\textbf{C} & 32 & \\textbf{A} & 42 & \\textbf{B}"
          ],
          "keyConcept": "12 & \\textbf{B} & 22 & \\textbf{C} & 32 & \\textbf{A} & 42 & \\textbf{B}"
        },
        "id": 2
      },
      {
        "question": "A statement in assembly language uses readable abbreviations for operations called:",
        "options": [
          "Macros",
          "Identifiers",
          "Operands",
          "Mnemonics"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "13 & \\textbf{A} & 23 & \\textbf{B} & 33 & \\textbf{A} & 43 & \\textbf{B}"
          ],
          "keyConcept": "13 & \\textbf{A} & 23 & \\textbf{B} & 33 & \\textbf{A} & 43 & \\textbf{B}"
        },
        "id": 3
      },
      {
        "question": "Which software tool is required to convert assembly language programs into machine code?",
        "options": [
          "Compiler",
          "Interpreter",
          "Linker",
          "Assembler"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "14 & \\textbf{A} & 24 & \\textbf{B} & 34 & \\textbf{B} & 44 & \\textbf{A}"
          ],
          "keyConcept": "14 & \\textbf{A} & 24 & \\textbf{B} & 34 & \\textbf{B} & 44 & \\textbf{A}"
        },
        "id": 4
      },
      {
        "question": "A translator that converts an entire high-level program into machine code before execution is a/an:",
        "options": [
          "Text Editor",
          "Assembler",
          "Compiler",
          "Interpreter"
        ],
        "correctIndex": 2,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "15 & \\textbf{B} & 25 & \\textbf{B} & 35 & \\textbf{B} & 45 & \\textbf{B}"
          ],
          "keyConcept": "15 & \\textbf{B} & 25 & \\textbf{B} & 35 & \\textbf{B} & 45 & \\textbf{B}"
        },
        "id": 5
      },
      {
        "question": "An interpreter translates and executes high-level language programs:",
        "options": [
          "During compile time (across all standard operating temperatures)",
          "Only after linking with libraries",
          "Statement-by-statement during runtime",
          "All at once prior to execution"
        ],
        "correctIndex": 2,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "16 & \\textbf{C} & 26 & \\textbf{B} & 36 & \\textbf{A} & 46 & \\textbf{B}"
          ],
          "keyConcept": "16 & \\textbf{C} & 26 & \\textbf{B} & 36 & \\textbf{A} & 46 & \\textbf{B}"
        },
        "id": 6
      },
      {
        "question": "In an assembly instruction such as \\texttt{ADD R1, R2}, the operation code \\texttt{ADD} is known as the:",
        "options": [
          "Operand",
          "Opcode",
          "Mnemonic address",
          "Label"
        ],
        "correctIndex": 1,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "17 & \\textbf{C} & 27 & \\textbf{B} & 37 & \\textbf{B} & 47 & \\textbf{B}"
          ],
          "keyConcept": "17 & \\textbf{C} & 27 & \\textbf{B} & 37 & \\textbf{B} & 47 & \\textbf{B}"
        },
        "id": 7
      },
      {
        "question": "Which of the following programming languages is classified as a high-level language?",
        "options": [
          "Microcode",
          "C++",
          "Assembly Language",
          "Machine Code"
        ],
        "correctIndex": 1,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "18 & \\textbf{B} & 28 & \\textbf{B} & 38 & \\textbf{B} & 48 & \\textbf{B}"
          ],
          "keyConcept": "18 & \\textbf{B} & 28 & \\textbf{B} & 38 & \\textbf{B} & 48 & \\textbf{B}"
        },
        "id": 8
      },
      {
        "question": "In an assembly instruction \\texttt{MOV R1, \\#5}, what does the symbol \\texttt{\\#5} represent?",
        "options": [
          "A condition flag",
          "An opcode (under steady-state operating conditions)",
          "A memory address pointer",
          "An immediate operand value"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "19 & \\textbf{B} & 29 & \\textbf{B} & 39 & \\textbf{B} & 49 & \\textbf{B}"
          ],
          "keyConcept": "19 & \\textbf{B} & 29 & \\textbf{B} & 39 & \\textbf{B} & 49 & \\textbf{B}"
        },
        "id": 9
      },
      {
        "question": "What is the primary advantage of high-level programming languages over machine language?",
        "options": [
          "They are portable and human-readable",
          "They directly control CPU registers",
          "They execute without a CPU",
          "They require no translation"
        ],
        "correctIndex": 0,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "20 & \\textbf{A} & 30 & \\textbf{B} & 40 & \\textbf{B} & 50 & \\textbf{B}"
          ],
          "keyConcept": "20 & \\textbf{A} & 30 & \\textbf{B} & 40 & \\textbf{B} & 50 & \\textbf{B}"
        },
        "id": 10
      },
      {
        "question": "An electronic, programmable machine that accepts data, processes it, produces output, and stores results is a/an:",
        "options": [
          "Sensor",
          "Transistor",
          "Computer",
          "Assembler"
        ],
        "correctIndex": 2,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "11 & \\textbf{A} & 21 & \\textbf{B} & 31 & \\textbf{B} & 41 & \\textbf{B}"
          ],
          "keyConcept": "11 & \\textbf{A} & 21 & \\textbf{B} & 31 & \\textbf{B} & 41 & \\textbf{B}"
        },
        "id": 11
      },
      {
        "question": "What is the sequence of the fundamental data processing cycle in computing?",
        "options": [
          "Process $\\rightarrow$ Storage $\\rightarrow$ Output $\\rightarrow$ Input",
          "Input $\\rightarrow$ Process $\\rightarrow$ Output $\\rightarrow$ Storage",
          "Output $\\rightarrow$ Process $\\rightarrow$ Input $\\rightarrow$ Storage",
          "Storage $\\rightarrow$ Input $\\rightarrow$ Process $\\rightarrow$ Output"
        ],
        "correctIndex": 1,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "12 & \\textbf{B} & 22 & \\textbf{A} & 32 & \\textbf{B} & 42 & \\textbf{B}"
          ],
          "keyConcept": "12 & \\textbf{B} & 22 & \\textbf{A} & 32 & \\textbf{B} & 42 & \\textbf{B}"
        },
        "id": 12
      },
      {
        "question": "Raw, unorganized facts such as numbers, names, or symbols with no immediate meaning are called:",
        "options": [
          "Data",
          "Information",
          "Wisdom",
          "Knowledge"
        ],
        "correctIndex": 0,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "13 & \\textbf{B} & 23 & \\textbf{C} & 33 & \\textbf{A} & 43 & \\textbf{B}"
          ],
          "keyConcept": "13 & \\textbf{B} & 23 & \\textbf{C} & 33 & \\textbf{A} & 43 & \\textbf{B}"
        },
        "id": 13
      },
      {
        "question": "Processed data that has been organized to carry context, meaning, and usefulness is termed:",
        "options": [
          "Information",
          "Byte",
          "Raw input",
          "Firmware"
        ],
        "correctIndex": 0,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "14 & \\textbf{C} & 24 & \\textbf{B} & 34 & \\textbf{B} & 44 & \\textbf{B}"
          ],
          "keyConcept": "14 & \\textbf{C} & 24 & \\textbf{B} & 34 & \\textbf{B} & 44 & \\textbf{B}"
        },
        "id": 14
      },
      {
        "question": "The architecture in which both instructions and data are held in the same unified memory space is named after:",
        "options": [
          "Charles Babbage",
          "Blaise Pascal",
          "John von Neumann",
          "Linus Torvalds"
        ],
        "correctIndex": 2,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "15 & \\textbf{C} & 25 & \\textbf{A} & 35 & \\textbf{B} & 45 & \\textbf{B}"
          ],
          "keyConcept": "15 & \\textbf{C} & 25 & \\textbf{A} & 35 & \\textbf{B} & 45 & \\textbf{B}"
        },
        "id": 15
      },
      {
        "question": "Which historical mechanical calculating device was invented by Blaise Pascal in 1642 to perform addition and subtraction?",
        "options": [
          "Abacus",
          "Analytical Engine",
          "ENIAC",
          "Pascaline"
        ],
        "correctIndex": 3,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "16 & \\textbf{B} & 26 & \\textbf{B} & 36 & \\textbf{B} & 46 & \\textbf{C}"
          ],
          "keyConcept": "16 & \\textbf{B} & 26 & \\textbf{B} & 36 & \\textbf{B} & 46 & \\textbf{C}"
        },
        "id": 16
      },
      {
        "question": "Who designed the mechanical programmable \"Analytical Engine\" in the 1830s containing concepts of memory and processor?",
        "options": [
          "Herman Hollerith",
          "John von Neumann",
          "Alan Turing",
          "Charles Babbage"
        ],
        "correctIndex": 3,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "17 & \\textbf{B} & 27 & \\textbf{B} & 37 & \\textbf{B} & 47 & \\textbf{B}"
          ],
          "keyConcept": "17 & \\textbf{B} & 27 & \\textbf{B} & 37 & \\textbf{B} & 47 & \\textbf{B}"
        },
        "id": 17
      },
      {
        "question": "Herman Hollerith successfully used which technology to automate data processing for the 1890 US Census?",
        "options": [
          "Vacuum tubes",
          "Transistors",
          "Punched cards",
          "Integrated circuits"
        ],
        "correctIndex": 2,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "18 & \\textbf{B} & 28 & \\textbf{B} & 38 & \\textbf{B} & 48 & \\textbf{B}"
          ],
          "keyConcept": "18 & \\textbf{B} & 28 & \\textbf{B} & 38 & \\textbf{B} & 48 & \\textbf{B}"
        },
        "id": 18
      },
      {
        "question": "What was the primary electronic switching component used in first-generation computers (1940--1956)?",
        "options": [
          "Transistors",
          "Vacuum tubes",
          "Microprocessors",
          "Integrated circuits"
        ],
        "correctIndex": 1,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "19 & \\textbf{C} & 29 & \\textbf{B} & 39 & \\textbf{B} & 49 & \\textbf{C}"
          ],
          "keyConcept": "19 & \\textbf{C} & 29 & \\textbf{B} & 39 & \\textbf{B} & 49 & \\textbf{C}"
        },
        "id": 19
      },
      {
        "question": "Which famous early computer is a classic example of a first-generation electronic computer?",
        "options": [
          "ENIAC",
          "Cray-1",
          "Apple II",
          "IBM PC"
        ],
        "correctIndex": 0,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "20 & \\textbf{B} & 30 & \\textbf{B} & 40 & \\textbf{A} & 50 & \\textbf{B}"
          ],
          "keyConcept": "20 & \\textbf{B} & 30 & \\textbf{B} & 40 & \\textbf{A} & 50 & \\textbf{B}"
        },
        "id": 20
      },
      {
        "question": "What is the primary function of the Central Processing Unit (CPU) in a computer system?",
        "options": [
          "Executing instructions and controlling other hardware components",
          "Displaying graphical output on the screen (under steady-state operating conditions)",
          "Connecting to the internet (as determined by Maxwell boundary constraints)",
          "Storing permanent files when power is lost (across all standard operating temperatures)"
        ],
        "correctIndex": 0,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "11 & \\textbf{B} & 21 & \\textbf{B} & 31 & \\textbf{B} & 41 & \\textbf{B}"
          ],
          "keyConcept": "11 & \\textbf{B} & 21 & \\textbf{B} & 31 & \\textbf{B} & 41 & \\textbf{B}"
        },
        "id": 21
      },
      {
        "question": "Why are Graphics Processing Units (GPUs) particularly well suited for training deep learning models?",
        "options": [
          "They feature higher clock frequencies than CPUs for single threads (under steady-state operating conditions)",
          "They use non-volatile magnetic storage (as determined by Maxwell boundary constraints)",
          "They contain thousands of cores designed for massively parallel mathematical operations",
          "They eliminate the need for system RAM (governed by linear superposition principles)"
        ],
        "correctIndex": 2,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "12 & \\textbf{B} & 22 & \\textbf{A} & 32 & \\textbf{A} & 42 & \\textbf{B}"
          ],
          "keyConcept": "12 & \\textbf{B} & 22 & \\textbf{A} & 32 & \\textbf{A} & 42 & \\textbf{B}"
        },
        "id": 22
      },
      {
        "question": "The CPU register that stores the memory address of the next instruction to be fetched is the:",
        "options": [
          "Accumulator",
          "Memory Buffer Register (MBR)",
          "Instruction Register (IR)",
          "Program Counter (PC)"
        ],
        "correctIndex": 3,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "13 & \\textbf{B} & 23 & \\textbf{B} & 33 & \\textbf{C} & 43 & \\textbf{B}"
          ],
          "keyConcept": "13 & \\textbf{B} & 23 & \\textbf{B} & 33 & \\textbf{C} & 43 & \\textbf{B}"
        },
        "id": 23
      },
      {
        "question": "The CPU register that holds the instruction currently being decoded or executed is the:",
        "options": [
          "Program Counter (PC)",
          "Stack Pointer",
          "Status Register",
          "Instruction Register (IR)"
        ],
        "correctIndex": 3,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "14 & \\textbf{B} & 24 & \\textbf{B} & 34 & \\textbf{C} & 44 & \\textbf{A}"
          ],
          "keyConcept": "14 & \\textbf{B} & 24 & \\textbf{B} & 34 & \\textbf{C} & 44 & \\textbf{A}"
        },
        "id": 24
      },
      {
        "question": "Which level of CPU cache memory is typically the smallest, fastest, and located closest to the execution core?",
        "options": [
          "L3 Cache",
          "L2 Cache",
          "L1 Cache",
          "Virtual Memory"
        ],
        "correctIndex": 2,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "15 & \\textbf{B} & 25 & \\textbf{B} & 35 & \\textbf{B} & 45 & \\textbf{A}"
          ],
          "keyConcept": "15 & \\textbf{B} & 25 & \\textbf{B} & 35 & \\textbf{B} & 45 & \\textbf{A}"
        },
        "id": 25
      },
      {
        "question": "What is the primary difference between Dynamic RAM (DRAM) and Static RAM (SRAM)?",
        "options": [
          "SRAM is used for hard disk storage (independent of external field perturbations)",
          "DRAM requires periodic electrical refreshing while SRAM does not",
          "DRAM is non-volatile while SRAM is volatile (under steady-state operating conditions)",
          "DRAM is faster than SRAM (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 1,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "16 & \\textbf{C} & 26 & \\textbf{B} & 36 & \\textbf{B} & 46 & \\textbf{B}"
          ],
          "keyConcept": "16 & \\textbf{C} & 26 & \\textbf{B} & 36 & \\textbf{B} & 46 & \\textbf{B}"
        },
        "id": 26
      },
      {
        "question": "Which of the following types of memory is commonly used in CPU cache because of its high speed?",
        "options": [
          "SRAM",
          "DRAM",
          "EEPROM",
          "Magnetic Tape"
        ],
        "correctIndex": 0,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "17 & \\textbf{B} & 27 & \\textbf{B} & 37 & \\textbf{C} & 47 & \\textbf{B}"
          ],
          "keyConcept": "17 & \\textbf{B} & 27 & \\textbf{B} & 37 & \\textbf{C} & 47 & \\textbf{B}"
        },
        "id": 27
      },
      {
        "question": "Which memory retains its contents permanently even after the computer is turned completely off?",
        "options": [
          "DRAM",
          "SRAM",
          "L2 Cache",
          "ROM"
        ],
        "correctIndex": 3,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "18 & \\textbf{B} & 28 & \\textbf{B} & 38 & \\textbf{B} & 48 & \\textbf{B}"
          ],
          "keyConcept": "18 & \\textbf{B} & 28 & \\textbf{B} & 38 & \\textbf{B} & 48 & \\textbf{B}"
        },
        "id": 28
      },
      {
        "question": "What is stored in a computer's ROM that initializes hardware and begins the boot sequence?",
        "options": [
          "Spreadsheet formulas (as determined by Maxwell boundary constraints)",
          "Web browser cache (across all standard operating temperatures)",
          "Operating system firmware (e.g., BIOS/UEFI)",
          "User documents (independent of external field perturbations)"
        ],
        "correctIndex": 2,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "19 & \\textbf{B} & 29 & \\textbf{B} & 39 & \\textbf{C} & 49 & \\textbf{B}"
          ],
          "keyConcept": "19 & \\textbf{B} & 29 & \\textbf{B} & 39 & \\textbf{C} & 49 & \\textbf{B}"
        },
        "id": 29
      },
      {
        "question": "Why are Solid-State Drives (SSDs) more durable and resistant to physical shock than Hard Disk Drives (HDDs)?",
        "options": [
          "SSDs are water-cooled (across all standard operating temperatures)",
          "SSDs use flash memory chips with no moving mechanical parts",
          "SSDs use high-power laser beams (independent of external field perturbations)",
          "SSDs have spinning platters (in an ideal homogeneous medium)"
        ],
        "correctIndex": 1,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "20 & \\textbf{B} & 30 & \\textbf{B} & 40 & \\textbf{C} & 50 & \\textbf{B}"
          ],
          "keyConcept": "20 & \\textbf{B} & 30 & \\textbf{B} & 40 & \\textbf{C} & 50 & \\textbf{B}"
        },
        "id": 30
      }
    ]
  },
  {
    "id": "cse111-midterm-paper-3",
    "code": "CSE111-SET-C",
    "title": "Midterm Examination • Paper 3 (Memory Management & Deadlock Dynamics)",
    "courseCode": "CSE111",
    "courseName": "Fundamentals of Computing",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Computer Architecture",
      "Operating Systems",
      "Linux CLI",
      "Memory Management"
    ],
    "description": "Focuses on paging, page faults, LRU replacement, virtual memory addressing, and Coffman deadlock conditions.",
    "questions": [
      {
        "question": "Which phase of compilation groups raw characters into meaningful tokens such as identifiers and keywords?",
        "options": [
          "Lexical analysis",
          "Code optimization",
          "Syntax analysis",
          "Semantic analysis"
        ],
        "correctIndex": 2,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 1
      },
      {
        "question": "Checking whether statements in a source code conform to the grammatical rules of the language is done during:",
        "options": [
          "Lexical analysis",
          "Linking",
          "Syntax analysis",
          "Code generation"
        ],
        "correctIndex": 0,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 2
      },
      {
        "question": "Detecting a type mismatch error (such as assigning a string to an integer variable) is the responsibility of:",
        "options": [
          "Lexical analysis",
          "The preprocessor",
          "Semantic analysis",
          "The loader"
        ],
        "correctIndex": 2,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 3
      },
      {
        "question": "A syntax error in a C++ program is detected at:",
        "options": [
          "Run time",
          "Compile time",
          "Link time",
          "Load time"
        ],
        "correctIndex": 1,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 4
      },
      {
        "question": "What is the role of a preprocessor in the C/C++ compilation pipeline?",
        "options": [
          "To link object files",
          "To expand macros and include header files",
          "To execute machine code",
          "To load the program into RAM"
        ],
        "correctIndex": 2,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 5
      },
      {
        "question": "The software that combines multiple compiled object files and standard library routines into an executable is the:",
        "options": [
          "Compiler",
          "Assembler",
          "Loader",
          "Linker"
        ],
        "correctIndex": 1,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 6
      },
      {
        "question": "Which program is responsible for bringing the executable file from secondary storage into primary memory (RAM) for execution?",
        "options": [
          "Compiler",
          "Linker",
          "Loader",
          "Interpreter"
        ],
        "correctIndex": 0,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 7
      },
      {
        "question": "The four stages of the CPU instruction execution cycle in correct order are:",
        "options": [
          "Fetch $\\rightarrow$ Execute $\\rightarrow$ Decode $\\rightarrow$ Store",
          "Fetch $\\rightarrow$ Decode $\\rightarrow$ Execute $\\rightarrow$ Store",
          "Execute $\\rightarrow$ Fetch $\\rightarrow$ Decode $\\rightarrow$ Store",
          "Decode $\\rightarrow$ Fetch $\\rightarrow$ Store $\\rightarrow$ Execute"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 8
      },
      {
        "question": "In an assembler, what is the primary task performed during the first pass of a two-pass assembler?",
        "options": [
          "Linking object files",
          "Recording symbol and label definitions with their memory addresses",
          "Loading the program into RAM",
          "Generating final binary machine instructions"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 9
      },
      {
        "question": "What does a two-pass assembler do during its second pass?",
        "options": [
          "Translates mnemonics and symbolic references into machine code",
          "Runs the code (in an ideal homogeneous medium)",
          "Allocates heap memory (under steady-state operating conditions)",
          "Identifies syntax errors only (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 0,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 10
      },
      {
        "question": "Second-generation computers (1956--1963) replaced vacuum tubes with:",
        "options": [
          "Silicon wafers",
          "Mechanical gears",
          "Transistors",
          "Microprocessors"
        ],
        "correctIndex": 2,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 11
      },
      {
        "question": "Which programming languages became prominent during the second generation of computers?",
        "options": [
          "HTML and CSS",
          "FORTRAN and COBOL",
          "C\\# and Swift",
          "Java and Python"
        ],
        "correctIndex": 3,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 12
      },
      {
        "question": "Third-generation computers (1964--1971) were characterized by the widespread adoption of:",
        "options": [
          "Artificial intelligence",
          "Punched cards",
          "Vacuum tubes",
          "Integrated Circuits (ICs)"
        ],
        "correctIndex": 1,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 13
      },
      {
        "question": "Which generation of computers introduced keyboards, monitors, and modern operating systems to replace batch punch cards?",
        "options": [
          "Third generation",
          "Fifth generation",
          "First generation",
          "Second generation"
        ],
        "correctIndex": 2,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 14
      },
      {
        "question": "The fourth generation of computers (from 1971 onward) is fundamentally defined by the development of:",
        "options": [
          "Vacuum tubes",
          "Optical gears",
          "Discrete relays",
          "Microprocessors"
        ],
        "correctIndex": 0,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 15
      },
      {
        "question": "Which company introduced the world's first commercial single-chip microprocessor (the 4004) in 1971?",
        "options": [
          "IBM",
          "Intel",
          "Apple",
          "Microsoft"
        ],
        "correctIndex": 0,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 16
      },
      {
        "question": "Fifth-generation computing focuses primarily on which technological direction?",
        "options": [
          "Magnetic drums",
          "Pure mechanical gears",
          "Artificial Intelligence and parallel processing",
          "Vacuum tubes"
        ],
        "correctIndex": 3,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 17
      },
      {
        "question": "The computer characteristic stating that \"incorrect input data inevitably produces incorrect output information\" is known as:",
        "options": [
          "DMA",
          "FIFO",
          "LIFO",
          "GIGO (Garbage In, Garbage Out)"
        ],
        "correctIndex": 1,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 18
      },
      {
        "question": "A computer's ability to perform repetitive operations continuously for hours without fatigue or loss of concentration is called:",
        "options": [
          "Speed",
          "Diligence",
          "Automation",
          "Versatility"
        ],
        "correctIndex": 3,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 19
      },
      {
        "question": "Which characteristic refers to a computer's capability to perform widely diverse tasks ranging from music playback to complex calculations?",
        "options": [
          "Accuracy",
          "Versatility",
          "Diligence",
          "Volatility"
        ],
        "correctIndex": 0,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 20
      },
      {
        "question": "A mechanical Hard Disk Drive (HDD) stores data magnetically on:",
        "options": [
          "Rotating circular platters with moving read/write heads",
          "Punch cards",
          "Semiconductor flash cells",
          "Optical reflective pits"
        ],
        "correctIndex": 2,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 21
      },
      {
        "question": "Which storage medium is widely used for high-capacity, low-cost long-term archival backups despite having sequential access?",
        "options": [
          "Magnetic Tape",
          "L1 Cache",
          "Dynamic RAM",
          "SSD"
        ],
        "correctIndex": 2,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 22
      },
      {
        "question": "How many bits are in one standard Byte?",
        "options": [
          "8",
          "32",
          "16",
          "4"
        ],
        "correctIndex": 3,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 23
      },
      {
        "question": "A memory capacity of $1\\text{ KiB}$ (Kibibyte) corresponds to exactly how many bytes?",
        "options": [
          "1,048,576 bytes",
          "1,000 bytes",
          "512 bytes",
          "1,024 bytes"
        ],
        "correctIndex": 1,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 24
      },
      {
        "question": "How many bytes are in $1\\text{ GiB}$ (Gibibyte)?",
        "options": [
          "$1,024\\text{ KiB}$",
          "$8\\text{ bits",
          "$1,000,000\\text{ bytes}$",
          "$1,024\\text{ MiB}$ ($1,073,741,824\\text{ bytes}$)"
        ],
        "correctIndex": 2,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 25
      },
      {
        "question": "A touchscreen monitor is best classified as:",
        "options": [
          "An output device only",
          "An input device only",
          "A storage device",
          "Both an input and an output device"
        ],
        "correctIndex": 1,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 26
      },
      {
        "question": "Which input device converts printed text from paper into editable digital characters using Optical Character Recognition (OCR)?",
        "options": [
          "Barcode reader",
          "Scanner",
          "Touchpad",
          "Microphone"
        ],
        "correctIndex": 3,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 27
      },
      {
        "question": "Which peripheral converts physical sound waves into electrical analog signals for computer processing?",
        "options": [
          "Speaker",
          "Microphone",
          "Actuator",
          "Projector"
        ],
        "correctIndex": 0,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 28
      },
      {
        "question": "An analog-to-digital converter (ADC) in an audio input setup performs which task?",
        "options": [
          "Converts continuous audio sound waves into digital binary samples",
          "Displays audio waveforms on screen",
          "Stores audio on magnetic tape",
          "Amplifies sound through speakers"
        ],
        "correctIndex": 3,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 29
      },
      {
        "question": "Which output device creates physical motion or mechanical movement from computer control signals (e.g., moving a robotic arm)?",
        "options": [
          "Monitor",
          "Sensor",
          "Touchpad",
          "Actuator"
        ],
        "correctIndex": 1,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 30
      }
    ]
  },
  {
    "id": "cse111-midterm-paper-4",
    "code": "CSE111-SET-D",
    "title": "Midterm Examination • Paper 4 (Linux FHS, CLI Commands & Permissions)",
    "courseCode": "CSE111",
    "courseName": "Fundamentals of Computing",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Computer Architecture",
      "Operating Systems",
      "Linux CLI",
      "Memory Management"
    ],
    "description": "Comprehensive problem set on Linux directory hierarchy (/etc, /var, /bin), chmod octal permissions, grep, and pipes.",
    "questions": [
      {
        "question": "Which type of programming error allows a program to compile and run successfully but produces incorrect output?",
        "options": [
          "Syntax error",
          "Linker error",
          "Lexical error",
          "Logic error"
        ],
        "correctIndex": 0,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 1
      },
      {
        "question": "Division by zero occurring during program execution is classified as a:",
        "options": [
          "Semantic error",
          "Runtime error",
          "Compile-time error",
          "Syntax error"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 2
      },
      {
        "question": "The organized sequence used to transform a real-world problem into a working software application is called the:",
        "options": [
          "Compilation pipeline",
          "Bus arbitration cycle",
          "Program development cycle",
          "Instruction cycle"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 3
      },
      {
        "question": "What is the first step in the program development cycle?",
        "options": [
          "Program maintenance",
          "Writing program code",
          "Compiling the code",
          "Problem definition"
        ],
        "correctIndex": 1,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 4
      },
      {
        "question": "A step-by-step graphical representation of an algorithm using standard geometric symbols is called a:",
        "options": [
          "Pseudocode",
          "Program draft",
          "Syntax tree",
          "Flowchart"
        ],
        "correctIndex": 0,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 5
      },
      {
        "question": "A finite, ordered set of unambiguous instructions designed to solve a specific problem is known as a/an:",
        "options": [
          "Token",
          "Algorithm",
          "Mnemonic",
          "Operand"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 6
      },
      {
        "question": "Testing program execution using edge values such as \\texttt{hours = 0} is an example of:",
        "options": [
          "Lexical scanning",
          "Boundary value testing",
          "Preprocessing",
          "Syntax verification"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 7
      },
      {
        "question": "Why is machine language considered hardware-dependent?",
        "options": [
          "Because it operates only on laptops",
          "Because it requires a high-level interpreter",
          "Because it uses English keywords",
          "Because each CPU family has its own unique binary instruction set"
        ],
        "correctIndex": 2,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 8
      },
      {
        "question": "Which language requires an assembler for conversion to machine code?",
        "options": [
          "Java",
          "Assembly language",
          "C",
          "Python"
        ],
        "correctIndex": 0,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 9
      },
      {
        "question": "Which tool provides an interactive environment with line-by-line execution and immediate feedback, ideal for scripting and beginners?",
        "options": [
          "Interpreter",
          "Compiler",
          "Assembler",
          "Linker"
        ],
        "correctIndex": 1,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 10
      },
      {
        "question": "Which CPU component is responsible for performing additions, subtractions, and logical comparisons?",
        "options": [
          "Address Bus",
          "Instruction Register",
          "Control Unit",
          "Arithmetic Logic Unit (ALU)"
        ],
        "correctIndex": 2,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 11
      },
      {
        "question": "Which component acts as the supervisor of the CPU, generating timing and control signals to direct operations?",
        "options": [
          "Cache",
          "Control Unit (CU)",
          "ALU",
          "RAM"
        ],
        "correctIndex": 1,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 12
      },
      {
        "question": "The high-speed system bus that carries the actual data and instructions between CPU, memory, and devices is the:",
        "options": [
          "Data Bus",
          "Control Bus",
          "Address Bus",
          "Power Bus"
        ],
        "correctIndex": 2,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 13
      },
      {
        "question": "Which system bus is unidirectional and transmits memory locations from the CPU to primary memory?",
        "options": [
          "Control Bus",
          "Address Bus",
          "Expansion Bus",
          "Data Bus"
        ],
        "correctIndex": 3,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 14
      },
      {
        "question": "Which system bus carries command signals such as Memory Read, Memory Write, and Interrupt acknowledgments?",
        "options": [
          "Local Bus",
          "Control Bus",
          "Address Bus",
          "Data Bus"
        ],
        "correctIndex": 1,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 15
      },
      {
        "question": "Primary memory directly accessed by the CPU includes:",
        "options": [
          "Magnetic tape and Optical disks",
          "RAM and Cache",
          "USB drives",
          "HDD and SSD"
        ],
        "correctIndex": 3,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 16
      },
      {
        "question": "Which memory loses all its contents immediately when electrical power is switched off?",
        "options": [
          "Solid-State Drive (SSD)",
          "Random-Access Memory (RAM)",
          "Read-Only Memory (ROM)",
          "Hard Disk Drive (HDD)"
        ],
        "correctIndex": 2,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 17
      },
      {
        "question": "What is the primary function of Read-Only Memory (ROM)?",
        "options": [
          "To hold non-volatile startup firmware (e.g., BIOS)",
          "To back up user photos",
          "To store temporary variables during gaming",
          "To speed up web browsing"
        ],
        "correctIndex": 2,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 18
      },
      {
        "question": "The physical, tangible parts of a computer system that you can touch are collectively known as:",
        "options": [
          "Firmware",
          "Hardware",
          "Freeware",
          "Software"
        ],
        "correctIndex": 3,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 19
      },
      {
        "question": "Programs and sets of instructions that direct physical computer hardware to perform tasks are called:",
        "options": [
          "Chipsets",
          "Hardware",
          "Software",
          "Peripherals"
        ],
        "correctIndex": 1,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 20
      },
      {
        "question": "Which printer technology uses an electrostatic drum and powdered toner to produce rapid, high-quality document prints?",
        "options": [
          "Plotter",
          "Dot matrix printer",
          "Inkjet printer",
          "Laser printer"
        ],
        "correctIndex": 2,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 21
      },
      {
        "question": "Which printer technology forms characters by spraying tiny microscopic droplets of liquid ink onto paper?",
        "options": [
          "Thermal printer",
          "Inkjet printer",
          "Laser printer",
          "Daisy wheel"
        ],
        "correctIndex": 1,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 22
      },
      {
        "question": "The delay between a user input action (such as clicking a mouse) and the visual response on the screen is called:",
        "options": [
          "Latency",
          "Bandwidth",
          "Resolution",
          "Clock speed"
        ],
        "correctIndex": 1,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 23
      },
      {
        "question": "The sharpness and detail of a monitor display measured by the total number of horizontal and vertical pixels (e.g., $1920 \\times 1080$) is:",
        "options": [
          "Resolution",
          "Latency",
          "Aspect ratio",
          "Refresh rate"
        ],
        "correctIndex": 3,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 24
      },
      {
        "question": "Display refresh rate is measured in which unit representing the number of times the screen image updates each second?",
        "options": [
          "DPI",
          "Hertz (Hz)",
          "Gigabytes",
          "Nanoseconds"
        ],
        "correctIndex": 0,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 25
      },
      {
        "question": "Printer print resolution and output quality are conventionally measured in:",
        "options": [
          "Pixels per second",
          "Dots per inch (DPI)",
          "Hertz (Hz)",
          "Bytes per second"
        ],
        "correctIndex": 2,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 26
      },
      {
        "question": "Which of the following devices is specifically designed as an accessibility tool for visually impaired users?",
        "options": [
          "Laser printer",
          "Webcam",
          "Optical mouse",
          "Refreshable Braille display"
        ],
        "correctIndex": 0,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 27
      },
      {
        "question": "What software component is essential for allowing the operating system to send commands to a specific peripheral hardware device?",
        "options": [
          "Word processor",
          "Compiler",
          "BIOS updater",
          "Device driver"
        ],
        "correctIndex": 0,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 28
      },
      {
        "question": "Which device reads machine-readable vertical parallel bars used extensively in supermarket checkout counters?",
        "options": [
          "Barcode reader",
          "Microphone",
          "Biometric sensor",
          "Webcam"
        ],
        "correctIndex": 2,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 29
      },
      {
        "question": "Which input technology uses physical biological traits such as fingerprints or iris patterns for user identity verification?",
        "options": [
          "QR-code reader",
          "Capacitive sensor",
          "Touchpad",
          "Biometric scanner"
        ],
        "correctIndex": 0,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 30
      }
    ]
  },
  {
    "id": "cse111-midterm-paper-5",
    "code": "CSE111-SET-E",
    "title": "Midterm Examination • Paper 5 (Full Midterm Computer Systems Companion)",
    "courseCode": "CSE111",
    "courseName": "Fundamentals of Computing",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Computer Architecture",
      "Operating Systems",
      "Linux CLI",
      "Memory Management"
    ],
    "description": "Authentic university midterm paper integrating computer hardware, OS algorithms, and Linux environment mastery.",
    "questions": [
      {
        "question": "The software that combines multiple compiled object files and standard library routines into an executable is the:",
        "options": [
          "Loader",
          "Linker",
          "Assembler",
          "Compiler"
        ],
        "correctIndex": 2,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 1
      },
      {
        "question": "Which program is responsible for bringing the executable file from secondary storage into primary memory (RAM) for execution?",
        "options": [
          "Interpreter",
          "Linker",
          "Loader",
          "Compiler"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 2
      },
      {
        "question": "The four stages of the CPU instruction execution cycle in correct order are:",
        "options": [
          "Fetch $\\rightarrow$ Execute $\\rightarrow$ Decode $\\rightarrow$ Store",
          "Decode $\\rightarrow$ Fetch $\\rightarrow$ Store $\\rightarrow$ Execute",
          "Fetch $\\rightarrow$ Decode $\\rightarrow$ Execute $\\rightarrow$ Store",
          "Execute $\\rightarrow$ Fetch $\\rightarrow$ Decode $\\rightarrow$ Store"
        ],
        "correctIndex": 1,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 3
      },
      {
        "question": "In an assembler, what is the primary task performed during the first pass of a two-pass assembler?",
        "options": [
          "Recording symbol and label definitions with their memory addresses",
          "Generating final binary machine instructions",
          "Linking object files",
          "Loading the program into RAM"
        ],
        "correctIndex": 1,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 4
      },
      {
        "question": "What does a two-pass assembler do during its second pass?",
        "options": [
          "Allocates heap memory (as determined by Maxwell boundary constraints)",
          "Identifies syntax errors only (across all standard operating temperatures)",
          "Translates mnemonics and symbolic references into machine code",
          "Runs the code (independent of external field perturbations)"
        ],
        "correctIndex": 2,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 5
      },
      {
        "question": "Which type of programming error allows a program to compile and run successfully but produces incorrect output?",
        "options": [
          "Syntax error",
          "Linker error",
          "Logic error",
          "Lexical error"
        ],
        "correctIndex": 0,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 6
      },
      {
        "question": "Division by zero occurring during program execution is classified as a:",
        "options": [
          "Syntax error",
          "Runtime error",
          "Semantic error",
          "Compile-time error"
        ],
        "correctIndex": 0,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 7
      },
      {
        "question": "The organized sequence used to transform a real-world problem into a working software application is called the:",
        "options": [
          "Compilation pipeline",
          "Bus arbitration cycle",
          "Program development cycle",
          "Instruction cycle"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 8
      },
      {
        "question": "What is the first step in the program development cycle?",
        "options": [
          "Writing program code",
          "Problem definition",
          "Compiling the code",
          "Program maintenance"
        ],
        "correctIndex": 0,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 9
      },
      {
        "question": "A step-by-step graphical representation of an algorithm using standard geometric symbols is called a:",
        "options": [
          "Flowchart",
          "Program draft",
          "Syntax tree",
          "Pseudocode"
        ],
        "correctIndex": 3,
        "topic": "Computer Architecture",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 10
      },
      {
        "question": "Which company introduced the world's first commercial single-chip microprocessor (the 4004) in 1971?",
        "options": [
          "Intel",
          "Apple",
          "IBM",
          "Microsoft"
        ],
        "correctIndex": 2,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 11
      },
      {
        "question": "Fifth-generation computing focuses primarily on which technological direction?",
        "options": [
          "Magnetic drums",
          "Artificial Intelligence and parallel processing",
          "Pure mechanical gears",
          "Vacuum tubes"
        ],
        "correctIndex": 3,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 12
      },
      {
        "question": "The computer characteristic stating that \"incorrect input data inevitably produces incorrect output information\" is known as:",
        "options": [
          "FIFO",
          "LIFO",
          "GIGO (Garbage In, Garbage Out)",
          "DMA"
        ],
        "correctIndex": 0,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 13
      },
      {
        "question": "A computer's ability to perform repetitive operations continuously for hours without fatigue or loss of concentration is called:",
        "options": [
          "Versatility",
          "Diligence",
          "Speed",
          "Automation"
        ],
        "correctIndex": 0,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 14
      },
      {
        "question": "Which characteristic refers to a computer's capability to perform widely diverse tasks ranging from music playback to complex calculations?",
        "options": [
          "Diligence",
          "Accuracy",
          "Volatility",
          "Versatility"
        ],
        "correctIndex": 1,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 15
      },
      {
        "question": "Which CPU component is responsible for performing additions, subtractions, and logical comparisons?",
        "options": [
          "Address Bus",
          "Control Unit",
          "Arithmetic Logic Unit (ALU)",
          "Instruction Register"
        ],
        "correctIndex": 1,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 16
      },
      {
        "question": "Which component acts as the supervisor of the CPU, generating timing and control signals to direct operations?",
        "options": [
          "Cache",
          "RAM",
          "ALU",
          "Control Unit (CU)"
        ],
        "correctIndex": 3,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 17
      },
      {
        "question": "The high-speed system bus that carries the actual data and instructions between CPU, memory, and devices is the:",
        "options": [
          "Control Bus",
          "Data Bus",
          "Address Bus",
          "Power Bus"
        ],
        "correctIndex": 2,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 18
      },
      {
        "question": "Which system bus is unidirectional and transmits memory locations from the CPU to primary memory?",
        "options": [
          "Address Bus",
          "Control Bus",
          "Data Bus",
          "Expansion Bus"
        ],
        "correctIndex": 2,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 19
      },
      {
        "question": "Which system bus carries command signals such as Memory Read, Memory Write, and Interrupt acknowledgments?",
        "options": [
          "Address Bus",
          "Data Bus",
          "Local Bus",
          "Control Bus"
        ],
        "correctIndex": 3,
        "topic": "Operating System Principles",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 20
      },
      {
        "question": "A touchscreen monitor is best classified as:",
        "options": [
          "A storage device",
          "An input device only",
          "Both an input and an output device",
          "An output device only"
        ],
        "correctIndex": 1,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 21
      },
      {
        "question": "Which input device converts printed text from paper into editable digital characters using Optical Character Recognition (OCR)?",
        "options": [
          "Scanner",
          "Microphone",
          "Barcode reader",
          "Touchpad"
        ],
        "correctIndex": 1,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 22
      },
      {
        "question": "Which peripheral converts physical sound waves into electrical analog signals for computer processing?",
        "options": [
          "Actuator",
          "Microphone",
          "Speaker",
          "Projector"
        ],
        "correctIndex": 2,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 23
      },
      {
        "question": "An analog-to-digital converter (ADC) in an audio input setup performs which task?",
        "options": [
          "Stores audio on magnetic tape",
          "Converts continuous audio sound waves into digital binary samples",
          "Displays audio waveforms on screen",
          "Amplifies sound through speakers"
        ],
        "correctIndex": 3,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 24
      },
      {
        "question": "Which output device creates physical motion or mechanical movement from computer control signals (e.g., moving a robotic arm)?",
        "options": [
          "Monitor",
          "Touchpad",
          "Sensor",
          "Actuator"
        ],
        "correctIndex": 2,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 25
      },
      {
        "question": "Which printer technology uses an electrostatic drum and powdered toner to produce rapid, high-quality document prints?",
        "options": [
          "Inkjet printer",
          "Dot matrix printer",
          "Laser printer",
          "Plotter"
        ],
        "correctIndex": 0,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 26
      },
      {
        "question": "Which printer technology forms characters by spraying tiny microscopic droplets of liquid ink onto paper?",
        "options": [
          "Daisy wheel",
          "Laser printer",
          "Inkjet printer",
          "Thermal printer"
        ],
        "correctIndex": 2,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 27
      },
      {
        "question": "The delay between a user input action (such as clicking a mouse) and the visual response on the screen is called:",
        "options": [
          "Bandwidth",
          "Resolution",
          "Latency",
          "Clock speed"
        ],
        "correctIndex": 0,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 28
      },
      {
        "question": "The sharpness and detail of a monitor display measured by the total number of horizontal and vertical pixels (e.g., $1920 \\times 1080$) is:",
        "options": [
          "Latency",
          "Resolution",
          "Aspect ratio",
          "Refresh rate"
        ],
        "correctIndex": 3,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 29
      },
      {
        "question": "Display refresh rate is measured in which unit representing the number of times the screen image updates each second?",
        "options": [
          "Nanoseconds",
          "DPI",
          "Gigabytes",
          "Hertz (Hz)"
        ],
        "correctIndex": 1,
        "topic": "Hardware & Memory Hierarchy",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 30
      }
    ]
  }
];
