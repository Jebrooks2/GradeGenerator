import csv
import os
from src1.gradebook3 import Gradebook
from src1.gradebook2 import Gradebook2
from tkinter import *
from tkinter import scrolledtext
import tkinter as tk

class GUI:

    def __init__(self, master, path):

        self.path = path
        self.master = master
        self.master.title("Paint")
        self.master.state("zoomed")

        self.master.rowconfigure(1000, weight=10)
        self.master.columnconfigure(1000, weight=0)

        menubar = Menu(window)
        self.master.config(menu=menubar)
        submenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="file", menu=submenu)

        frame = tk.Frame(self.master)
        self.frame = frame
        hor = Scrollbar(frame, orient='horizontal')
        hor.grid(row=0, column=10)
        vert = Scrollbar(frame, orient='vertical')
        vert.grid(row=50, column=0)
        text = Text(frame, width=140, height=25, wrap='none', xscrollcommand=hor.set, yscrollcommand=vert.set)
        hor.config(command=text.xview)
        vert.config(command=text.yview)

        # textHsb = tk.Scrollbar(frame, orient=HORIZONTAL, command=text.xview)
        # textVsb = tk.Scrollbar(frame, orient="vertical", command=text.yview)
        # text.configure(yscrollcommand=textVsb.set, xscrollcommand=textHsb.set)
        self.text = text
        self.text.grid(row=1, column=10)
        self.label = Label(self.master, text="Enter Course1 Student Name and press Enter: ")
        self.bar = Entry(self.master)
        self.bar.bind("<Return>", self.get_stu)
        self.bar.grid(row=450, column=1000)
        self.label.grid(row=400, column=1000)

        self.label2 = Label(self.master, text="Enter Course2 Student Name and press Enter: ")
        self.bar2 = Entry(self.master)
        self.bar2.bind("<Return>", self.get_stu2)
        self.bar2.grid(row=600, column=1000)
        self.label2.grid(row=550, column=1000)

        self.label3 = Label(self.master, text="Enter Course3 Student Name and press Enter: ")
        self.bar3 = Entry(self.master)
        self.bar3.bind("<Return>", self.get_stu3)
        self.bar3.grid(row=800, column=1000)
        self.label3.grid(row=750, column=1000)

        self.frame = frame.grid(row=10, column=10)
        self.write_slogan()

    def get_stu(self, *args):
        self.clear()
        main = Gradebook2(grade_book_path, roster_file_path, test_files, project_files, quiz_files)
        for num, line in enumerate(main.__str__()):
            print(num)
            print(len(main.__str__()))
            if self.bar.get().upper().strip() in line:
                self.text.insert('insert', str(line))
                self.bar.delete(0, 100)
                break
            if num+1 == len(main.__str__()):
                self.text.insert("insert", "Not a valid name")
                self.bar.delete(0, 100)

    def get_stu2(self, *args):
        self.clear()
        main = Gradebook2(grade_book_path, roster_file_path2, test_files2, project_files2, quiz_files2)
        for num, line in enumerate(main.__str__()):
            if self.bar2.get().upper().strip() in line:
                self.text.insert('insert', str(line))
                self.bar2.delete(0, 100)
                break
            if num + 1 == len(main.__str__()):
                self.bar2.delete(0, 100)
                self.text.insert("insert", "Not a valid name")


    def get_stu3(self, *args):
        self.clear()
        main = Gradebook2(grade_book_path, roster_file_path3, test_files3, project_files3, quiz_files3)
        for num, line in enumerate(main.__str__()):
            if self.bar3.get().upper().strip() in line:
                self.text.insert('insert', str(line))
                self.bar3.delete(0, 100)
                break
            if num+1 == len(main.__str__()):
                self.bar3.delete(0, 100)
                self.text.insert("insert", "Not a valid name")



    def print_list11(self):
        self.clear()
        crn9011 = Gradebook(grade_book_path, roster_file_path, test_files, project_files, quiz_files)
        self.text.insert('insert', crn9011.__str__())
        main = Gradebook2(grade_book_path, roster_file_path, test_files, project_files, quiz_files)
        for line in main.__str__():
            self.text.insert('insert', str(line))

    def print_list12(self):
        self.clear()
        crn9012 = Gradebook(grade_book_path, roster_file_path2, test_files2, project_files2, quiz_files2)
        self.text.insert('insert', crn9012.__str__())
        main = Gradebook2(grade_book_path, roster_file_path2, test_files2, project_files2, quiz_files2)
        for line in main.__str__():
            self.text.insert('insert', str(line))

    def print_list13(self):
        self.clear()
        crn9013 = Gradebook(grade_book_path, roster_file_path3, test_files3, project_files3, quiz_files3)
        self.text.insert('insert', crn9013.__str__())
        main = Gradebook2(grade_book_path, roster_file_path3, test_files3, project_files3, quiz_files3)
        for line in main.__str__():
            self.text.insert('insert', str(line))

    def clear(self):
        self.text.delete('1.0', END)

    def write_slogan(self):
        print("Tkinter is easy to use!")

        # button = tk.Button(
        #     text="Click me!",
        #     width=25,
        #     height=5,
        #     bg="blue",
        #     fg="yellow",
        # )
        button2 = tk.Button(self.master,
                            text='clear',
                            fg='red',
                            command=self.clear)
        button2.grid(row=70, column=100)
        button = tk.Button(self.master,
                           text="QUIT",
                           fg="red",
                           command=quit)
        button.grid(row=60, column=100)
        slogan = tk.Button(self.master,
                           text="crn9011",
                           command=self.print_list11)
        slogan.grid(row=30, column=100)

        slogan1 = tk.Button(self.master,
                           text="crn9012",
                           command=self.print_list12)
        slogan1.grid(row=40, column=100)
        slogan2 = tk.Button(self.master,
                           text="crn9013",
                           command=self.print_list13)
        slogan2.grid(row=50, column=100)

        canvas = Canvas(window, background="blue")
    #        canvas.grid(row=0, column=0, sticky="nsew")


if __name__ == '__main__':
    size = "short"  # "big"
    test_files = [os.path.join("data", "course_grades", "crn9011", "T_{}.csv".format(i)) for i in range(2)]
    project_files = [os.path.join("data", "course_grades", "crn9011", "P_{}.csv".format(i)) for i in range(2)]
    quiz_files = [os.path.join("data", "course_grades", "crn9011", "Q_{}.csv".format(i)) for i in range(8)]
    roster_file_path = os.path.join("data", "course_grades", "crn9011", "roster.csv")

    test_files2 = [os.path.join("data", "course_grades", "crn9012", "T_{}.csv".format(i)) for i in range(2)]
    project_files2 = [os.path.join("data", "course_grades", "crn9012", "P_{}.csv".format(i)) for i in range(2)]
    quiz_files2 = [os.path.join("data", "course_grades", "crn9012", "Q_{}.csv".format(i)) for i in range(4)]
    roster_file_path2 = os.path.join("data", "course_grades", "crn9012", "roster.csv")
    
    test_files3 = [os.path.join("data", "course_grades", "crn9013", "T_{}.csv".format(i)) for i in range(2)]
    project_files3 = [os.path.join("data", "course_grades", "crn9013", "P_{}.csv".format(i)) for i in range(2)]
    quiz_files3 = [os.path.join("data", "course_grades", "crn9013", "Q_{}.csv".format(i)) for i in range(3)]
    roster_file_path3 = os.path.join("data", "course_grades", "crn9013", "roster.csv")

    window = tk.Tk()
    grade_book_path = os.path.join("data", "grade_book_{}.csv".format(size))
    # num = Gradebook(grade_book_path, roster_file_path, test_files, project_files, quiz_files)
    crn9011 = Gradebook(grade_book_path, roster_file_path, test_files, project_files, quiz_files)
    crn9012 = Gradebook(grade_book_path, roster_file_path2, test_files2, project_files2, quiz_files2)
    #crn9013 = Gradebook(grade_book_path, roster_file_path, test_files3, project_files3, quiz_files3)
    # crn9012 = Gradebook()
    b = GUI(window, crn9011.__str__())

    window.mainloop()
