class Subjects:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


def load_data():
    subjects = []
    names = []
    tot_marks = []

    with open("safefile.txt") as file:

        for line in file:
            name = line[:line.index(":")]
            marks = line[line.index(":") + 1:]

            marks = marks.split(",")

            tot_marks.append(marks)
            names.append(name)

    for subject in names:
        subject = Subjects(subject, tot_marks[names.index(subject)])
        subjects.append(subject)

    return subjects
def do_nothing():
    pass

if __name__ == '__main__':
    subjects = load_data()
    print(subjects[0].name, subjects[0].marks)