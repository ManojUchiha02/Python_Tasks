import pandas as pd
from datetime import datetime, timedelta

file_path = 'employee_attendance.xlsx'
df = pd.read_excel(file_path)

today = datetime.today().date()

previous_5_dates = [today - timedelta(days=i) for i in range(0, 7)]

today_wfh_column = None
today_wfo_column = None
for column in df.columns:
    if isinstance(column, datetime) and column.date() == today:
        today_wfh_column = column
        today_wfo_column = column
        break

previous_wfh_columns = []
previous_wfo_columns = []
for prev_date in previous_5_dates:
    for column in df.columns:
        if isinstance(column, datetime) and column.date() == prev_date:
            previous_wfh_columns.append(column)
            previous_wfo_columns.append(column)
            break

today_wfh_count = df[df[today_wfh_column] == 'WFH']['EmpId'].count()
today_wfo_count = df[df[today_wfo_column] == 'WFO']['EmpId'].count()

previous_wfh_count = df[df[previous_wfh_columns].apply(lambda row: 'WFH' in row.values, axis=1)]['EmpId'].count()
previous_wfo_count = df[df[previous_wfo_columns].apply(lambda row: 'WFO' in row.values, axis=1)]['EmpId'].count()

no_attendance = df[df[previous_wfh_columns + previous_wfo_columns].isnull().all(axis=1)]['EmpId']

print("WFH & WFO Count on Current Date:")
print("WFH Count:", today_wfh_count)
print("WFO Count:", today_wfo_count)

print("\nWFH & WFO Count for Previous 5 Days:")
print("WFH Count:", previous_wfh_count)
print("WFO Count:", previous_wfo_count)

print("\nEmployee IDs who have not filled attendance in today and previous 5 days:")
print(no_attendance.tolist())
