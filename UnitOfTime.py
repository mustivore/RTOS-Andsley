class UnitOfTime:
    def __init__(self, index):
        self.index = index
        self.isAssignedFor = None
        self.tasksDeadlineMissed = set()

    def setIsAssignedFor(self, task):
        self.isAssignedFor = task

    def addNewTaskToDeadlineMissed(self, task):
        self.tasksDeadlineMissed.add(task)
