import pandas as pd


student_df = pd.read_csv('student.csv')

filtered_df = student_df[(student_df["studytime"] >= 3) & (student_df["internet"] == 1) & (student_df["absences"] <= 5)]
print("Filtered DataFrame")

filtered_df.to_csv('filtered_students.csv', index=False)
print("Writing to file complete... filtered_students.csv created")

average_grade_filtered = filtered_df["grade"].mean()
amount_of_students_filtered = len(filtered_df)
print(f"Average grade of filtered students: {average_grade_filtered}")
print(f"Number of filtered students: {amount_of_students_filtered}")
