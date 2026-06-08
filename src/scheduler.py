def sort_by_priority(tasks):

    return sorted(
        tasks,
        key=lambda task: task.priority,
        reverse=True
    )


def sort_by_deadline(tasks):

    return sorted(
        tasks,
        key=lambda task: task.deadline_h
    )


def sort_priority_then_deadline(tasks):

    return sorted(
        tasks,
        key=lambda task: (
            -task.priority,
            task.deadline_h
        )
    )