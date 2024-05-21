import pandas as pd

# Sample data
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8],
    'quest': [
        'Solve for x: 15x = 75',
        'Solve for x: 5x - 2 = 13',
        'Solve for x: 4x + 6 = 18',
        'Solve for x: 6x = 42',
        'Solve for x: 3x + 5 = 14',
        'Solve for x: 6x - 9 = 15',
        'Solve for x: 4x + 5 = 2x + 11',
        'Solve for x: 6x + 3 = 4x + 9',
        ],
    'op1': [3, 1, 1, 6, 2, 2, 1, 2],
    'op2': [5, 2, 2, 7, 3, 3, 2, 3],
    'op3': [6, 3, 3, 8, 4, 4, 3, 4],
    'op4': [10, 4, 4, 12, 5, 5, 4, 5],
    'ans': [5, 3, 3, 7, 3, 4, 3, 3]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel('new_problems_Problems.xlsx', index=False)

print("Excel file 'new_problems_Problems.xlsx' created successfully.")