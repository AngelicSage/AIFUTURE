import pandas as pd

# Sample data
data = {
    'id': [1, 2, 3],
    'quest': ['What is 2 + 2?', 'What is the square root of 16?', 'What is 10 / 2?'],
    'op1': [3, 2, 3],
    'op2': [4, 3, 4],
    'op3': [5, 4, 5],
    'op4': [6, 5, 6],
    'ans': [2, 3, 3]
}
# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel('new_problems_Problems.xlsx', index=False)

print("Excel file 'new_problems_Problems.xlsx' created successfully.")