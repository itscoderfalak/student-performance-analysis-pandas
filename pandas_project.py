import pandas as pd
import numpy as np

# -------------------------
# Step 1: Create dataset (basic)
# -------------------------
data = {
    'Name': ['Ali', 'Sara', 'Zara', 'Bilal', 'Taseer', 'Aisha', 'Hassan', 'Maria'],
    'Age': [18, 17, 18, 16, 17, 16, 17, 16],
    'Class': [12, 12, 12, 11, 12, 11, 11, 12],
    'Math Marks': [85, 92, 78, 92, 88, 75, 80, 95],
    'Science Marks': [80, 89, 85, 95, 90, 82, 88, 93],
    'English Marks': [90, 87, 88, 90, 85, 80, 84, 91],
    'Study Hours per Week': [12, 15, 10, 16, 14, 8, 9, 18],
    'Sports': ['Football', 'Basketball', 'Tennis', 'Cricket', 'Football', 'Tennis', 'Cricket', 'Basketball']
}

df = pd.DataFrame(data)

# -------------------------
# Step 2: Basic Exploration
# -------------------------
print("First 5 rows:")
print(df.head(), "\n")

print("Info and summary statistics:")
print(df.info(), "\n")
print(df.describe(), "\n")

# -------------------------
# Step 3: Basic Cleaning
# -------------------------
# Check missing values
print("Missing values:\n", df.isnull().sum(), "\n")

# Fill missing numeric values with mean (advanced basic)
df.fillna(df.mean(numeric_only=True), inplace=True)

# -------------------------
# Step 4: Basic Analysis
# -------------------------
# Average marks per subject
avg_marks = df[['Math Marks','Science Marks','English Marks']].mean()
print("Average marks per subject:\n", avg_marks, "\n")

# Total and average marks per student
df['Total Marks'] = df[['Math Marks','Science Marks','English Marks']].sum(axis=1)
df['Average Marks'] = df[['Math Marks','Science Marks','English Marks']].mean(axis=1)

# Top performer
top_student = df.loc[df['Total Marks'].idxmax()]
print(f"Top performer: {top_student['Name']} with {top_student['Total Marks']} marks\n")

# -------------------------
# Step 5: Intermediate Analysis
# -------------------------
# Sorting
print("Students sorted by Total Marks descending:\n", df.sort_values('Total Marks', ascending=False)[['Name','Total Marks']], "\n")

# Filtering: Students scoring >85 in all subjects
high_achievers = df[(df['Math Marks']>85) & (df['Science Marks']>85) & (df['English Marks']>85)]
print("High achievers (>85 in all subjects):\n", high_achievers[['Name','Math Marks','Science Marks','English Marks']], "\n")

# Grouping: Average marks by Class
avg_by_class = df.groupby('Class')[['Math Marks','Science Marks','English Marks']].mean()
print("Average marks by Class:\n", avg_by_class, "\n")

# Conditional column: Performance
df['Performance'] = np.where(df['Average Marks']>=90,'Excellent',
                             np.where(df['Average Marks']>=80,'Good','Average'))
print("Data with Performance column:\n", df[['Name','Average Marks','Performance']], "\n")

# -------------------------
# Step 6: Advanced Analysis
# -------------------------
# Ranking students by Total Marks
df['Rank'] = df['Total Marks'].rank(ascending=False, method='dense').astype(int)
print("Students with Rank:\n", df[['Name','Total Marks','Rank']], "\n")

# Pivot Table: Average marks by Class and Sport
pivot_table = pd.pivot_table(df, values=['Math Marks','Science Marks','English Marks'],
                             index='Class', columns='Sports', aggfunc='mean', fill_value=0)
print("Pivot Table: Average Marks by Class and Sport:\n", pivot_table, "\n")

# Apply function: Bonus marks for Math >90
df['Math Bonus'] = df['Math Marks'].apply(lambda x: 5 if x>90 else 0)
print("Data with Math Bonus:\n", df[['Name','Math Marks','Math Bonus']], "\n")

# Advanced filtering: Students in Class 12 with Total Marks >= 250
class12_top = df.query('Class==12 & `Total Marks`>=250')
print("Class 12 students with Total Marks >=250:\n", class12_top[['Name','Total Marks']], "\n")

# -------------------------
# Step 7: Save final dataset
# -------------------------
df.to_csv('student_analysis.csv', index=False)
print("Project complete! Dataset saved as 'student_analysis.csv'")
