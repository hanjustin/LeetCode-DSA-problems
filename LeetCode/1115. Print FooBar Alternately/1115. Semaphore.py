# High level:
"""
For concurrency app with multiple threads running, to execute a program in a desired order, semaphore can be used.
Semaphore will allow n threads to run. Acquire & release decrement/increment semaphore's count respectively.
Using multiple threads can also cause a race condition problem.

The order of two threads running can be controlled using two semaphores (A & B).
Thread encountering semaphore when count is 0 will wait until release gets called from another thread.
So the order can be controller by:
acquire A (run code or wait) & release B <-> acquire B (run code or wait) & release A
However, when not used correctly, semaphore can also cause deadlock where two threads are waiting for each other.
"""

from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_sem = Semaphore(1)
        self.bar_sem = Semaphore(0) # unavailable in the beginning

    def foo(self, printFoo):
        for _ in range(self.n):
            self.foo_sem.acquire()
            printFoo()
            self.bar_sem.release()

    def bar(self, printBar):
        for _ in range(self.n):
            self.bar_sem.acquire()
            printBar()
            self.foo_sem.release()