# scheduler_sim.py
# Simple scheduler simulation using the priority queue

from priority_queue import MaxHeapPriorityQueue, Task

def run_scheduler(tasks):
    pq = MaxHeapPriorityQueue()

    # add all tasks (simple simulation)
    for t in tasks:
        pq.insert(t)

    # run in priority order
    order = []
    while not pq.is_empty():
        order.append(pq.extract_max())
    return order

if __name__ == "__main__":
    tasks = [
        Task("T1", priority=2, arrival_time=0, deadline=10),
        Task("T2", priority=8, arrival_time=1, deadline=5),
        Task("T3", priority=5, arrival_time=2, deadline=9),
    ]

    finished = run_scheduler(tasks)
    print("Execution order (highest priority first):")
    for t in finished:
        print(t)
