import os
from colorama import Fore

class Subjects:
    def __init__(self, name, ex_names, ex_marks, weight):
        self.name = name
        self.ex_marks = ex_marks
        self.ex_names = ex_names
        self.weight = weight
        average = []
        for mark in ex_marks:
            for i in range(int(weight[ex_marks.index(mark)])):
                average.append(mark)
        print(average)
        self.average = sum(average)/len(average)

    def update(self):
        average = []
        for mark in self.ex_marks:
            if int(self.weight[self.ex_marks.index(mark)]) != 1:
                for i in range(int(self.weight[self.ex_marks.index(mark)])):
                    average.append(mark)
            else:
                average.append(mark)

        self.average = sum(average) / len(average)


def load_data():
    subjects = []
    names = []

    with open("safefile.txt") as file:

        for line in file:

            ex_names = []
            ex_marks = []
            ex_weight = []

            name = line[:line.index("\\")]
            marks = line[line.index("\\"):-1]
            marks = marks.split(",")
            names.append(name)

            for mark in marks:
                mark = mark.split(":")
                ex_names.append(mark[0])
                ex_marks.append(float(mark[1]))
                ex_weight.append(int(mark[2]))

            name = Subjects(name, ex_names, ex_marks, ex_weight)
            subjects.append(name)

    return subjects


def change_mark(subjects):
    subject_index = 18769
    mark_index = 42069

    subject_name = input("what subjects mark do you want to change?")
    if subject_name == "exit":
        return subjects

    for subject in subjects:
        if subject.name.lower() == subject_name.lower():
            subject_index = subjects.index(subject)

    if subject_index == 18769:
        print("please select a valid subject")
        return subjects

    exam_name = input("what mark would you like to change?")

    if exam_name == "exit":
        return subjects

    for mark_name in subjects[subject_index].ex_names:
        if mark_name.lower().replace("\\", "").replace(" ", "") == exam_name.lower():
            mark_index = subjects[subject_index].ex_names.index(mark_name)

    if mark_index == 42069:
        print("please select a valid exam")
        return subjects

    new_mark = input("what would you like to change the mark to?")

    subjects[subject_index].ex_marks[mark_index] = new_mark
    return subjects

def setup(subjects):
    os.system('cls')
    with open("text.txt") as text:
        print(Fore.LIGHTMAGENTA_EX + text.read())

    for subject in subjects:
        print(subject.name + " :")
        for name in subject.ex_names:
            distance = 30 - len(name.replace("\\", "").replace(" ", ""))
            print(name.replace("\\", "").replace(" ", "") + ":" + " " * distance +
                  str(subject.ex_marks[subject.ex_names.index(name)]) + " "*5 +
                  str(subject.weight[subject.ex_names.index(name)]))

        print("\nAverage:" + " " * 23 + str(subject.average))
        print("\n\n")

def add(subjects, command):
    type = ""
    ex_name = []
    ex_mark = []
    weight = []
    if command == "add":
        ask_type = input("would you like to add a subject or mark?")
        if "mark" in ask_type:
            type = "mark"
        elif "subj" in ask_type:
            type = "subject"

    elif "add" in command:

        if "mark" in command:
            type = "mark"
        elif "subj" in command:
            type = "subject"
        else:
            print("please select a valid type")
            type = "invalid"

    if type == "subject":
        name = input("how would you like to call the subject?") + "\\"
        exam = input("add an exam to the subject (seperate name, mark and weight with \":\")")
        ex_name.append(exam.split(":")[0])
        ex_mark.append(float(exam.split(":")[1]))
        weight.append(int(exam.split(":")[2]))
        name = Subjects(name, ex_name, ex_mark, weight)
        subjects.append(name)

    elif type == "mark":
        sub_index = 69420
        subject = input("add a mark to what subject? ")
        for sub in subjects:
            if subject.lower() == sub.name:
                sub_index = subjects.index(sub)

        if sub_index != 69420:
            exam_data = input("add an exam to the subject (seperate name, mark and weight with \":\")")
            exam_name = exam_data.split(":")[0]
            exam_mark = float(exam_data.split(":")[1])
            weight = int(exam_data.split(":")[2])
            subjects[sub_index].ex_names.append(exam_name)
            subjects[sub_index].ex_marks.append(exam_mark)
            subjects[sub_index].weight.append(weight)

    return subjects

def delete(subjects, command):
    type = ""
    sub_name = ""
    mark_name = ""
    command = command.split()

    if len(command) == 3:
        type = command[1]
        sub_name = command[2]
        if type.lower() != "subject":
            print("please use valid syntax")
            return subjects

    elif len(command) == 4:
        type = command[1]
        sub_name = command[2]
        mark_name = command[3]
        if type.lower() != "mark":
            print("please use valid syntax")
            return subjects

    if type == "":
        print("please use remove + type + subject + mark to delete a mark")
        return subjects

    if type.lower() == "mark":
        subject_index = 69420
        mark_index = 69420
        for subject in subjects:
            if sub_name.lower() == subject.name:
                subject_index = subjects.index(subject)

        if subject_index == 69420:
            print("please select a valid subject")
            return subjects

        for element in subjects[subject_index].ex_names:
            if element.lower().strip("\\").strip() == mark_name.lower().strip():
                mark_index = subjects[subject_index].ex_names.index(element)

        if mark_index == 69420:
            print("please select a valid mark")
            return subjects

        if input(f"do you want to remove {mark_name} from {sub_name}? (y/n)").lower() == "y":
            subjects[subject_index].ex_names.pop(mark_index)
            subjects[subject_index].ex_marks.pop(mark_index)
            subjects[subject_index].weight.pop(mark_index)
        else:
            return subjects

    elif type == "subject":
        subject_index = 69420
        for subject in subjects:
            if sub_name.lower() == subject.name.lower():
                subject_index = subjects.index(subject)

        if subject_index == 69420:
            print("please select a valid subject")
            return subjects
        if input(f"do you want do delte {sub_name}? (y/n)").lower() == "y":
            subjects.pop(subject_index)
        else:
            return subjects

    else:
        print("this should not happen, lol0")
        return subjects

    return subjects



def run(subjects):
    while True:
        command = input("What action do you want to perform?    ")
        if "help" in command:
            with open("commands.txt") as file:
                print(file.read)

        elif "change" in command:
            subjects = change_mark(subjects)
            setup(subjects)


        elif "main" in command:
            setup(subjects)

        elif "add" in command:
            subjects = add(subjects,command)
            setup(subjects)


        elif "remove" in command:
            subjects = delete(subjects, command)
            setup(subjects)

        elif command == "exit":
            break
        else:
            print("Use the Help command to see a list of commands")
        for subject in subjects:
            subject.update()

    return subjects
def safe_changes(subjects):
    content = ""
    for subject in subjects:
        content += subject.name
        for exam in subject.ex_names:
            content += (subject.ex_names[subject.ex_names.index(exam)] + ":" +
                        str(subject.ex_marks[subject.ex_names.index(exam)]) + ":" +
                        str(int(subject.weight[subject.ex_names.index(exam)]))).strip("]").strip("[")
            if subject.ex_names.index(exam) < len(subject.ex_names)-1:
                content += ","
        content += "\n"


    with open("safefile.txt", 'w') as file:
        file.write(content)


if __name__ == '__main__':
    subjects = load_data()
    setup(subjects)
    subjects = run(subjects)
    safe_changes(subjects)
