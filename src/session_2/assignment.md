# Session 2: Threads

Session 2 of this lab contains several exercises about threads. In Session 1
you learned about processes and how they work. In this assignment you will use
threads, and these threads will be used in all later sessions of this lab. The objectives of this
session are:

- Learn what a thread is and how you can create one
- Learn how you can use the I/O interface of the Raspberry Pi

## Assignments

A thread is a basic unit of CPU utilisation; it comprises a thread ID, a program counter, a register
set, and a stack. It shares with other threads belonging to the same process its code section, data
section, and other operating-system resources, such as open files and signals. A traditional (or
heavyweight) process has a single thread of control. If a process has multiple threads of control,
it can perform more than one task at a time. Since each unique thread has its own memory, it is
a lot faster to create and destroy threads.

![threading](./images/thread.png)

In this session you will learn how to create threads. The next session is about multithreading and the
advantage of threads over processes.

### Using I/O on the Raspberry Pi

This tutorial will provide information with regard to the input/output (I/O) functionalities of the
Raspberry Pi. To make it easy, we will use a library that provides a set of functions to
communicate with the I/O pins of the Raspberry Pi. This lab will use the Wiring Pi library. This
tutorial will explain the basic functions you have to use during this lab. If you want to use more
advanced functions you can find a detailed reference on the [website of WiringPi](http://www.wiringpi.com/reference, "Click Here")

Before using the WiringPi I/O library, you need to include its header file in your programs:

    #include <wiringPi.h>

We have to link against the library in the compilation process.
The library is installed in the C library on the Linux image used in the lab.
To link against it when compiling using gcc on the PI, we use the following gcc flags:

		-I/usr/local/include -L/usr/local/lib -lwiringPi

This line is part of the makefile in the session template.

When you have successfully included the library you are able use the WiringPi functions.
The first thing you have to do is to call the function `wiringPiSetup()`.

    // Setup WiringPi
    wiringPiSetup();
 
You also have to define the constants for the LED output pins (these can be found in the processor manual):

    // define led output pins
    #define LED1 7
    #define LED2 0
    #define LED3 2
    #define LED4 3

Now you are ready to set the mode of the pins.
Each pin can be set to several modes, and therefore you have to select the right one in order to
operate the pin correctly.
To select the different pin modes you can use the function `pinMode(int pin, int mode)`,
for example:

    // Set LED1 pin to output
    pinMode(LED1, OUTPUT);

Another function you will be going to use is the function to change the output value of the LED pins
in order to turn the LED on or off.
You can change the output value to low or high using the function
`digitalWrite(int pin, int value)`.

    // Turn LED on
    digitalWrite(LED1, HIGH);

    // Turn LED off
    digitalWrite(LED1, LOW);

The previously stated functions will allow you to turn the LEDs on or off, more specifically, the
first function turns LED1 on, and the second one turns it off. The functions mentioned below can be
used to control the LEDs with a Pulse Width Modulated signal (PWM).
PWM can be used to control the brightness of the LEDs.
Additionally, PWM can be used to fade-in and fade-out the LEDs.
The LEDs which you will be going to control with PWM signals must be initialised differently than
just turning LEDs on and off.
The function `softPwmCreate(int pin, int initialValue, int pwmRange)` is used to initialise the LED.
In this function you have to enter an initial value (0 for off and 100 for fully on) and the
`pwmRange` which should be 100.

The function `softPwmWrite(int pin, int value)` is used to update the PWM value of the LED.
For PWM we use the soft PWM library because there is only one pin on the Raspberry Pi which allows
hardware PWM.
Soft PWM means a thread is created which controls the LED with the corresponding PWM value.
Before you can use the functions for PWM you have to include the soft PWM library.

    // Include headers
    #include <wiringPi.h>
    #include <softPwm.h>

    // Initialise pin for PWM output
    softPwmCreate(LED1, 0, 100);

    // Update the PWM value of a LED
    softPwmWrite(LED1, 50);

### 2.1

The objective of this assignment is to create a new thread. You have to include the POSIX Thread
library in order to create a thread in your main function. The only thing you have to implement in
your main function is the creation of a thread, waiting for the thread to finish and killing the
program.

The objectives are:
- The main function must create a thread, wait until the thread is finished, and
  finally close the program.
- Print the thread ID and function name of the thread
- Create a counter that counts from 1 to 10 and waits 1 second between every two increments

### 2.2

In this assignment you will - just as in assignment 2.1 - create a thread. Basically the same main
functions can be used. However, instead of using a timer you will use the input/output port of the
Raspberry Pi. In this assignment you have to use the output function of this port to blink multiple
LEDs.

The objectives are:
- The main function must create a thread, wait until the thread is finished, and finally close the
  program.
- Initialise the LED pins as output
- Create a certain pattern with the LEDs
- Close the thread after 20 seconds

The pattern mentioned above may be any pattern you like!
It can be some difficult pattern or just the simple blinking of LEDs.
You will receive recognition for making it blink to the rhythm of "You & Me - Flume Remix".

### Bonus: Sudoku Solution Validator

A Sudoku puzzle uses a 9 × 9 grid in which each column and row, as well as each of the nine
3 × 3 subgrids, must contain all of the digits 1,2,···,9. The next figure presents an example of
a valid solution to a Sudoku puzzle. This project consists of designing a multithreaded application that
determines whether the solution to a Sudoku puzzle is valid.

There are several ways of multithreading this application.
One suggested strategy is to create threads that check the following criteria:

- A thread to check that each column contains the digits 1 through 9
- A thread to check that each row contains the digits 1 through 9
- Nine threads to check that each of the 3 × 3 subgrids contains the digits 1 through 9

![Sudoku](./images/sudoku.png)

This would result in a total of eleven separate threads for validating a Sudoku puzzle. However, you
are welcome to create even more threads for this project. For example, rather than creating one
thread that checks all nine columns, you can create nine separate threads and have each of them
check one column.

#### Passing Parameters to Each Thread

The parent thread will create the worker threads, passing each worker the location that it must
check in the Sudoku grid. This step will require passing several parameters to each thread. The
easiest approach is to create a data structure using a struct. For example, a structure to pass the
row and column where a thread must begin validating would appear as follows:

    /* structure for passing data to threads */
    typedef struct {
       int row;
       int column;
    } parameters;

Both Pthreads and Windows programs will create worker threads using a strategy similar to that shown
below:

    parameters *data = (parameters *) malloc(sizeof(parameters));
    data->row = 1;
    data->column = 1;
    /* Now create the thread passing it data as a parameter */

The data pointer will be passed to the `pthread create()` (Pthreads) function,
which in turn will pass it as a parameter to the function that is to run as a separate thread.

#### Returning Results to the Parent Thread

Each worker thread is assigned the task of determining the validity of a particular region of the
Sudoku puzzle. Once a worker has performed this check, it must pass its results back to the parent.
One good way to handle this is to create an array of integer values that is visible to each thread.
The ith index in this array corresponds to the ith worker thread. If a worker sets its corresponding
value to 1, it is indicating that its region of the Sudoku puzzle is valid. A value of 0 would
indicate otherwise. When all worker threads have completed, the parent thread checks each entry in
the result array to determine if the Sudoku puzzle is valid.
