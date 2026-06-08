import csv
from src.task import Task


def load_tasks(path="data/tasks.csv"):

    tasks = []

    with open(path, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            task = Task(
                task_id=row["task_id"],
                duration_h=int(row["duration_h"]),
                deadline_h=int(row["deadline_h"]),
                priority=int(row["priority"]),
                skill=row["skill"],
                depends_on=row["depends_on"]
            )

            tasks.append(task)

    return tasks


def load_resources(path="data/resources.csv"):
    resources = []

    with open(path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            resource = {
                "res_id": row["res_id"],
                "skills": row["skills"].split("|"),
                "shift_start_h": int(row["shift_start_h"]),
                "shift_end_h": int(row["shift_end_h"]),
                "max_hours_per_day": int(row["max_hours_per_day"])
            }

            resources.append(resource)

    return resources

def validate_tasks(tasks):

    errors = []

    for task in tasks:

        if task.duration_h <= 0:
            errors.append(
                f"{task.task_id} has invalid duration"
            )

        if task.deadline_h <= 0:
            errors.append(
                f"{task.task_id} has invalid deadline"
            )

        if task.priority < 1 or task.priority > 5:
            errors.append(
                f"{task.task_id} priority must be between 1 and 5"
            )

    return errors


def validate_resources(resources):
    errors = []

    for resource in resources:

        if resource["shift_start_h"] >= resource["shift_end_h"]:
            errors.append(
                f"{resource['res_id']} shift hours invalid"
            )

        if resource["max_hours_per_day"] <= 0:
            errors.append(
                f"{resource['res_id']} max hours invalid"
            )

    return errors