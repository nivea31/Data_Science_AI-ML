import pandas as pd
from matplotlib import pyplot as plt

# Task 1: Read the employee dataset from a CSV file:
df=pd.read_csv("employee_data_large.csv")
print(df)

# Task 2: Add a new column Bonus where the bonus is 10% of the salary if the employee has more than 5 years of experience, otherwise 5%.
df["Bonus"]=df["Salary"]*0.10
df.loc[df["Experience"]<=5,"Bonus"]=df["Salary"]*0.05
print(df)

# Task 3: Find the average salary for each department and compare it with the overall company average salary.
dep_avgsal=df.groupby("Department")["Salary"].mean()
print("Average salary for each department",dep_avgsal)
compare_sal=df["Salary"].mean()
print("Comparision of both",compare_sal)

# Task 4: Identify the employee with the highest salary and the lowest salary in each department.
highest_sal=df.groupby("Department")["Salary"].max()
print("Highest Salary",highest_sal)
lowest_sal=df.groupby("Department")["Salary"].min()
print("Lowest Salary",lowest_sal)

# Task 5: Create a new column Salary after Tax assuming a tax deduction of 12% from the Salary, and rank employees based on their post-tax salary.
df["Salary_after_tax"]=df["Salary"]*0.88
print(df)
df["Rank"]=df["Salary_after_tax"].rank()
print(df)

# Task 6: Sort the employees by experience in descending order and filter the top 3 most experienced employees.
sort_employee=df.sort_values("Experience",ascending=False).head(3)
print(sort_employee)

# Task 7: Count the number of employees in each department and visualize this using a bar chart.
count=df["Department"].value_counts()
print(count)
department = list(df["Department"].unique())
#print(department)
count = list(count)
#print(count)
plt.bar(department,count)
#plt.show()

# Task 8: Find the department with the highest average experience and the lowest average experience.
highest_avg=df.groupby("Department")["Experience"].mean().idxmax()
print(highest_avg)
lowest_avg=df.groupby("Department")["Experience"].mean().idxmin()
print(lowest_avg)

# Task 9: Identify employees earning above the department average salary and display only their names and salaries.
employee=df.groupby("Department")["Salary"].mean()
x=df[df["Salary"]>df["Department"].map(employee)][["Employee","Salary"]]
print(x)

# Task 10: Create a pivot table summarizing the total salary, average experience, and total bonus per department.
total_salary=df.groupby("Department")["Salary"].sum()
print(total_salary)
average_experience=df.groupby("Department")["Experience"].mean()
print(average_experience)
total_bonus=df.groupby("Department")["Bonus"].sum()
print(total_bonus)
pivot_table=pd.DataFrame({"Total_Salary":total_salary,"Average_Experience":average_experience,"Total_Bonus":total_bonus},index=df["Department"].unique())
print(pivot_table)