import pandas as pd

df = pd.read_csv('student.csv')

# Create grade_band column
def assign_grade_band(grade):
    if grade <= 9:
        return 'Low'
    elif grade <= 14:
        return 'Medium'
    else:
        return 'High'

df['grade_band'] = df['grade'].apply(assign_grade_band)

# Create grouped summary table
summary = df.groupby('grade_band').agg(
    number_of_students=('grade_band', 'size'),
    average_absences=('absences', 'mean'),
    internet_access_percentage=('internet', lambda x: (x.sum() / len(x)) * 100)
).reset_index()


summary['grade_band'] = pd.Categorical(summary['grade_band'], 
                                        categories=['Low', 'Medium', 'High'], 
                                        ordered=True)
summary = summary.sort_values('grade_band').reset_index(drop=True)

# Save to CSV
summary.to_csv('student_bands.csv', index=False)

print(summary)