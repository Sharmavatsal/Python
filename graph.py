import calendar
import random
import matplotlib.pyplot as plt

month=calendar.month_name[1:13]
salary=random.sample(range(10000,80000),12)
tax=random.sample(range(5000,20000),12)
perks=random.sample(range(3000,15000),12)
plt.plot(month,salary,tax)
print("Tax : ",tax)

plt.figure(figsize=(15,10))
plt.bar(month,salary,color="red")
plt.plot(month,salary,color="black",marker='o', linestyle=':')# marker keeps the small markers on top of bar of graph
plt.xlabel('MONTH')
plt.ylabel('SALARY')
plt.grid()
plt.show



# practice of above exercise

import calendar
import random
import matplotlib.pyplot as plt

