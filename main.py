class Subjects:
    def __init__(self, name, ex_names, ex_marks):
        self.name = name
        self.ex_marks = ex_marks
        self.ex_names = ex_names
        self.average = sum(ex_marks)/len(ex_marks)



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
                print(mark)
                ex_names.append(mark[0])
                ex_marks.append(int(mark[1]))


            name = Subjects(name, ex_names, ex_marks)
            subjects.append(name)

    return subjects


def run(subjects):
    pass


if __name__ == '__main__':
    subjects = load_data()
    run(subjects)
