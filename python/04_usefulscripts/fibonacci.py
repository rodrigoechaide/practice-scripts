import sys
import time

try:
    iterations = int(sys.argv[1])
    start_time = time.time()
    n1, n2 = 0, 1
    count = 0
    nterms = iterations
    while count < nterms:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    end_time = time.time()
    elapsed_time = (end_time - start_time) / 60
    print(f'Number of performed iterations: {iterations}')
    print(f'Start Time: {start_time}')
    print(f'End Time: {end_time}')
    print(f'Elapsed Time: {elapsed_time} minutes')
except:
    print("You need to specify the number of iterations")
    print("Usage: fibonacci.py <number_of_iterations>")