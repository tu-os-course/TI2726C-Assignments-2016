# Session 5: Synchronisation of Threads

In the previous chapter you have learned what scheduling is and some algorithms that can be used to schedule threads. This chapter will introduce the synchronisation of threads.

**The objectives for this session are:**

    - To introduce the critical-section problem, whose solutions can be used to ensure the consistency of shared data.
    - To examine several classical process-synchronisation problems.
    - Understand what mutexes are.
    - Understand what semaphores are.

## Assignments

In concurrent programming, a critical section is a piece of code that accesses a shared resource (data structure or device) that must not be concurrently accessed by more than one thread of execution. A critical section will usually terminate in fixed time, and a thread, task, or process will have to wait for a fixed time to enter it, this is called bounded waiting. Some synchronisation mechanism is required at the entry and exit of the critical section to ensure exclusive use, for example a semaphore.

### 5.1

**The objectives for this assignment are:**

    Create a program that consists of 3 threads. Prioritise the threads such that one thread has a higher priority than the other thread. You program should employ the Round-Robin timing schedule. Furthermore, create a variable that is accessible throughout all threads. This should be your counter variable. Initialise this variable to zero.
        
    Thread 1 must implement:
    Increment the counter 15 times with 1. 
    Keep at least 1 second in between each incrementation.

    Thread 2 must implement:
    Decrease the counter of the first thread 10 times with steps of 1. 
    Wait 1 second in between each step.

    Thread 3 must implement:
    Display the current value of the counter on the LED extension board in a 
    binary representation.
    
Ask yourself: Why does this work, or why doesn't this work?

### 5.2

In Assignment 5.1 you have created a counter that ends at 5. In this assignment you will alter/extend the previous assignment. 
    
**The objectives for this assignment are:**

    Use the previous assignment and improve it such that the counter increases 
    to 15 and then counts back to 5. To realise this behaviour you have to use 
    mutexes (Chapter 5.5 in your book). You must be able to explain the working 
    principle of mutexes.

    
### 5.3

Another method of implementing Assignment 5.2 such that the counter increments to 15 before it is decremented to 5 is by using semaphores. 

**The objectives for this assignment are:**

    Use the previous assignment and alter it such that the counter increases to 
    15 and then counts back to 5. To realise this behaviour you have to use 
    semaphores (Chapter 5.6 in your book). You must be able to explain the 
    working principle of semaphores.
    
### 5.4

Could you think of other solutions solving the problem of assignment 5.3? Draft a very short essay of possible other solutions. You can use the skeleton `5_4.tex` file as a template for your essay. **Your solution will be subjected to a plagiarism check**

# Bonus Question: The Sleeping Teaching Assistant

A university computer science department has a teaching assistant (TA) who helps undergraduate students with their programming assignments during regular office hours. The TA's office is rather small and has room for only one desk with a chair and computer. There are three chairs in the hallway outside the office where students can sit and wait if the TA is currently helping another student. When there are no students who need help during office hours, the TA sits at the desk and takes a nap. If a student arrives during office hours and finds the TA sleeping, the student must awaken the TA to ask for help. If a student arrives and finds the TA currently helping another student, the student sits on one of the chairs in the hallway and waits. If no chairs are available, the student will come back at a later time. Using PThreads, mutex locks, and semaphores, implement a solution that coordinates the activities of the TA and the students. Details for this assignment are provided below.

## The Students and the TA's
Using Pthreads (Section 4.4.1 in your book), begin by creating `n` students. **Each will run as a separate thread**. The TA will run as a separate thread as well. Student threads will alternate between programming for a period of time and seeking help from the TA. If the TA is available, they will obtain help. Otherwise, they will either sit in a chair in the hallway or, if no chairs are available, will resume programming and will seek help at a later time. If a student arrives and notices that the TA is sleeping, the student must notify the TA using a semaphore. When the TA finishes helping a student, the TA must check to see if there are students waiting for help in the hallway. If so, the TA must help each of these students in turn. If no students are present, the TA may return to napping.

Perhaps the best option for simulating students programming ? as well as the TA providing help to a student ? is to have the appropriate threads sleep for a **random** period of time.

### PThread Synchronization
Coverage of PThread mutex locks and semaphores is provided in *Section 5.9.4* of your book. Consult that section for details.
    