import csv
import os
import numpy as np


def generate_assignment_data(expected_grade_file_path,
                             std_dev, output_file_path):
    """
    Retrieve list of students and their expected grade from file,
    generate a sampled test grade for each student
    drawn from a Gaussian distribution defined by the
    student expected grade as mean, and the given
    standard deviation.

    If the sample is higher than 100, re-sample.
    If the sample is lower than 0 or 5 standard deviations below mean,
    re-sample

    Write the list of student grades to the given
    output file using ID and grade with TAB separation.

    :param expected_grade_file_path: This is our file of student IDs and expected grades
    :param std_dev: Standard deviation used when sampling grades
    :param output_file_path: Where to write the sample grades
    :return: number of student grades generated and
            tuple of mean, median and standard deviation of grades
    """

    #creating new grades based on grades that make_roster generated each
    # student grade as mean, to create random value based on grade as mean

    list_of_data, list_of_grades, count = helper_method(expected_grade_file_path)
    list2 = []
    list4 = []
    count2 = 0
    list_of_grades = list_of_grades.astype('float64')
    #for every iteration in list_of_grades(grades pulled from make roster), create a 1 item np array that has mean
    #grade pulled from make_roster list and given stdv. Filter that value through the appropriate expectations.
    #append value to a list
    while len(list2) < len(list_of_grades):
        # nplist = np.random.normal(list_of_grades, std_dev, len(list_of_grades))
        # nplist = nplist[nplist < 100]
        # nplist = nplist[nplist > 0.0]
        # print(len(nplist))
        # if len(nplist) == len(list_of_grades):
        #     nplist = nplist[nplist > (list_of_grades - 5 * std_dev)]
        #     print('sigma', len(nplist))
        #     if len(nplist) == len(list_of_grades):
        #         print(nplist)
        #         nplist = nplist.astype(float)
        #         for i, j in enumerate(nplist):
        #             list2.append(j)
        for itemz, joke in enumerate(list_of_grades):
            while count2 == itemz:
                nplist = np.random.normal(float(joke), std_dev, 1)
                nplist = nplist[nplist < 100]
                nplist = nplist[nplist > 0.0]
                print("zero", len(nplist))
                print(joke)
                print(nplist)
                print(float(joke) - 5 * std_dev)
                nplist = nplist[nplist - 5 * std_dev > float(joke) - 5 * std_dev]
                print("sigma", len(nplist))
                if len(nplist) != 0:
                    #print('item', nplist.item(0))
                    #print('stdv', (float(j)-5*std_dev))
                    #print(nplist.item(0) > (float(j) - 5 * std_dev))
                    list2.append(nplist.item(0))
                    count2 += 1
    with open(output_file_path, 'w') as file:
        writer = csv.writer(file, delimiter='\t')
        for itey in list_of_data:
            new = itey.split('\t')
            del new[1]
            list4.append(new)
        cont = 0
        for item in list4:
            if cont < (len(list2)):
                item.append(list2[cont])
            cont += 1
        for item in list4:
            writer.writerow(item)

        # for id in list_of_data:
        #     data = id.split('\t')
        #     print(data[0])
        #     print('data is', data)
        #     writer.writerow(data[0] + str(list3[id_num]) + '\n')
        #     id_num += 1
    #np actually very versitile! got mean/ median/ stdv of a list of one dimensional single value numpy arrays
    mean = np.mean(list2)
    median = np.median(list2)
    std_dev = np.std(list2)
    return count, mean, median, std_dev


def helper_method(expected_grade_file_path):
    list_of_data = []
    list_of_grades = []
    count = 0
    with open(expected_grade_file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for line in reader:
            if len(line) == 0:
                continue
            else:
                list_of_data.append(line[0] + '\t' + line[1])
                list_of_grades.append(line[1])
                count += 1
        list_of_grades = np.array(list_of_grades)
    return list_of_data, list_of_grades, count

def generate_multiple_files(ex_path, std_dev, num, folder, prefix):
    #
    count_files = 0
    total = 0
    for item in range(num):
        name = "{}_{}.csv".format(prefix, item)
        count, _, _, _ = generate_assignment_data(ex_path, std_dev, os.path.join(folder, name))
        count_files += 1
        total += count
    return count_files, total


def generate_test_data_files(expected_grade_file_path, std_dev, num_tests, folder_path):
    """
    For given student expected grades, generate the grades as
    described in generate_assignment_data given std_dev.

    For this method, you will generate multiple files for each tests.
    For example, if num_tests = 4, then you should generate four files
    according to the following naming convention:
    "T_0.csv" ... "T_3.csv" .  The files should be written in the folder
    defined by folder_path.

    For example, given num_tests = 1 and folder_path="data", you should
    create one file of test grades in "data/T_0.csv"

    You should be making use of the generate_assignment_data method above!

    :param expect: This is our file of student IDs and expected grades
    :param std_dev: Standard deviation used when sampling grades
    :param num_tests: Number of test files to generate
    :param folder_path: location of the output files.
    :return: Total number of grade samples written to test files
    """

    total = generate_multiple_files(expected_grade_file_path, std_dev, num_tests, folder_path, 'T')

    return total


def generate_quiz_data_files(expected_grade_file_path, std_dev, num_quizzes, folder_path):
    """
    For given student expected grades, generate the grades as
    described in generate_assignment_data given std_dev.

    For this method, you will generate multiple files for each quiz.
    For example, if num_quizzes = 4, then you should generate four files
    according to the following naming convention:
    "Q_0.csv" ... "Q_3.csv" .  The files should be written in the folder
    defined by folder_path.

    For example, given num_quizzes = 1 and folder_path="data", you should
    create one file of test grades in "data/Q_0.csv"

    You should be making use of the generate_assignment_data method above!

    :param expected_grade_file_path: This is our file of student IDs and expected grades
    :param std_dev: Standard deviation used when sampling grades
    :param num_quizzes: Number of quiz files to generate
    :param folder_path: location of the output files.
    :return: Total number of grade samples written to quiz files
    """
    total = generate_multiple_files(expected_grade_file_path, std_dev, num_quizzes, folder_path, 'Q')

    return total


def generate_project_data_files(expected_grade_file_path, std_dev, num_projects, folder_path):
    """
    For given student expected grades, generate the grades as
    described in generate_assignment_data given std_dev.

    For this method, you will generate multiple files for each project.
    For example, if num_projects = 4, then you should generate four files
    according to the following naming convention:
    "P_0.csv" ... "P_3.csv" .  The files should be written in the folder
    defined by folder_path.

    For example, given num_projects = 1 and folder_path="data", you should
    create one file of test grades in "data/P_0.csv"

    You should be making use of the generate_assignment_data method above!

    :param expected_grade_file_path: This is our file of student IDs and expected grades
    :param std_dev: Standard deviation used when sampling grades
    :param num_projects: Number of project files to generate
    :param folder_path: location of the output files.
    :return: Total number of grade samples written to all project files
    """
    total = generate_multiple_files(expected_grade_file_path, std_dev, num_projects, folder_path, 'P')

    return total


if __name__ == '__main__':


    print("fuck you_______________________________________________________________________________")
    #generate_multiple_files(os.path.join('data', 'short_expected.csv'), 1, 1,
     #                       os.path.join("data", "assignment_grades.csv"), "lol")

    import make_roster
    NUM_STUDENTS = make_roster.generate_roster(
                            os.path.join("SampleData", "short_names.txt"),
                            os.path.join("SampleData", "short_roster.csv"))

    print("Generated ", NUM_STUDENTS, " IDs in roster")
    MEDIAN, MEAN, STD_DEV = make_roster.generate_expected_grades(
                                    os.path.join("SampleData", "short_roster.csv"),
                                    os.path.join("SampleData", "short_expected.csv"),
                                                     78.0, 10.0)
    print("Calculated median={} mean={} s.d.={}".format(MEDIAN, MEAN, STD_DEV))


    COUNT, MEDIAN_TEST, MEAN_TEST, STD_TEST = generate_assignment_data(os.path.join("SampleData", "short_expected.csv"),
                                                                         15.,
                                                                         os.path.join("SampleData", "short_test.csv"))

    print("Test median={} mean={} s.d.={}".format(MEDIAN_TEST, MEAN_TEST, STD_TEST))
    print("  {} {} {}".format(COUNT, NUM_STUDENTS, COUNT == NUM_STUDENTS))

    TOTAL = generate_test_data_files(os.path.join("SampleData", "short_expected.csv"),
                                    15.0, 3, "SampleData")
    print("Total test grades =", TOTAL)

    TOTAL = generate_quiz_data_files(os.path.join("SampleData", "short_expected.csv"),
                                    1.0, 4, "SampleData")
    print("Total quiz grades =", TOTAL)

    TOTAL = generate_project_data_files(os.path.join("SampleData", "short_expected.csv"),
                                    15.0, 2, "SampleData")
    print("Total project grades =", TOTAL)