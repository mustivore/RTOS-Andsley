class Task:
    def __init__(self, name, offset, wcet, deadline, period, typeOfDeadline ="soft"):
        self.offset = offset
        self.wcet = wcet
        self.deadline = deadline
        self.period = period
        self.typeOfDeadline = typeOfDeadline
        self.isReleased = offset == 0
