import pandas as pd
import numpy as np
data = pd.read_csv("Employees.csv")
# data set
print(data)

# converting to numpy array
monthly_salary=np.array(data["Monthly Salary"])
# print(monthly_salary)

# find the mean of monthly salary
mean = monthly_salary.mean()
print("mean of monthly salary = ",round(mean))

# find the mean of Annual Salary
Annual_Salary = np.array(data["Annual Salary"])
mean1= Annual_Salary.mean()
print("mean of Annual Salary = ", round(mean1))

#find the mean of Job Rate
Job_Rate=np.array(data["Job Rate"])
mean2=Job_Rate.mean()
print("mean of Job Rate =",round(mean2))

# find the median
median = data["Monthly Salary"].median()
print("median of Monthly Salary = ",median)

median1 = data["Annual Salary"].median()
print("meadian of annual Salary", median1)

# find the mode
mode = data["Monthly Salary"].mode()
print("mode of Monthly Salary = ",mode)

mode1 = data["Annual Salary"].mode()
print("mode of annunal salary = " ,mode1)

# find the standar deviation
print("standar deviation of monthly salary = " , monthly_salary.std())
print("standar deviation of annuly salary = ", Annual_Salary.std())

