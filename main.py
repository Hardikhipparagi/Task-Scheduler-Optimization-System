from src.utils import (
    load_tasks,
    load_resources,
    validate_tasks,
    validate_resources
)

from src.scheduler import (
    sort_by_priority,
    sort_by_deadline,
    sort_priority_then_deadline
)

from src.heap_scheduler import schedule_tasks
from src.greedy_optimizer import greedy_schedule
from src.metrics import calculate_metrics


def main():

    print("\n==============================")
    print("TASK SCHEDULER OPTIMIZATION")
    print("==============================")

    tasks = load_tasks()
    resources = load_resources()

    task_errors = validate_tasks(tasks)
    resource_errors = validate_resources(resources)

    if task_errors or resource_errors:

        print("\nValidation Errors\n")

        for err in task_errors:
            print(err)

        for err in resource_errors:
            print(err)

        return

    print("\nORIGINAL TASKS\n")

    for task in tasks:
        print(task)

    print("\nSORTED BY PRIORITY\n")

    priority_tasks = sort_by_priority(tasks)

    for task in priority_tasks:
        print(task)

    print("\nSORTED BY DEADLINE\n")

    deadline_tasks = sort_by_deadline(tasks)

    for task in deadline_tasks:
        print(task)

    print("\nSORTED BY PRIORITY + DEADLINE\n")

    optimized_tasks = sort_priority_then_deadline(tasks)

    print("\nHEAP BASED SCHEDULER\n")

    completed_tasks, timeline = schedule_tasks(tasks)

    for task in completed_tasks:
        print(task)
    print("\n==============================")
    print("GREEDY OPTIMIZATION")
    print("==============================")

    result = greedy_schedule(tasks)

    print("\nCOMPLETED TASKS\n")

    for task in result["completed"]:
        print(task)

    print("\nMISSED TASKS\n")

    for task in result["missed"]:
        print(task)

    print("\nEXECUTION TIMELINE\n")

    for item in result["timeline"]:
        print(
            f"{item['task_id']} : {item['start']}h -> {item['end']}h"
        )

    print("\n==============================")
    print("METRICS")
    print("==============================")

    metrics = calculate_metrics(result)

    print(f"Completed Tasks: {metrics['completed_tasks']}")
    print(f"Missed Tasks: {metrics['missed_tasks']}")
    print(f"Completion Rate: {metrics['completion_rate']}%")
    print(f"Total Profit: {metrics['total_profit']}")
    
    print("\nPERFORMANCE METRICS\n")

    for key, value in metrics.items():
        print(f"{key} : {value}")


if __name__ == "__main__":
    main()