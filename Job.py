class Job:

    def __init__(self, task, number, executionTime, deadline):
        self.task = task
        self.number = number
        self.executionTime = executionTime
        self.deadline = deadline

    def decreaseExecutionTime(self):
        self.executionTime -= 1

    def __gt__(self, other):
        if self.task.number == other.task.number:
            return self.number > other.number
        return self.task.number > other.task.number

    def __eq__(self, other):
        if self.task.number == other.task.number:
            return self.number == other.number
        return False
