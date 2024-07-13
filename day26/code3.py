student_dict = {
        "student" : ["Angela","James", "Lily"],
        "score" : [56, 78, 94 ]
        }

import pandas

student_data_frame = pandas.DataFrame(student_dict)

#print(student_data_frame)

# loop through DataFrame...
#for key,value in student_data_frame.items():
#    print(value)

# Loop through row of data frame..
for (index,row) in student_data_frame.iterrows():
    print(row.student)
