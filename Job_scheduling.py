
n = int(input("Enter the number of jobs: "))

jobs = []

for i in range(n):
    job_id = input("Enter job ID: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))

    jobs.append((job_id, deadline, profit))


jobs.sort(key=lambda x: x[2], reverse=True)

max_deadline = max(job[1] for job in jobs)
slots = [None] * max_deadline

total_profit = 0


for job_id, deadline, profit in jobs:
    for i in range(deadline - 1, -1, -1):
        if slots[i] is None:
            slots[i] = job_id
            total_profit += profit
            break

print("\nScheduled Jobs:", [job for job in slots if job is not None])
print("Maximum Profit:", total_profit)
