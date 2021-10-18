import math
import matplotlib.pyplot as plt
import numpy as np

from UnitOfTime import UnitOfTime


class Scheduler:
    def __init__(self, tasks):
        self.tasks = tasks
        self.schedulerArray = None

    def __initialiseDeadlineAndPeriod(self, endOfFeasibilityInterval):
        scheduleArray = [UnitOfTime(i) for i in range(endOfFeasibilityInterval + 1)]
        for task in self.tasks:
            previousPeriod = task.offset + task.period
            previousDeadline = task.offset + task.deadline
            scheduleArray[task.offset].addNewTaskToPeriod(task)
            scheduleArray[task.offset + task.period].addNewTaskToPeriod(task)
            scheduleArray[task.offset + task.deadline].addNewTaskToDeadline(task)

            for i in range(task.offset + 1, endOfFeasibilityInterval + 1):
                if i - previousPeriod == task.period:
                    scheduleArray[i].addNewTaskToPeriod(task)
                    previousPeriod = i
                if i - previousDeadline == task.deadline:
                    scheduleArray[i].addNewTaskToDeadline(task)
                    previousDeadline = i
        return scheduleArray

    def schedule(self):
        maxOffset = max(self.tasks, key=lambda t: t.offset).offset
        hyperPeriod = lcm(self.tasks)
        endOfFeasibilityInterval = maxOffset + (2 * hyperPeriod)
        self.schedulerArray = self.__initialiseDeadlineAndPeriod(endOfFeasibilityInterval)
        hardDeadlineMissed = False
        i = 0
        while i < endOfFeasibilityInterval and not hardDeadlineMissed:
            for task in self.schedulerArray[i].tasksDeadline:
                if task.executionTimeLeft != 0:
                    if task.typeOfDeadline == 'hard':
                        print(task.name, 'miss a hard deadline at time', i)
                        hardDeadlineMissed = True
                    else:
                        print(task.name, 'miss a soft deadline at time', i)

            if hardDeadlineMissed:
                continue

            for task in self.schedulerArray[i].tasksPeriod:
                task.executionTimeLeft += task.wcet
                task.isReleased = True

            for task in self.tasks:
                if task.isReleased:
                    self.schedulerArray[i].setIsAssignedFor(task)
                    task.decreaseExecutionTimeLeft()
                    if task.executionTimeLeft == 0:
                        task.isReleased = False
                    break
            i += 1

    def plot(self):
        colors = ['red', 'blue', 'green', 'yellow', 'orange']
        for i in range(len(self.tasks)):
            self.tasks[i].color = colors[i % len(colors)]
        fig, gnt = plt.subplots()
        gnt.set_xlabel('Time')
        gnt.grid(axis='x')
        gnt.set_yticks(np.arange(13, 13 * len(self.tasks), 10))
        gnt.set_yticklabels(t.name for t in self.tasks)
        plt.xticks(np.arange(0, len(self.schedulerArray) + 1, 10))
        previousTask = None
        start = 0
        for unitOfTime in self.schedulerArray:
            currentTask = unitOfTime.isAssignedFor
            if previousTask is None:
                previousTask = currentTask
                start = unitOfTime.index
            elif previousTask is not currentTask:
                gnt.broken_barh([(start, unitOfTime.index - start)], (previousTask.number * 10, 7),
                                facecolors=previousTask.color)
                start = unitOfTime.index
                previousTask = currentTask

        plt.show()


# function to calculate LCM of a tasks array
def lcm(tasksArray):
    lcm = tasksArray[0].period
    for i in range(1, len(tasksArray)):
        lcm = lcm * tasksArray[i].period // math.gcd(lcm, tasksArray[i].period)
    return lcm
