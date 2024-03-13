class Subjects:
    def __init__(self, name, ex_names, ex_marks):
        self.name = name
        self.ex_marks = ex_marks
        self.ex_names = ex_names
        self.average = sum(ex_marks) / len(ex_marks)


def load_data():
    subjects = []
    names = []

    with open("safefile.txt") as file:

        for line in file:

            ex_names = []
            ex_marks = []

            name = line[:line.index("\\")]
            marks = line[line.index("\\"):-1]
            marks = marks.split(",")
            names.append(name)

            for mark in marks:
                mark = mark.split(":")
                ex_names.append(mark[0])
                ex_marks.append(int(mark[1]))

            name = Subjects(name, ex_names, ex_marks)
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
    with open("text.txt") as text:
        print(text.read())

    for subject in subjects:
        print(subject.name + " :")
        for name in subject.ex_names:
            distance = 20 - len(name.replace("\\", "").replace(" ", ""))
            print(name.replace("\\", "").replace(" ", "") + ":" + " " * distance + str(
                subject.ex_marks[subject.ex_names.index(name)]))

        print("\nAverage:" + " " * 13 + str(subject.average))
        print("\n\n")


def run(subjects):
    while True:
        command = input("What action do you want to perform?    ")
        if "help" in command:
            with open("commands.txt") as file:
                print(file.read)
        elif "change" in command:
            subjects = change_mark(subjects)
            setup(subjects)
        elif command == "exit":
            break
        else:
            print("Use the Help command to see a list of commands")
    return subjects
def safe_changes(subjects):
    content = ""
    for subject in subjects:
        content += subject.name
        for exam in subject.ex_names:
            content += subject.ex_names[subject.ex_names.index(exam)] + ":" + str(subject.ex_marks[subject.ex_names.index(exam)])
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
