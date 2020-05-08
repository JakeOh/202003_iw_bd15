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
sns.pairplot(data=iris, hue='species')
plt.show()

print(iris.index)  # DataFrame, Series의 인덱스(row label)
vars = iris.columns[:4]
n_vars = len(vars)
print(vars, n_vars)

fig, ax = plt.subplots(nrows=n_vars, ncols=n_vars)
for i in range(n_vars):  # 0 <= i < 4
    for j in range(n_vars):  # 0 <= j < 4
        if i == j:  # 히스토그램 또는 KDE Plot을 그림
            sns.kdeplot(data=iris[iris['species'] == 'setosa'][vars[i]],
                        shade=True, ax=ax[i][j], legend=False)
            sns.kdeplot(data=iris[iris['species'] == 'versicolor'][vars[i]],
                        shade=True, ax=ax[i][j], legend=False)
            sns.kdeplot(data=iris[iris['species'] == 'virginica'][vars[i]],
                        shade=True, ax=ax[i][j], legend=False)
        else:  # scatter plot을 그림
            sns.scatterplot(x=vars[j], y=vars[i], hue='species',
                            data=iris, ax=ax[i][j], legend=False)
        if j == 0:
            ax[i][j].set_ylabel(vars[i])
        else:
            ax[i][j].set_ylabel(None)
plt.show()
