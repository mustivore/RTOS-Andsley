import matplotlib.pyplot as plt
import math
import sys
from Task import Task
from UnitOfTime import UnitOfTime
import os.path
import io


# task1 = Task("T1", 100, 10, 20, 30)
# task2 = Task("T2", 50, 20, 50, 50)
# task3 = Task("T3", 0, 30, 100, 150)
# tasks = [task3, task1, task2]


def checkArgumentLine(length):
    if length == 2 and sys.argv[1] == 'audsley':
        return 'call audley function'
    if length == 3 and sys.argv[1] == 'scheduler' and os.path.isfile(sys.argv[2]):
        return scheduler(parseTextFileToTasksArray(sys.argv[2]))
    else:
        showUsageError()
        return sys.exit()


def showUsageError():
    return 'usage error : to do '


def parseTextFileToTasksArray(filename):
    tasks = []
    with io.open(filename, 'r', encoding='utf-8') as f:
        task_index = 1
        for line in f:
            line_split = line.split()

            if len(line_split) != 4:
                print('wrong file format')
                return sys.exit()

            tasks.append(Task('T' + str(task_index), int(line_split[0]), int(line_split[1]),
                              int(line_split[2]), int(line_split[3])))
            task_index += 1

    return tasks


# function to calculate LCM of a tasks array
def lcm(tasksArray):
    lcm = tasksArray[0].period
    for i in range(1, len(tasksArray)):
        lcm = lcm * tasksArray[i].period // math.gcd(lcm, tasksArray[i].period)
    return lcm


def initialiseDeadlineAndPeriod(endOfFeasibilityInterval, tasksArray):
    scheduleArray = [UnitOfTime() for i in range(endOfFeasibilityInterval + 1)]
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
    schedulerArray = initialiseDeadlineAndPeriod(endOfFeasibilityInterval, tasksArray)
    for i in range(endOfFeasibilityInterval + 1):
        for task in schedulerArray[i].tasksPeriod:
            task.executionTimeLeft += task.wcet
            task.isReleased = True

        for task in tasksArray:
            if task.isReleased:
                schedulerArray[i].setIsAssignedFor(task)
                task.decreaseExecutionTimeLeft()
                if task.executionTimeLeft == 0:
                    task.isReleased = False
                break
    plot(schedulerArray)
    return schedulerArray


def plot(schedulerArray):
    fig, gnt = plt.subplots()
    gnt.set_xlabel('Seconds since start')
    gnt.set_ylabel('Tasks')
    previousTask = None
    for unitOfTime in schedulerArray:
        if previousTask is None:
            previousTask = unitOfTime.isAssignedFor


def main():
    print(checkArgumentLine(len(sys.argv)))


if __name__ == "__main__":
    main()
