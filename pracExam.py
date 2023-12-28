# Import necessary libraries
import pandas as pd
import re

# Load the data from the CSV file
df = pd.read_csv('ipes.csv')

# Convert column names to lowercase and replace non-alphanumeric characters with underscores
df.columns = [re.sub(r'[^a-zA-Z0-9_]', '_', col.lower()) for col in df.columns]

# Aggregate by 'faculty', 'item', and 'rating'
agg_data = df.groupby(['faculty', 'item', 'rating']).size().unstack(fill_value=0)

# Calculate mean for each item
agg_data['mean'] = agg_data.apply(lambda row: sum(row * row.index) / sum(row) if sum(row) > 0 else 0, axis=1)

# Display the first row
print('=' * 47)
print(f"{'Item':>15}{'1':>4}{'2':>4}{'3':>4}{'4':>4}{'5':>4}{'Mean':>5}{'Median':>7}")
print('-' * 47)

# Reset the index of agg_data
agg_data_reset = agg_data.reset_index()

# Initialize variables for current faculty
current_faculty = None

# Loop through aggregated data and print tables
for index, row in agg_data_reset.iterrows():
    if row['faculty'] != current_faculty:
        if current_faculty is not None:
            print()
        print(f"Instructor :     {int(row['faculty'])}")
        current_faculty = row['faculty']

    # Caculating Median Algorithm
    values = [int(row[col]) for col in range(1, 6)]
    even = False
    sum_values = sum(values)

    if sum_values % 2 == 0:
        even = True
        n = sum_values // 2
    else:
        n = (sum_values // 2) + 1

    k = 1
    sum2 = 0

    while k < 6:
        sum2 = sum2 + int(row[k])

        if sum2 < n:
            k = k + 1
        else:
            if sum2 > n:
                median = k
            elif even:
                median = (2 * k + 1) // 2
            else:
                median = k

            break

    print(f"{int(row['item']):>15} |{int(row[1]): >3}{int(row[2]): >3}{int(row[3]): >4}{int(row[4]): >4}{int(row[5]): >4}{row['mean']:>5.2f}{median:>6.2f}")