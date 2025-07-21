# python sequence: list, range, string, tuple
# new_list=[new_item for item in list]
# conditional list comprehension to simplify loop
# new_list=[new_item for item in list if test]
# numbers=[1,2,3]
# new_nums=[n+1 for n in numbers]
# print(new_nums)
#
# name ="Joy"
# letters_list=[letter for letter in name]
# print(letters_list)
#
# range_list=[num*2 for num in range(1,5)]
# print(range_list)

names=['Alex',"Beth","Caroline","Alexander"]
# short_names=[name for name in names if len(name)<5]
# print(short_names)
# long_names=[name.upper() for name in names if len(name)>5]
# print(long_names)

# dictionary comprehension
import random
# {key:value for item in list}
# {new_key:new_value for (key,value) in list}
student_scores={student:random.randint(40,100) for student in names}
passed_students={student:score for (student,score) in student_scores.items() if score >=60}
# print(passed_students)

import pandas
student_dict={
    "student":["Amy","Hinata","Jurin"],
    "score":[99,98,89]
}
student_scores_dataframe=pandas.DataFrame(student_dict)
print(student_scores_dataframe)
# loop through a data frame
# for (key,value) in student_scores_dataframe.items():
    # print(f"{key}") #title of each column
    # print(f"{value}") # data of each column

# loop through rows of a data frame
for (index,row) in student_scores_dataframe.iterrows():
    # print(f"{index}") # index of each row
    print(f"{row.student}") # data of each row
    if row.student == "Amy":
        print(f"{row.student}'s score is {row.score}")