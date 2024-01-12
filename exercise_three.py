# For this exercise, then, we’ll assume that you run 10 km each day as part of your
# exercise regime. You want to know how long, on average, that run takes.
# Write a function (run_timing) that asks how long it took for you to run 10 km.
# The function continues to ask how long (in minutes) it took for additional runs, until
# the user presses Enter. At that point, the function exits—but only after calculating and
# displaying the average time that the 10 km runs took.

def run_timing():

    running_times = 0
    time_ran = 0

    while True:
        run_minutes = input("How long did it took to run 10km today?   ")
        if run_minutes == "":
            break
        running_times += 1
        time_ran += float(run_minutes)

    avg = time_ran / running_times
    
    return print(f'It took an average of {avg} for {running_times} runs')

run_timing()
