import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips.head())

# matplotlib.pyplot을 이용한 시각화(visualization)
# Figure 객체 생성
fig = plt.figure()
print(fig)

# Subplot 생성
axis = fig.add_subplot(1, 1, 1)
print(axis)

# histogram
axis.hist(x=tips['total_bill'], bins=20)

# 그래프 설정(options)
axis.set_title('Histogram of Total Bill')
axis.set_ylabel('# of total bill')
axis.set_xlabel('total bill')

# 그래프 보여주기
plt.show()

# Figure 생성 & Subplot 생성
# fig = plt.figure()
# axis = fig.add_subplot(1, 1, 1)
fig, ax = plt.subplots(nrows=1, ncols=1)
print('Figure:', fig)
print('Subplots:', ax)

ax.hist(x=tips['total_bill'])
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.hist(x=tips['total_bill'], bins=20)
ax1.set_title('Histogram of total bill')
ax1.set_xlabel('Total bill')
ax1.set_ylabel('# of total bill')

ax2.scatter(x=tips['total_bill'], y=tips['tip'])
ax2.set_title('Scatter plot(total bill vs tip)')
ax2.set_xlabel('Total bill')
ax2.set_ylabel('Tip')

plt.show()

# Figure & Subplot 생성
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].hist(x=tips['total_bill'])
ax[1].scatter(x=tips['total_bill'], y=tips['tip'])
ax[1].set_xlabel('total bill')
ax[1].set_ylabel('tip')
plt.show()

# histogram, scatter plot을 위/아래로 배치
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.hist(x=tips['total_bill'])
ax2.scatter(x=tips['total_bill'], y=tips['tip'])

plt.show()

fig, ax = plt.subplots(nrows=2, ncols=1)
ax[0].hist(x=tips['total_bill'])
ax[1].scatter(x=tips['total_bill'], y=tips['tip'])
plt.show()

# Figure에 Plot을 하나만 그릴 경우,
# matplotlib.pyplot 모듈의 top-level 함수들만 사용해도 됨.
plt.hist(x=tips['total_bill'])
plt.title('Histogram')
plt.xlabel('total bill')
plt.ylabel('# of total bill')
plt.show()




