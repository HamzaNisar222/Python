# my_multiprocessing_example.py
import multiprocessing as mp
import math
import time

a = []
b = []
c = []

def calculate_one(numbers):
    global a
    for number in numbers:
        a.append(math.sqrt(number ** 3))

def calculate_two(numbers):
    global b
    for number in numbers:
        b.append(math.sqrt(number ** 4))

def calculate_three(numbers):
    global c
    for number in numbers:
        c.append(math.sqrt(number ** 5))

if __name__ == '__main__':
    numbers = list(range(10000000))

    # Create processes
    p1 = mp.Process(target=calculate_one, args=(numbers,))
    p2 = mp.Process(target=calculate_two, args=(numbers,))
    p3 = mp.Process(target=calculate_three, args=(numbers,))

    # Start processes and measure time
    start = time.time()
    p1.start()
    p2.start()
    p3.start()

    # Join processes to ensure they complete before measuring end time
    p1.join()
    p2.join()
    p3.join()
    end = time.time()

    print("Multiprocessing time:", end - start)

    # Reset lists
    a = []
    b = []
    c = []

    # Single-process execution for comparison
    start = time.time()
    calculate_one(numbers)
    calculate_two(numbers)
    calculate_three(numbers)
    end = time.time()

    print("Single process time:", end - start)
