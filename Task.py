class Task:
    Number = 1

    def __init__(self, name, offset, wcet, deadline, period, color=None, typeOfDeadline="soft"):
        self.number = Task.Number
        Task.Number += 1
        self.name = name
        self.offset = offset
        self.wcet = wcet
        self.executionTimeLeft = 0
        self.deadline = deadline
        self.period = period
        self.typeOfDeadline = typeOfDeadline
        self.isReleased = offset == 0
        self.color = color

    def decreaseExecutionTimeLeft(self):
        self.executionTimeLeft -= 1
