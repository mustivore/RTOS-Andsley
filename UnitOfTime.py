class UnitOfTime:
    def __init__(self):
        self.isAssignedFor = None
        self.tasksDeadline = set()
        self.tasksPeriod = set()

    def setIsAssignedFor(self, task):
        self.isAssignedFor = task

    def addNewTaskToDeadline(self, task):
        self.tasksDeadline.add(task)

    def addNewTaskToPeriod(self, task):
        self.tasksPeriod.add(task)
