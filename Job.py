class Job:

    def __init__(self, number, executionTime, deadline):
        self.number = number
        self.executionTime = executionTime
        self.deadline = deadline

    def decreaseExecutionTime(self):
        self.executionTime -= 1
