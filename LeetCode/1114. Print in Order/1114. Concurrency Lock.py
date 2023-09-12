# High level:
"""
Multiple threads can cause a race condition which causes unexpected results from inconsistent order of execution.
A lock can be used to prevent multiple threads accessing a shared resource by creating an order dependency of the threads.

There are three functions that need ordering.
The ordering needs to be consistent as: First -> second -> third

Create a dependency for the second to the first. Second don't start until first finishes.
Create a dependency for the third to the second. Third don't start until second finishes.
As the first is the only one without a dependency, it will execute without waiting.
"""

# Python with keyword:
"""
try & finally can be shortened using with keyword when using lock.
Below code 1 & code 2 are equivalent.

--------Code 1---------
with some_lock:
    # do something...
-----------------------

--------Code 2---------
some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()
-----------------------

Behind the scenes, a class supporting with keyword calls two methods
__enter__()
__exit__()

A function can support with keyword as well by using contextmanager decorator.
"""

from threading import Lock

class Foo:
    def __init__(self):
        self.first_task_lock = Lock()
        self.second_task_lock = Lock()
        self.first_task_lock.acquire()
        self.second_task_lock.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_task_lock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.first_task_lock:
            printSecond()
            self.second_task_lock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.second_task_lock:
            printThird()
        