from Job import Job


class Task:

    def __init__(self, number, offset, wcet, deadline, period, typeOfDeadline, color=None):
        self.number = number
        self.name = 'T' + str(number)
        self.queueJobs = Queue()
        self.nbJobCreated = 0
        self.offset = offset
        self.wcet = wcet
        self.deadline = deadline
        self.period = period
        self.typeOfDeadline = typeOfDeadline
        self.isReleased = False
        self.color = color

    def createNewJob(self, currentPeriod):
        self.nbJobCreated += 1
        job = Job(self.nbJobCreated, self.wcet, currentPeriod + self.deadline)
        self.queueJobs.enqueue(job)

    def getCurrentJob(self):
        return self.queueJobs.peek()

    def decreaseExecutionTimeOfTheCurrentJob(self):
        job = self.getCurrentJob()
        job.decreaseExecutionTime()
        if job.executionTime == 0:
            self.queueJobs.dequeue()
            if self.queueJobs.size() == 0:
                self.isReleased = False


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)
