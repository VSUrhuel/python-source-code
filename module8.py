# Import necessary libraries
import pandas as pd
import re

# Load the data from the CSV file
df = pd.read_csv('ipes.csv')

# Convert column names to lowercase and replace non-alphanumeric characters with underscores
df.columns = [re.sub(r'[^a-zA-Z0-9_]', '_', col.lower()) for col in df.columns]

# Aggregate by 'faculty', 'course', and 'item'
agg_data = df.groupby(['faculty', 'course', 'item', 'rating']).size().unstack(fill_value=0)

# Calculate the Mean for each item
agg_data['mean'] = agg_data.apply(lambda row: sum(row * row.index) / sum(row) if sum(row) > 0 else 0, axis=1)

# Display the first table
print('=' * 60)
print(f"{'Item':>15}{'1':>7}{'2':>7}{'3':>7}{'4':>7}{'5':>7}{'Mean':>8}")
print('-' * 60)

# Reset the index of agg_data
agg_data_reset = agg_data.reset_index()

# Initialize variables for current faculty and course
current_faculty = None
current_course = None

# Loop through aggregated data and print tables
for index, row in agg_data_reset.iterrows():
    if row['faculty'] != current_faculty:
        if current_faculty is not None:
            print('=' * 60)
        print(f"Instructor :    {int(row['faculty'])}")
        current_faculty = row['faculty']
        current_course = None  # Reset current_course when changing instructor
    if row['course'] != current_course:
        if current_course is not None:
            print('-' * 60)  # Add dashes between different courses
        print(f"    Course :    {int(row['course'])}")
        print()
        current_course = row['course']

    print(f"{int(row['item']):>15}  |{int(row[1]): >5}{int(row[2]): >7}{int(row[3]): >7}{int(row[4]): >7}{int(row[5]): >7}{row['mean']:>7.2f}")

# Display the table for "Rating Summary by Faculty and Course"
print()
print('~' * 60)
print("Rating Summary by Faculty and Course")
print('=' * 60)

# Aggregate by 'faculty' and 'course' with Mean and Median of 'rating'
summary_data = df.groupby(['faculty', 'course']).agg(
    mean_rating=('rating', 'mean'),
    median_rating=('rating', 'median')).reset_index()

# Print the summary table
print(f"{'Faculty':<5}{'Course':>13}{'Mean':>9}{'Median':>13}")
print('-' * 60)

for index, row in summary_data.iterrows():
    print(
        f"{int(row['faculty']):>5}    - {int(row['course']):>8}{row['mean_rating']:>10.2f}{row['median_rating']:>12.2f}")
