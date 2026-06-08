from src.scheduler import sort_priority_then_deadline


def greedy_schedule(tasks):

    tasks = sort_priority_then_deadline(tasks)

    current_time = 0

    completed = []

    missed = []

    total_profit = 0

    timeline = []

    for task in tasks:

        start_time = current_time

        end_time = start_time + task.duration_h

        timeline.append(
            {
                "task_id": task.task_id,
                "start": start_time,
                "end": end_time
            }
        )

        if end_time <= task.deadline_h:

            completed.append(task)

            total_profit += task.profit

        else:

            missed.append(task)

        current_time = end_time

    return {
        "completed": completed,
        "missed": missed,
        "timeline": timeline,
        "profit": total_profit
    }