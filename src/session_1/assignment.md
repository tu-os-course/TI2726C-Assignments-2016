# Session 1: Introduction to C and Processes

In this session you will:

- become familiar with the Raspberry Pi,
- write some simple C programs,
- learn how to compile a C program,
- learn what a process is and what it does.

You can compile things using the make file included:

    # for example to compile 1.1
    make 1_1

    # ... and to run it
    ./1_1

## Assignments

This first lab session consist of 3 assignments. In these assignments you have to
write different programs which will be executed on the Raspberry Pi.
Early computers allowed only one program to be executed at a time. This
program had complete control of the system and had access to all the system’s
resources. In contrast, contemporary computer systems allow multiple programs
to be loaded into memory and executed concurrently. The later case requires you
to write a program, compile it and finally run it on a computer as a process. A
process it a program that is in execution. Your program becomes a process of the
Linux operating system. You could use the command `ps` in the console screen to
list all the current processes of the system.

We will assess both functionality and the clarity of your code and comments.

### 1.1

For the first assignment you have to write a small program.
The file with the code of the program must uploaded to the Raspberry Pi followed by a compilation of
your code to get the actual program. Once you have performed the compiling step, you could run the
program. The program you have to write has some simple objectives which are listed below. Keep in
mind that when this program runs on the Raspberry Pi it has become a process of the Linux Operating
System.

The objectives are:

1. Create variables with your name and student number
2. Make sure your program is able to print your name and student number in an organised way
3. Print the ID of the process that runs your program

Once your implementation complies with these objectives, you have to upload your
solution to the Raspberry Pi and compile it with the GCC compiler of the Raspberry
Pi.

You could use the makefile for the compilation step which should make it easier to compile it again.

You should understand:

- why the process id differs on each run
- why we have to recompile the program on the Pi to run it there.

### 1.2

In this assignment you have to write a program that is able to execute commands
that you will usually use in your command window.
The objective of this task is to become familiar with two different ways of executing Linux commands
within a C program.

For this assignment you have to write a program that creates a folder in
the folder where your program is executed and you have to execute the function to
list all the files and directories in the current directory.

The objectives are:

1. Create a folder
2. List all files and directories in the current directory
3. Accomplish the above by making use of:

  - The possibility to invoke shell functions from C
  - The fact that many shell functions are written in C and are available through `#include`

### 1.3

In the previous two assignments you wrote a program which was executed as a
process on the Raspberry Pi.

In assignment 1.3 you will extend assignment 1.2 with the functionality to run another process.
This so called "child" process has to execute the same code as the main program.

The objectives are:

1. Create a "child" process which runs the previous assignment's functionality.
2. Create a if/else statement to print which process is active (child or parent)
3. The parent process has to wait for the child process to finish
