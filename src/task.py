class Task:

    def __init__(
        self,
        task_id,
        duration_h,
        deadline_h,
        priority,
        skill,
        depends_on
    ):
        self.task_id = task_id
        self.duration_h = duration_h
        self.deadline_h = deadline_h
        self.priority = priority
        self.skill = skill
        self.depends_on = depends_on

        # Profit derived from priority
        self.profit = priority * 100

    def __repr__(self):

        return (
            f"Task("
            f"{self.task_id}, "
            f"P={self.priority}, "
            f"D={self.deadline_h}, "
            f"Dur={self.duration_h}, "
            f"Profit={self.profit}"
            f")"
        )