class UnitOfTime:
    def __init__(self, index):
        self.index = index
        self.isAssignedFor = None
        self.tasksDeadlineMissed = set()
        self.tasksPeriod = set()

    def setIsAssignedFor(self, task):
        self.isAssignedFor = task

    def addNewTaskToDeadlineMissed(self, task):
        self.tasksDeadlineMissed.add(task)

    def addNewTaskToPeriod(self, task):
        self.tasksPeriod.add(task)
