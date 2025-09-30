'''
SOLUTIONS FOR CLASS 3 EXERCISES
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Load datasets
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

# 1
plt.plot([1,3,2,4])
plt.show()

# 2
plt.plot([1,3,2,4], marker='o')
plt.show()

# 3
plt.bar(["A","B","C","D"], [4,7,2,9])
plt.show()

# 4
data = np.random.randn(100)
plt.hist(data)
plt.show()

# 5
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,100,86,103,87,94,78,77,85,86]
plt.scatter(x,y)
plt.show()

# 6
plt.scatter(x,y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot Example")
plt.show()

# 7
fig, ax = plt.subplots(1,2, figsize=(10,4))
ax[0].plot([3,8,1,10])
ax[1].bar(["A","B","C","D"], [3,8,1,10])
plt.show()

# 8
sns.histplot(data=tips, x="total_bill")
plt.show()

# 9
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.show()

# 10
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.show()

# 11
sns.boxplot(data=tips, x="day", y="total_bill")
plt.show()

# 12
sns.violinplot(data=tips, x="day", y="tip", hue="sex", split=True)
plt.show()

# 13
sns.pairplot(tips, hue="time")
plt.show()

# 14
y1 = [3,8,1,10]
y2 = [6,2,7,11]
plt.plot(y1, label="Series 1")
plt.plot(y2, label="Series 2")
plt.legend()
plt.show()

# 15
plt.bar(["A","B","C"], [5,6,7])
plt.savefig("barplot.png")
plt.close()

# 16
sns.barplot(data=tips, x="day", y="tip", estimator=np.mean)
plt.show()

# 17
sns.lineplot(data=tips, x="size", y="tip", hue="sex")
plt.show()

# 18
sns.histplot(data=tips, x="total_bill")
plt.title("Tips Distribution")
plt.show()

# 19
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species")
plt.show()

# 20
sns.pairplot(iris, hue="species")
plt.savefig("iris_pairplot.png")
plt.close()
