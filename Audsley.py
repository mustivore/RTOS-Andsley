from Scheduler import Scheduler


class Audsley:

    def __init__(self):
        self.solution = []

    # function that allows us to find a priority assignment for a set of tasks
    def assign_priority(self, tasks):

        if len(tasks) == 1:  # Feasible
            print("A FTP assignment has been found !")
            self.solution.append(tasks[0])
            f = open("audsley.txt", "w")
            size = len(self.solution)
            i = 0
            while i < size:
                task = self.solution.pop()
                f.write(str(task.offset) + " " + str(task.wcet) + " " + str(task.deadline) + " " +
                        str(task.period) + " " + "\n")
                i += 1
            f.close()
            return True
        else:
            for i in range(1, len(tasks) + 1):
                tasks[-1].typeOfDeadline = 'hard'
                scheduler = Scheduler(tasks)
                print("Test", tasks[- 1].name, "as the lowest-priority viable task")
                if scheduler.schedule():
                    print(tasks[- 1].name, "is the lowest-priority viable task")
                    self.solution.append(tasks[-1])
                    tasks.pop()
                    self.assign_priority(tasks)
                    break
                else:
                    if i == len(tasks):  # Not Feasible
                        print("There is no lowest-priority viable task !")
                        return False
                    tasks[-1].typeOfDeadline = 'soft'
                    # swap 2 tasks
                    temp = tasks[-1]
                    tasks[-1] = tasks[len(tasks) - i - 1]
                    tasks[len(tasks) - i - 1] = temp
