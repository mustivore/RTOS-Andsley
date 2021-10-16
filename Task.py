class Task:
    def __init__(self, name, offset, wcet, deadline, period, typeOfDeadline="soft"):
        self.name = name
        self.offset = offset
        self.wcet = wcet
        self.executionTimeLeft = wcet
        self.deadline = deadline
        self.period = period
        self.typeOfDeadline = typeOfDeadline
        self.isReleased = offset == 0

    def decreaseExecutionTimeLeft(self):
        self.executionTimeLeft -= 1
