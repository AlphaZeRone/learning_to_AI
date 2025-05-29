import pandas as pd

data = {
    'Name': ['Nut', 'Mild', 'Pun'],
    'Age': [22, 25, 58],
    'City': ['Bangkok', 'Udonthani', 'Bangkok']
}

df = pd.DataFrame(data)

df['Salary'] = [10000, 20000, 30000]

print(df)
print('--------------------------------')
print(df.loc[1:2, ['Name', 'Age']])
print('--------------------------------')
print(df[df['Age'] > 25])
print('--------------------------------')

grouped = df.groupby('City')['Salary'].mean()
print(grouped)
print('--------------------------------')

emp_csv = pd.read_csv('employee.csv')
print(emp_csv)
print('--------------------------------')
emp_Sort = (emp_csv[emp_csv['Salary'] > 30000])
emp_Sort.to_csv('new_employee.csv', index=False)

