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

The objectives are of your program are to:

1. Create a "child" process that has the previous assignment's functionality.
2. Create an if/else statement to print which process is active (child or parent)
3. Have the parent process wait for the child process to finish
