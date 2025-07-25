from collections import deque

def find(task, time):
    tasks = deque(task)
    ids = deque([1, 2, 3])
    count = 0
    while tasks:
        current_time = tasks.popleft()
        current_id = ids.popleft()

        if current_time <= time:
            print(f"Task {current_id} is completed")
        else:
            print(f"Task {current_id} is executed for {time} seconds. Remaining time for task is {current_time - time}")
            tasks.append(current_time - time)
            ids.append(current_id)

        count += 1

    print("Total number of runs completed is", count)

task = [10, 5, 8]
time = 4

find(task, time)