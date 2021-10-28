from Job import Job


class Task:

    def __init__(self, number, offset, wcet, deadline, period, typeOfDeadline, color=None):
        self.number = number
        self.name = 'T' + str(number)
        self.nbJobCreated = 0
        self.offset = offset
        self.wcet = wcet
        self.deadline = deadline
        self.period = period
        self.typeOfDeadline = typeOfDeadline
        self.color = color
        self.priority = None

    def createNewJob(self, currentPeriod):
        self.nbJobCreated += 1
        job = Job(self, self.nbJobCreated, self.wcet, currentPeriod + self.deadline)
        return job
