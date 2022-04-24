import numpy as np

"""
Generate roster of students given list of names and year

@author <Molly Dieter and Jake Brooks>
@version <09/30/2020>

"""
#pylint: disable=C0103


def generate_roster(name_file_path, roster_file_path, year=19):
    """
    Given a path to file with list of two names separated by space,
    a path to file for output roster, and year (default = 19),

    Get names from file at name_file_path, an create a new file at
    roster_file_path which is a TAB separated text file with:
    Last   First  ID
    on each line, where ID = first.last.year
    Use TAB to separate each item on line
    Ignore all lines that start with #

    :param name_file_path: relative path to file containing a list of names
    :param roster_file_path: relative path to file to hold the output roster
    :param year: year integer used to assign student IDs
    :return: number of students in roster
    """
    with open(name_file_path, 'rt') as file:
        lines = file.readlines()
        #print(lines)
    roster = []
    biglist = []
    for line in lines:
        line = line.strip()
        if line[0] == '#':
            continue
        else:
            line = line.split('\t')
            #print('line is', line)
            for char in line:
                names = char.split(' ')
                #print('names is', names)
                roster.append(names[0].lower() + '.' + names[1].lower() + '.' + str(year))
                biglist.append(names[1] + '\t' + names[0] + '\t' + roster[-1] + '\n')
        #print('bl is', biglist)
        #print(roster)
        with open(roster_file_path, 'wt') as file:
            for element in biglist:
                file.write(element)

    return len(roster)

def generate_expected_grades(roster_file_path, expected_grade_file_path,
                             class_mean, class_std_dev):
    """
    Given class roster file with contents (Last  First ID),
    generate a new file (using expected_grade_file_path name)
    that randomly assigns an expected grade to each student
    according to a Gaussian (normal) distribution of defined by
    class_mean and class_std_deviation

    The expected_grade_file_path file should contain the ID and expected
    grade as tab separated values.

    If the sample is higher than 100, re-sample.
    If the sample is lower than 0 or 5 standard deviations below mean,
    re-sample

    :param roster_file_path: file containing class roster
    :param expected_grade_file_path: output file containing ID and expected grade
    :param class_mean: ideal mean for the class samples
    :param class_std_deviation: ideal std_deviation for samples
    :return: calculated median, mean, std_dev for all samples
    """

    with open(roster_file_path, 'rt') as f:
        new = f.readlines()
#array is removing values against conditions when it should be "retesting" them
        listnp = np.array([0])
        if len(listnp) == 0:
            return 0, 0, 0

        while len(listnp) < len(new):
            print(len(listnp))
            listnp = np.random.normal(class_mean, class_std_dev, len(new))
            listnp = listnp[listnp < 100]
            listnp = listnp[listnp > 0.0]
            listnp = listnp[listnp > (class_mean-5*class_std_dev)]

    print("after if____________________________:")
    with open(expected_grade_file_path, 'wt') as p:
        for i in listnp:
            for line in new:
                lmao = line.split('\t')
                p.writelines(lmao[2].strip() + '\t' + str(i) + '\n')
                del new[0]
                break
    result = float(np.mean(listnp))
    result2 = float(np.median(listnp))
    result3 = float(np.std(listnp))
    #with open(expected_grade_file_path, 'wt') as f:
     #   f.write()
    #calculations incorrect?
    return result2, result, result3


"""
Simple output if you run as a script
"""
if __name__ == '__main__':

    import os
    num_students = generate_roster(os.path.join("SampleData", "data", "short_names.txt"),
                                   os.path.join("SampleData", "data", "short_roster.csv"))

    print("Generated ", num_students, " IDs in roster")
    median, mean, std_dev = generate_expected_grades(os.path.join("SampleData","data", "short_roster.csv"),
                                                     os.path.join("SampleData","data", "short_expected.csv"),
                                                     78.0, 10.0)
    print("Calculated median={} mean={} s.d.={}".format(median, mean, std_dev))
