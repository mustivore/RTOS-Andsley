from Scheduler import Scheduler


class Audsley:

    def __init__(self, tasks):
        self.tasks = tasks

    def assign_priority(self):
        self.__assign_priority(0, [])

    def __assign_priority(self, testedTaskNumber, priorityAssignmentStack):

        if testedTaskNumber == len(self.tasks):
            print("there is no lowest-priority viable task!!!")
            return False

        if len(self.tasks) == 1:
            print("A FTP assignment has been found!!!")
            priorityAssignmentStack.append(self.tasks[- 1])
            f = open("audsley.txt", "w")

            while priorityAssignmentStack:
                task = priorityAssignmentStack.pop()
                f.write(str(task.offset) + " " + str(task.wcet) + " " + str(task.deadline) + " " + str(
                    task.period) + " " + "\n")
            return True

        print("Test lowest-priority viable task ", self.tasks[- 1].name)
        self.tasks[-1].typeOfDeadline = "hard"
        scheduler = Scheduler(self.tasks)
        if scheduler.schedule():
            # scheduler return true so we need to remove a task
            priorityAssignmentStack.append(self.tasks[- 1])
            print(self.tasks[- 1].name, "is the lowest-priority viable task ")
            self.tasks.pop()
            return self.__assign_priority(0, priorityAssignmentStack)
        else:
            testedTaskNumber += 1
            self.tasks[-1].typeOfDeadline = "soft"

            # swap 2 tasks
            temp = self.tasks[-1]
            self.tasks[-1] = self.tasks[len(self.tasks) - testedTaskNumber - 1]
            self.tasks[len(self.tasks) - testedTaskNumber - 1] = temp

            return self.__assign_priority(testedTaskNumber, priorityAssignmentStack)
