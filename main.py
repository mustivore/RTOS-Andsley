import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import math

from Task import Task
from UnitOfTime import UnitOfTime

task1 = Task("T1", 100, 10, 20, 30)
task2 = Task("T2", 50, 20, 50, 50)
task3 = Task("T3", 0, 30, 100, 150)
tasks = [task1, task2, task3]


# function to calculate LCM of a tasks array
def lcm(tasksArray):
    lcm = tasksArray[0].period
    for i in range(1, len(tasksArray)):
        lcm = lcm * tasksArray[i].period // math.gcd(lcm, tasksArray[i].period)
    return lcm


def initialiseDeadlinePeriod(endOfFeasibilityInterval, tasksArray):
    scheduleArray = [UnitOfTime() for i in range(endOfFeasibilityInterval+1)]
    for task in tasksArray:
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


def scheduler(tasksArray):
    maxOffset = max(tasksArray, key=lambda t: t.offset).offset
    hyperPeriod = lcm(tasksArray)
    endOfFeasibilityInterval = maxOffset + (2 * hyperPeriod)
    schedulerByTask = initialiseDeadlinePeriod(endOfFeasibilityInterval, tasksArray)
    # for i in range(endOfFeasibilityInterval + 1):
    #     for task in tasks:
    #         if task.isReleased:
    #
    #             break
    #     break
    return schedulerByTask


print(scheduler(tasks))
