class Subjects:
    def __init__(self, marks):
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

    return names, tot_marks

if __name__ == '__main__':
    names, marks = load_data()
    print(names, marks)