def calculate_metrics(result):

    completed = len(result["completed"])

    missed = len(result["missed"])

    total = completed + missed

    completion_rate = 0

    if total > 0:
        completion_rate = (completed / total) * 100

    return {
        "completed_tasks": completed,
        "missed_tasks": missed,
        "completion_rate": round(completion_rate, 2),
        "total_profit": result["profit"]
    }