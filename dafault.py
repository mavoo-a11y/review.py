import time

def countdown(start, end):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Time's out!")

countdown(0, 5)