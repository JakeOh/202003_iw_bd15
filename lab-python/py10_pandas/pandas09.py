import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris)
print(iris.describe())
print(iris['species'].describe())
print(iris['species'].value_counts())

sns.boxplot(data=iris)
plt.show()

# seaborn 패키지의 함수 catplot()함수를 사용
# species별로 column을 구분
# sl, sw, pl, pw의 box plot
sns.catplot(data=iris, col='species', kind='box')
plt.show()

# pairplot
# sns.pairplot(data=iris, hue='species')
# plt.show()

vars = iris.columns[:4]
n_vars = len(vars)
print(vars, n_vars)

fig, ax = plt.subplots(nrows=n_vars, ncols=n_vars)
for i in range(n_vars):
    for j in range(n_vars):
        pass
