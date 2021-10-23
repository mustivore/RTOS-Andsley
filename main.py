import sys
import os.path
import io

from Audsley import Audsley
from Task import Task
from Scheduler import Scheduler


def showUsageError():
    return 'usage error : main.py [audsley|scheduler] <task_file> '


def parseTextFileToTasksArray(filename, typeOfDeadline):
    tasks = []
    with io.open(filename, 'r', encoding='utf-8') as f:
        task_index = 1
        for line in f:
            line_split = line.split()

            if len(line_split) != 4:
                print('wrong file format')
                return sys.exit()

            tasks.append(Task(task_index, int(line_split[0]), int(line_split[1]),
                              int(line_split[2]), int(line_split[3]), typeOfDeadline))
            task_index += 1

    return tasks


if __name__ == "__main__":

    length = len(sys.argv)

    if length == 3 and os.path.isfile(sys.argv[2]):
        if sys.argv[1] == 'audsley':
            tasks = parseTextFileToTasksArray(sys.argv[2], 'soft')
            audsley = Audsley(tasks)
            audsley.assign_priority()
        elif sys.argv[1] == 'scheduler':
            tasks = parseTextFileToTasksArray(sys.argv[2], 'hard')
            scheduler = Scheduler(tasks)
            scheduler.schedule()
            scheduler.plot()
        else:
            print(showUsageError())
            sys.exit(-1)
    else:
        print(showUsageError())
        sys.exit(-1)
