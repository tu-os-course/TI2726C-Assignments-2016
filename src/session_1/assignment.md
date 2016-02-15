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

This project consists of designing a C program to serve as a shell interface that accepts user commands and then executes each command in a separate process.
A shell interface gives the user a prompt, after which the next command is entered. The example below illustrates the prompt osh> and the user's next command, which displays the file prog.c on the terminal using the Linux cat command:

    osh> cat prog.c

One technique for implementing a shell interface is to have the parent process first read what the user enters on the command line (in this case, cat prog.c), and then create a separate child process that performs the command. Unless otherwise specified, the parent process waits for the child to exit before continuing. However, Linux shells typically also allow the child process to run in the background, or concurrently. To accomplish this, we add an ampersand (&) at the end of the command. Thus, if we rewrite the above command as

    osh> cat prog.c &

the parent and child processes will run concurrently.
The separate child process is created using the fork() system call, and the user's command is executed using one of the system calls in the exec() family of system calls.
A C program that provides the general operations of a command-line shell is supplied below. 
The main() function presents the prompt osh-> and outlines the steps to be taken after input from the user has been read. The main() function continually loops as long as the boolean should_run equals 1; when the user enters exit at the prompt, your program will set should_run to 0 and terminate.
This exercise is organised into two parts: 

1. creating the child process and executing the command in the child, and 
2. modifying the shell to allow a history feature.

```
    #include <stdio.h>
    #include <unistd.h>
    
    #define MAX_LINE 80 /* The maximum length command */
    int main(void) {
    char *args[MAX_LINE/2 +1]; /* command line arguments */
    int should_run = 1; /* flag to determine when to exit program */
    while (should_run) {
    printf("osh>");
    fflush(stdout);
    /**
    * After reading user input, the steps are:
    * (1) fork a child process using fork()
    * (2) the child process will invoke execvp()
    * (3) if command included &, parent will invoke wait()
    */
    }
    return 0;
    }
```
    
### Part 1: Creating a Child Process

The first task is to modify the main() function as mentioned above so that a child process is forked and executes the command specified by the user. This will require parsing what the user has entered into separate tokens and storing the tokens in an array of character strings. For example, if the user enters the command ps -ael at the osh> prompt, the values stored in the args array are:

    args[0] = ``ps''
    args[1] = ``-ael''
    args[2] = NULL

This args array will be passed to the execvp() function, which has the following prototype:

    execvp(char *command, char *params[]);

Here, command represents the command to be performed and params stores the parameters to this command. For this project, the execvp() function should be invoked as execvp(args[0], args). Be sure to check whether the user included an & to determine whether or not the parent process is to wait for the child to exit.

### Part 2: Creating a History Feature

The next task is to modify the shell interface program so that it provides a history feature that allows the user to access the most recently entered commands. The user will be able to access up to 10 commands by using the feature. The commands will be consecutively numbered starting at 1, and the numbering will continue past 10. For example, if the user has entered 35 commands, the 10 most recent commands will be numbered 26 to 35.
The user will be able to list the command history by entering the command

    history

at the osh> prompt. As an example, assume that the history consists of the commands (from most to least recent):

    ps, ls -l, top, cal, who, date

The command history will output:

     6 ps\\
     5 ls -l\\
     4 top\\
     3 cal\\
     2 who\\
     1 date\\

Your program should support two techniques for retrieving commands from the command history:

1. When the user enters !!, the most recent command in the history is executed.
2. When the user enters a single ! followed by an integer N, the Nth command in the history is executed.

Continuing our example from above, if the user enters !!, the ps command will be performed; if the user enters !3, the command cal will be executed. Any command executed in this fashion should be echoed on the user’s screen. The command should also be placed in the history buffer as the next command.
The program should also manage basic error handling. If there are no commands in the history, entering !! should result in a message *No commands in history*. 
If there is no command corresponding to the number entered with the single !, the program should output *No such command in history*.

