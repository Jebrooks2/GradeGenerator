import csv
import numpy as np

"""
Script to handle generating data for class quiz_grades


@author Jakob Brooks, Molly Dieter
@date   10/14/2020
"""

# pylint: disable=C0103

import os

class Gradebook2:

    def __init__(self, output_file_path, roster_file_path, test_files, project_files, quiz_files):
        """
        Given a roster file, and three lists of files for tests, projects, and quizes

        Write a class grade book to the output_file_path as:

        For each student write out the :
        id, overall, test average, project average, quiz average

        For the last four lines of the file, write the:
        "class median" , overall, test , project , quiz
        "class mean" , overall, test , project , quiz
        "class std deviation" , overall, test , project , quiz

        :param output_file_path:  name of class grade book
        :param roster_file_path: file path to roster
        :param test_files:       list of test grade file paths
        :param project_files:    list of project grade file paths
        :param quiz_files:       list of quiz grade file paths
        :return : number of students processed
        """
        # created list in python with all names on roster with the grades of each test
        # duplicate for quizes and projects
        # remove values based on names in the tuple and perform appropriate calculations grades
        # new is list of list of lists containing each students grades
        ex, zee = self.helper_method(roster_file_path)
        self.ex = ex
        overall = []
        test = []
        project = []
        quiz = []
        lol = self.count(roster_file_path)

        test_filez = self.get_list(test_files, roster_file_path)
        quiz_filez = self.get_list(quiz_files, roster_file_path)
        project_filez = self.get_list(project_files, roster_file_path)

        test_for_each = self.make_list(test_filez, roster_file_path)
        quiz_for_each = self.make_list(quiz_filez, roster_file_path)
        project_for_each = self.make_list(project_filez, roster_file_path)
        print("wtf", test_for_each)

        new_test_for_each = self.make_float(test_for_each)
        self.new_test_for_each = new_test_for_each
        print("newtest", new_test_for_each)
        new_quiz_for_each = self.make_float(quiz_for_each)
        self.new_quiz_for_each = new_quiz_for_each
        new_project_for_each = self.make_float(project_for_each)
        self.new_project_for_each = new_project_for_each
        newlist = []
        for index, name in enumerate(ex):
            newlist.append([name,
                            (((sum(new_test_for_each[index])/len(new_test_for_each[index])) * .4) +
                             ((sum(new_quiz_for_each[index])/len(new_quiz_for_each[index])) * .2) +
                             ((sum(new_project_for_each[index])/len(new_project_for_each[index])) * .4)),
                            sum(new_test_for_each[index])/len(new_test_for_each[index]),
                            sum(new_project_for_each[index])/len(new_project_for_each[index]),
                            sum(new_quiz_for_each[index])/len(new_quiz_for_each[index])])
        print("newlistQWERQWEFQEW", newlist)
        with open(output_file_path, 'w') as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerows(newlist)
        self.newlist = newlist
        with open(output_file_path, 'r') as file2:
            reader = csv.reader(file2, delimiter='\t')

            for line in reader:
                if len(line) == 0:
                    continue
                overall.append(float(line[1]))
                test.append(float(line[2]))
                project.append(float(line[3]))
                quiz.append(float(line[4]))

            new1 = np.array(overall)
            self.new1 = new1
            new2 = np.array(test)
            self.new2 = new2
            new3 = np.array(quiz)
            self.new3 = new3
            new4 = np.array(project)
            self.new4 = new4
        with open(output_file_path, 'a') as file3:
            writer = csv.writer(file3, delimiter='\t')
            writer.writerow(["class median", np.median(new1), np.median(new2), np.median(new3), np.median(new4)])
            writer.writerow(["class mean", np.mean(new1), np.mean(new2), np.mean(new3), np.mean(new4)])
            writer.writerow(["class std deviation", np.std(new1), np.std(new2), np.std(new3), np.std(new4)])
            lol = self.count(roster_file_path)

    def __str__(self):
        new = []
        for j, i in enumerate(self.ex):
            lmao = [str(i) for i in self.new_test_for_each[j]]
            res = " ".join(lmao)
            lmao1 = [str(i) for i in self.new_quiz_for_each[j]]
            res1 = " ".join(lmao1)
            lmao2 = [str(i) for i in self.new_project_for_each[j]]
            res2 = " ".join(lmao2)
            new_test = np.array(self.new_test_for_each[j])
            new_quiz = np.array(self.new_quiz_for_each[j])
            new_project = np.array(self.new_project_for_each[j])
            new.append("Student: {}\nTest Scores: {}\n"\
               "Quiz Scores: {}\nProject Scores: {}\n"
                       "TestAVG: {}\nQuizAVG: {}\nProjectAVG: {}\n".format(i[:-2].replace(".", " ").upper(),
                                                            res,
                                                            res1,
                                                            res2,
                                                            np.mean(new_test),
                                                            np.mean(new_quiz),
                                                            np.mean(new_project)))
        return new

    def count(self, roster_file_path):
        lol, yeet = self.helper_method(roster_file_path)
        return yeet

    def make_float(self, list1):
        for item in list1:
            fun = len(item)
            for ex, why in enumerate(item):

                why = float(why)
                item.append(why)
                if len(item) == (fun * 2):
                    del item[:fun]
                    break

        return list1
    #
    # def make_dict(id, overall, test_average, project_average, quiz_average):
    #     # x, z = helper_method(roster_file_path)
    #     # id = z
    #     # overall = 'some set value'
    #     dict = {
    #         id: [overall, test_average, project_average, quiz_average]
    #     }
    #     pass

    def get_list(self, files, roster_file_path):

        ex, zee = self.helper_method(roster_file_path)

        list1 = []
        for lmao in ex:
            for item in files:
                grade = self.read_files(item, lmao)
                list1.append(grade)
        return list1

    def make_list(self, list, roster_file_path):
        test_grades = []
        new = []
        new2 = []
        new3 = []
        # pull each score from files according to name of student ID
        ex, zee = self.helper_method(roster_file_path)

        count = 0
        for name in ex:
            if len(test_grades) > 0:
                new.append(test_grades)
                test_grades = []
                count += 1
            for item in list:
                if len(item) == 0:
                    continue
                if item[0][0] == name:
                    test_grades.append([item[0][1]])
            if name == ex[-1]:
                new.append(test_grades)
        # create list of lists to math with the index of the list of names to perform appropriate calculations
        for item in new:

            if len(new2) > 0:
                new3.append(new2)
                new2 = []
            for cee in item:
                new2.append(cee[0])
                #print("new2", new2)
            if item == new[-1]:
                #print("LOL", new[-1])
                new3.append(new2)
                break
        #print("END",new3)
        return new3

            # for values in grade:
            #     test_grades.append(values)
            # print("test_grades", test_grades)
            # t_grade = grade
    #    grade = read_files(quiz_files)
        # with open(test_files, 'w') as file:
        #     new = file.readlines()
        #
        #     for line in new:
        #         for item in list1:
        #             if item in line:
        #                 list2.append(item)


        # THINK FIRST
        #  * What do you need to do?
        #  * What can you use from prior weeks?
        #  * How to organize the data you get?
        #  * What tools (or packages) can simplify your life?
        #  * What helper methods would it be useful for you to write?
        #      That is what operations are repeated, and could be wrapped
        #      by a method instead of copying code?

    def read_files(self, path, name):
        grade = []

        with open(path, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            for line in reader:
                if len(line) == 0:
                    continue
                if line[0] == name:
                    grade.append((name, line[1]))
        return grade

    def helper_method(self, roster_file_path):

        list_of_ids = []
        with open(roster_file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            count = 0
            for line in reader:
                if len(line) == 0:
                    continue
                else:
                    count += 1
                    list_of_ids.append(line[2])

        return list_of_ids, count


if __name__ == '__main__':

    size = "short" #"big"
    test_files = [os.path.join("SampleData", "T_{}_{}.csv".format(size, i)) for i in range(3)]
    project_files = [os.path.join("SampleData", "P_{}_{}.csv".format(size, i)) for i in range(3)]
    quiz_files = [os.path.join("SampleData", "Q_{}_{}.csv".format(size, i)) for i in range(5)]
    roster_file_path = os.path.join("SampleData", "{}_roster.csv".format(size))
    Gradebook2(os.path.join("SampleData", "grade book"), roster_file_path, test_files, project_files, quiz_files)
    grade_book_path = os.path.join("SampleData", "grade_book_{}.csv".format(size))

    # size = "big" #"short"  #
    # test_files = [os.path.join("SampleData", "T_{}_{}.csv".format(size, i)) for i in range(3)]
    # project_files = [os.path.join("SampleData", "P_{}_{}.csv".format(size, i)) for i in range(4)]
    # quiz_files = [os.path.join("SampleData", "Q_{}_{}.csv".format(size, i)) for i in range(6)]
    # roster_file_path = os.path.join("SampleData", "{}_roster.csv".format(size))
    # generate_grade_book(os.path.join("SampleData", "grade book"), roster_file_path, test_files, project_files, quiz_files)

    num = Gradebook2(grade_book_path, roster_file_path, test_files, project_files, quiz_files)
    print("Wrote grade book for", num.count(roster_file_path), "students to", grade_book_path)
