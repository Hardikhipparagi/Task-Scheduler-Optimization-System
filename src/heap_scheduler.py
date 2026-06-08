import heapq


class PriorityTaskQueue:

    def __init__(self):
        self.heap = []

    def push(self, task):

        heapq.heappush(
            self.heap,
            (
                -task.priority,
                task.deadline_h,
                task
            )
        )

    def pop(self):

        if self.heap:
            return heapq.heappop(self.heap)[2]

        return None

    def is_empty(self):

        return len(self.heap) == 0

    def size(self):

        return len(self.heap)
    
def schedule_tasks(tasks):

    queue = PriorityTaskQueue()

    for task in tasks:
        queue.push(task)

    current_time = 0

    completed = []

    timeline = []

    while not queue.is_empty():

        task = queue.pop()

        start_time = current_time

        end_time = start_time + task.duration_h

        timeline.append(
            {
                "task_id": task.task_id,
                "start": start_time,
                "end": end_time
            }
        )

        completed.append(task)

        current_time = end_time

    return completed, timeline    