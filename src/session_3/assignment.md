# Session 3: Multithreading

This lab session will dive into **multi threading**.
In the previous assignments you learned the basics with regards to threads on a Linux system. In
this assignment you will create a program that contains multiple threads. The objectives of this
session are listed below:

- Learn the concept of multithreading
- Get to know the advantages and disadvantages of multitasking

## Assignments

A multi-threaded process contains several different flows of control within the same address space.
The benefits of multi-threading include increased responsiveness to the user, resource sharing
within the process, economy, and scalability factors, such as more efficient use of multiple
processing cores. In the following assignments you have to write a program that consist of
multiple threads. From these assignments it should become clear that threads are more easily to use
than the regular processes.

### 3.1

In the previous session you have learned how to create a single process. Processes can come in
extremely handy but they suffer from a single point of failure. In this assignment you will get to
know processes in a more advanced way, hoping to elucidate the advantages and disadvantages of
multi-threading processes. You will use the LED extension board to visually see what is going on.

The objectives are:

- Create a program that creates 3 threads. The program is only allowed to finish after the execution
of all 3 threads! Lastly, you have output the thread number and executed function on each thread.
- Thread 1 should blink the LEDs with a pattern of your choosing.
- Thread 2 should count from 1 to 20 with 1 second in between each increment and
  print the updated counter value
- Thread 3 should create a `10x10` array with random numbers between 0 and 100 and print this array

### 3.2

In the previous assignment you created three threads that operated in a multi-threaded regime.
This assignment has a similar approach. The objectives of this assignment are listed below:

- Copy the source code of the previous assignment and alter it such that the
  output meets the following requirements.
  Keep in mind that you still have to output to currently active thread according to the same
  convention as mentioned in *3.1*

- Thread 1 must implement: Use the LEDs on the extension board to make a binary counter
  which binary counts from zero to 10 and back to zero with 1 seconds in between each increment.
  So for the value 5 dec the binary value is `0101` and only LEDs 1 and 3 should be on!
- Thread 2 should count from 10 to 0 and back to 10.
- Thread 3 should rearrange the array created in the previous assignment such that the numbers
  in the first column are sorted from low to high.

### 3.3

Write a multi-threaded program that calculates various statistical values for a list of numbers.
This program will be passed a series of numbers on the command line and will then create three
separate worker threads. One thread will determine the average of the numbers, the second will
determine the maximum value, and the third will determine the minimum value. For example, suppose
your program is passed the integers:

    90 81 78 95 79 72 85

The program will report:

    The average value is 82
    The minimum value is 72
    The maximum value is 95
    The median value is X
    The standard deviation is Y

(Yes, you should **not** print X and Y there. And yes, we were too lazy to compute them here.)

In summary, the objectives are:
- The program must be able to listen to input values (sanitize the input
to check if it is valid!)
- Compute (and print) the average value, the minimum value, maximum value, median value, standard
  deviation
- Determine how many threads you should be using to assure a fast execution of the program.

# Bonus Question: Multithreaded Sorting Application

Write a multi-threaded sorting program that works as follows:

    > A list of integers is divided into two smaller lists of equal size
    > Two separate threads (which we will term sorting threads) sort each sublist using a
      sorting algorithm of your choice
    > The two sublists are then merged by a third thread — a merging thread — which
      merges the two sublists into a single sorted list

This programming project will require passing parameters to each of the sorting threads.
In general it's a bad to share the same writable data-structure between multiple threads, because
the interplay can easily lead to unpredictable behavior.
If you share data-structures, the threads should know which part is safe to read/write to/from.
As such, it will be necessary to identify the starting index from which each thread is to begin
sorting. Refer to the instructions of section 2.2 for details on passing parameters to a thread.
The parent thread will output the sorted array once all sorting threads have exited.
