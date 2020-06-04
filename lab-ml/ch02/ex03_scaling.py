import numpy as np
import pandas as pd

# 컬럼들마다 다른 scale을 맞추는 방법:
# 1) min_max 정규화(normalization):
#   모든 데이터를 0 ~ 1 사이의 값으로 변환
#   이상치에 민감.
# 2) 표준화(standardization)
#   데이터들의 평균이 0이고, 표준편차가 1이 되도록 변환
#   이상치에 민감하지 않음. 일부 알고리즘에서 사용할 수 없음.
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def min_max_normalize(data):
    """
    x_new = (x - min) / (max - min)

    :param data: Series, DataFrame
    :return: min-max 정규화가 된 Series, DataFrame
    """
    min, max = data.min(), data.max()
    return (data - min) / (max - min)


def standardize(data):
    """
    x_new = (x - mean) / std

    :param data: Series, DataFrame
    :return: 평균 0, 표준편차 1인 Series, DataFrame
    """
    mu, sigma = data.mean(), data.std()
    return (data - mu) / sigma


if __name__ == '__main__':
    np.random.seed(1)
    s = pd.Series(np.random.randint(10, size=5))
    print(s)

    mm = min_max_normalize(s)
    print(mm)

    # scikit-learn 패키지 MinMaxScaler 클래스 이용
    mm_scaler = MinMaxScaler()
    s_norm = mm_scaler.fit_transform(s.values.reshape((-1, 1)))
    print(s_norm)

    print('\n', '*' * 30, '\n')

    st = standardize(s)
    print(st)
    print(st.mean(), st.std())

    std_scaler = StandardScaler()
    print(std_scaler.fit_transform(s.values.reshape((-1, 1))))

    print('\n', '*' * 30, '\n')

    df = pd.DataFrame(np.random.randint(10, size=(5, 2)),
                      columns=['income', 'house'])
    print(df)

    print(min_max_normalize(df))
    print(mm_scaler.fit_transform(df.values))

    print('\n', '*' * 30, '\n')

    print(standardize(df))
    print(std_scaler.fit_transform(df.values))
