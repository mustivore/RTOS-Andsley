import math
import matplotlib.pyplot as plt
import numpy as np
import queue

from UnitOfTime import UnitOfTime


class Scheduler:
    def __init__(self, tasks):
        self.tasks = tasks
        self.jobQueue = queue.PriorityQueue()
        self.jobsByTask = dict()
        maxOffset = max(self.tasks, key=lambda t: t.offset).offset
        hyperPeriod = lcm(self.tasks)
        self.endOfFeasibilityInterval = maxOffset + (2 * hyperPeriod)
        self.schedulerArray = [UnitOfTime(i) for i in range(self.endOfFeasibilityInterval)]
        for i in range(1, len(tasks) + 1):
            self.tasks[i - 1].priority = i
            self.jobsByTask[self.tasks[i - 1]] = queue.Queue()

    # function that simulates an ftp scheduler
    def schedule(self):
        i = 0
        while i < self.endOfFeasibilityInterval:
            for task in self.tasks:  # For each task we are doing some stuff

                # Test if we reached a period. If True then create a new job
                if ((i - task.offset) % task.period) == 0 and i >= task.offset:
                    job = task.createNewJob(i)
                    self.jobQueue.put(job)
                    self.jobsByTask[task].put(job)

                if not self.jobsByTask[task].empty():
                    job = self.jobsByTask[task].queue[0]  # Test if the job reached his absolute deadline
                    if i == job.deadline:
                        self.schedulerArray[i].addNewTaskToDeadlineMissed(task)
                        if task.typeOfDeadline == 'hard':  # If it's a hard deadline we stop the simulator
                            print(task.name, 'miss a hard deadline at time', i)
                            return False
                        else:
                            print(task.name, 'miss a soft deadline at time', i)

            if not self.jobQueue.empty():
                # Peek the first element of the job queue
                # (according to the priority => see the method __gt__ in the Job's class)
                # which should be assigned to the UnitOfTime
                job = self.jobQueue.queue[0]
                job.decreaseExecutionTime()
                self.schedulerArray[i].setIsAssignedFor(job.task)
                if job.executionTime == 0:
                    self.jobQueue.get()
                    self.jobsByTask[job.task].get()
            i += 1
        return True

    # function that draws the graph representing the ordering of the tasks.
    def plot(self):
        colors = ['red', 'blue', 'green', 'yellow', 'orange']
        for i in range(len(self.tasks)):
            self.tasks[i].color = colors[i % len(colors)]
        fig, ax = plt.subplots()
        ax.set_xlabel('Time')
        ax.grid(axis='x')
        ax.set_yticks(np.arange(13, 13 * len(self.tasks), 10))
        ax.set_yticklabels(t.name for t in self.tasks)
        plt.xticks(np.arange(0, len(self.schedulerArray), gcd(self.tasks)))
        deadlineMissed = False
        previousTask = None
        start = 0
        i = 0
        while i < self.endOfFeasibilityInterval:
            for task in self.schedulerArray[i].tasksDeadlineMissed:
                dl = plt.Circle((self.schedulerArray[i].index, 13 * task.number), 1.5, color='black')
                ax.add_patch(dl)
                deadlineMissed = True

            currentTask = self.schedulerArray[i].isAssignedFor
            if previousTask is None:
                previousTask = currentTask
                start = self.schedulerArray[i].index
            elif previousTask is not currentTask:
                ax.broken_barh([(start, self.schedulerArray[i].index - start)], (previousTask.number * 10, 7),
                               facecolors=previousTask.color)
                start = self.schedulerArray[i].index
                previousTask = currentTask
            i += 1

        if deadlineMissed:
            plt.legend(['Deadline missed'])
        plt.show()


# function to calculate LCM of each period from tasks array
def lcm(tasksArray):
    lcm = tasksArray[0].period
    for i in range(1, len(tasksArray)):
        lcm = lcm * tasksArray[i].period // math.gcd(lcm, tasksArray[i].period)
    return lcm


# function to calculate LCM of each period from tasks array
def gcd(tasksArray):
    pgcd = tasksArray[0].wcet
    for i in range(1, len(tasksArray)):
        pgcd = math.gcd(pgcd, tasksArray[i].wcet)
    return pgcd
