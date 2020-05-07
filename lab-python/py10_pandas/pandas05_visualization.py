import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 선 그래프(plot)
data = np.random.rand(10)
print(data)

fig, ax = plt.subplots()
# ax.plot(data, 'ko--')
ax.plot(data, color='aqua', marker='x', linestyle='dotted')
# color: 색깔 이름(black, red, green, ...), #RGB(#000000, #FF0000, ...)

ax.set_title('Line Graph')
plt.show()

plt.plot(data, 'bo:')
plt.title('Line Graph 2')
plt.show()

x_pts = np.arange(0, 100, 10)
plt.plot(x_pts, data)
plt.xticks(np.arange(0, 100, 10))
plt.yticks(np.arange(0, 1, 0.1))
plt.show()

fig, ax = plt.subplots()
ax.plot(x_pts, data)
ax.set_xticks(np.arange(0, 100, 5))
ax.set_yticks(np.arange(0, 1, 0.05))
plt.show()

# label & legend (범례)
y1 = np.random.rand(10)
y2 = np.random.rand(10)
y3 = np.random.rand(10)

plt.plot(y1, color='red', linestyle='dotted', label='One')
plt.plot(y2, color='green',linestyle='dashed', label='Two')
plt.plot(y3, color='blue', label='Three')

plt.legend(loc='best')
plt.show()

fig, ax = plt.subplots()
ax.plot(y1, c='red', ls='dotted', label='One')
ax.plot(y2, c='green', ls='dashed', label='Two')
ax.plot(y3, c='blue', label='Three')

ax.legend()
# plt.legend()

plt.show()

# boxplot
tips = sns.load_dataset('tips')

plt.boxplot(x=tips['tip'], labels=['tip'])
plt.title('Boxplot of tip')
plt.show()

fig, ax = plt.subplots()
ax.boxplot(x=tips['total_bill'], labels=['total bill'])
ax.set_title('Boxplot of total bill')
plt.show()

# 성별 tip의 boxplot을 하나의 subplot에 그림.
tip_male = tips[tips['sex'] == 'Male']['tip']
tip_female = tips[tips['sex'] == 'Female']['tip']

plt.boxplot(x=[tip_male, tip_female],
            labels=['Male', 'Female'])
plt.show()
