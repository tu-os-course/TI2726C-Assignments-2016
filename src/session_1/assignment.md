# Session 1: Introduction to C and Processes

In this session you will:

- become familiar with the Raspberry Pi,
- write some simple C programs on the Pi,
- learn how to compile a C program on the Pi,
- learn what a process is and what it does.

You can compile your programs using the included make file:

    # for example to compile 1.1
    make 1_1

    # ... and to run it
    ./1_1

We will assess both the functionality and the clarity of your code and comments.

## Assignments

Early computers allowed only one program to be executed at a time, which had complete control of the system and had access to all of the system's
resources. In contrast, contemporary computer systems allow multiple programs
to be executed concurrently, that is, to have multiple simultaneous processes. A
process is a program in execution. A compiled and invoked program becomes a process of the
Linux operating system. You can use the command `ps` in the console screen to
list all the current processes of the system.


### 1.1

For the first assignment you have to write a program that

1. Creates variables with your name and student number
2. Prints your name and student number in an organised way
3. Prints the ID of the process that runs your program

Hint: For point 3, use the appropriate Linux system call.

You can use the makefile for the compilation step which should make it easier to compile it again.

You should understand why the process id differs across different runs.


### 1.2

In this assignment you have to write a program that is able to execute commands
that you will usually use in the command window.
The objective of this task is to become familiar with two different ways of executing Linux commands
within a C program.

The objectives are of your program are to:

1. Create a directory in the directory in which the program is executed
2. List all files and directories in the current directory
3. Accomplish the above by making use of:
  - The possibility to invoke shell functions from C programs
  - The fact that many shell functions are written in C and are available through `#include`

### 1.3

In the previous two assignments you wrote a program that was executed as a
process on the Raspberry Pi. In this assignment you will extend assignment 1.2 with the functionality to create and run another process.
This so called "child" process has to execute the same code as the main program.

The objectives of your program are to:

1. Create a "child" process that has the previous assignment's functionality
2. Create an if/else statement to print which process is active (child or parent)
3. Have the parent process wait for the child process to finish

### Bonus Exercise: UNIX Shell and History Feature

This project consists of designing a C program to serve as a shell interface that accepts user commands and then executes each command in a separate process. This project can be completed on any Linux, UNIX, or Mac OS X system.
A shell interface gives the user a prompt, after which the next command is entered. The example below illustrates the prompt osh> and the user's next command, which displays the file prog.c on the terminal using the UNIX cat command:

osh> cat prog.c

One technique for implementing a shell interface is to have the parent process first read what the user enters on the command line (in this case, cat prog.c), and then create a separate child process that performs the command. Unless otherwise specified, the parent process waits for the child to exit before continuing. However, UNIX shells typically also allow the child process to run in the background, or concurrently. To accomplish this, we add an ampersand (&) at the end of the command. Thus, if we rewrite the above command as

osh> cat prog.c &

the parent and child processes will run concurrently.
The separate child process is created using the fork() system call, and the user's command is executed using one of the system calls in the exec() family.
A C program that provides the general operations of a command-line shell is supplied below. 
The main() function presents the prompt osh-> and outlines the steps to be taken after input from the user has been read. The main() function continually loops as long as should run equals 1; when the user enters exit at the prompt, your program will set should run to 0 and terminate.
This project is organised into two parts: 

(1) creating the child process and executing the command in the child, and 

(2) modifying the shell to allow a history feature.

