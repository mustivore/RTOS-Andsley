import sys
import os.path
import io

from Task import Task
from Scheduler import Scheduler


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


if __name__ == "__main__":
    length = len(sys.argv)
    if length == 2 and sys.argv[1] == 'audsley':
        print('call audley function')
    if length == 3 and sys.argv[1] == 'scheduler' and os.path.isfile(sys.argv[2]):
        tasks = parseTextFileToTasksArray(sys.argv[2])
        tasks[len(tasks) - 1].typeOfDeadline = "hard"
        scheduler = Scheduler(tasks)
        scheduler.schedule()
        scheduler.plot()
    else:
        print(showUsageError())
        sys.exit(-1)
