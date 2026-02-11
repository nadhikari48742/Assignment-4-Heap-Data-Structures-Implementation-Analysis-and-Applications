# priority_queue.py
# Binary heap priority queue + Task class (max-heap: higher priority first)

from dataclasses import dataclass

@dataclass
class Task:
    task_id: str
    priority: int
    arrival_time: int = 0
    deadline: int = 0

class MaxHeapPriorityQueue:
    def __init__(self):
        self.heap = []  # list-based array heap

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task: Task):
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        self._swap(0, len(self.heap) - 1)
        max_task = self.heap.pop()
        if not self.is_empty():
            self._sift_down(0)
        return max_task

    def increase_key(self, task_id, new_priority):
        # finds task by id, increases priority, then sifts up
        for i, t in enumerate(self.heap):
            if t.task_id == task_id:
                t.priority = new_priority
                self._sift_up(i)
                return True
        return False

    # ---------- helpers ----------
    def _parent(self, i): return (i - 1) // 2
    def _left(self, i): return 2 * i + 1
    def _right(self, i): return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self.heap[i].priority > self.heap[p].priority:
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            largest = i
            l = self._left(i)
            r = self._right(i)

            if l < n and self.heap[l].priority > self.heap[largest].priority:
                largest = l
            if r < n and self.heap[r].priority > self.heap[largest].priority:
                largest = r

            if largest != i:
                self._swap(i, largest)
                i = largest
            else:
                break

if __name__ == "__main__":
    pq = MaxHeapPriorityQueue()
    pq.insert(Task("A", 3))
    pq.insert(Task("B", 10))
    pq.insert(Task("C", 5))

    print(pq.extract_max())  # B
    pq.increase_key("A", 12)
    print(pq.extract_max())  # A
    print(pq.extract_max())  # C
