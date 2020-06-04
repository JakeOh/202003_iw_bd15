# github에서 다운로드받은 datasets를 프로젝트에 복사
# ../datasets/housing/housing.csv 파일을 읽어서 데이터 프레임 생성

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor


def my_split(data, test_ratio=0.2):
    """
    데이터 프레임 data의 순서를 임의로 섞어서, test_ratio의 비율대로
    data를 두 개 subset(training_set, test_set)으로 나눈 후 리턴.

    :param data: 데이터 프레임
    :param test_ratio: 테스트 세트의 비율(0 ~ 1.0)
    :return: training set, test set
    """
    np.random.seed(1)
    num_of_data = len(data)  # 전체 데이터 개수
    # data를 임의로 섞음(row index를 섞음)
    shuffled_index = np.random.permutation(num_of_data)
    # print(shuffled_index)
    test_size = int(num_of_data * test_ratio)
    test_index = shuffled_index[:test_size]  # 앞에서 20%
    train_index = shuffled_index[test_size:]  # 나머지 80%
    # train/test로 나눌 인덱스로 data frame을 쪼갬.
    train_set = data.iloc[train_index]
    test_set = data.iloc[test_index]
    return train_set, test_set


class CombineAttributesAdder(BaseEstimator, TransformerMixin):
    # BaseEstimator, TransformerMixin 클래스를 상속받는 Subclass 정의
    # BaseEstimator 클래스의 get_params(), set_params(), ... 메서드를 상속
    # TransformerMixin 클래스의 fit_transform(), ... 메서드를 상속
    # fit_transform()은 fit() 메서드 호출 후, transform() 메서드를 호출
    # self.fit_transform()는 self.fit().transform()과 동일한 역할
    # 그래서, fit() 메서드는 반드시 self를 리턴해야 함.
    def __init__(self, add_bedrooms_per_room=True):
        # self.변수: field, property, attribute, 멤버 변수, 인스턴스 변수
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        # Nothing to do
        # print('CombineAttributesAdder fit 메서드')
        return self

    def transform(self, X):
        # print('CombineAttributesAdder transform 메서드')
        # 가구당 방의 개수, 가구당 인구수, 침실/방의 비율 변수 추가
        # X: 2-d numpy.ndarray 타입
        room_idx, bedroom_idx, pop_idx, household_idx = 3, 4, 5, 6
        rooms_per_household = X[:, room_idx] / X[:, household_idx]
        pop_per_household = X[:, pop_idx] / X[:, household_idx]
        result = np.c_[X, rooms_per_household, pop_per_household]
        if self.add_bedrooms_per_room:
            bedroom_per_room = X[:, bedroom_idx] / X[:, room_idx]
            result = np.c_[result, bedroom_per_room]

        return result


if __name__ == '__main__':
    path = '../datasets/housing/housing.csv'
    housing = pd.read_csv(path)
    print(housing.iloc[:5])  # DataFrame head 확인
    # DataFrame info: row, column, data type, not-null 개수
    housing.info()
    # 기술 요약 통계량
    # 1) 수치형 - 평균, 표준편차, 중앙값, 최솟값, 최댓값, 4분위 수, ...
    print(housing.describe())
    # 2) 범주형(category) - 빈도수(frequency)
    print(housing['ocean_proximity'].value_counts())

    # DataFrame의 row: observation, example, instance
    # DataFrame의 column: variable(변수), feature(특성), attribute(속성)

    # 시각화 -> 변수들의 특징, 이상치, ... 모습들 발견
    # 연속형 변수들의 분포 -> 히스토그램
    housing.hist(bins=50)
    plt.show()

    # 데이터 셋을 training set와 test set을 구분(분리, split)
    # train_set, test_set = my_split(housing, test_ratio=0.2)
    train_set, test_set = train_test_split(housing, test_size=0.2,
                                           random_state=1)
    print('train length:', len(train_set))
    print('test length:', len(test_set))

    print(train_set.iloc[:5])  # 훈련 세트 head 정보

    # 만약 median_income(수입)이 median_house_value(주택 가격)에
    # 영향를 많이 미친다고 하면, 수입의 비율대로 훈련/테스트 세트가 나눠져야 함.
    housing['median_income'].hist(bins=5)
    plt.show()
    # 대다수의 데이터들의 median_income은 6이하
    housing['income_cat'] = pd.cut(housing['median_income'],
                                   bins=[0, 1.5, 3, 4.5, 6, np.inf],
                                   labels=[1, 2, 3, 4, 5])
    print(housing['income_cat'].value_counts())
    print(housing['income_cat'].value_counts() / len(housing))

    housing['income_cat'].hist()
    plt.show()

    # 계층적 분리(Stratified Split)
    spl = StratifiedShuffleSplit(n_splits=1, test_size=0.2,
                                 random_state=1)
    for train_idx, test_idx in spl.split(housing, housing['income_cat']):
        strat_train_set = housing.iloc[train_idx]
        strat_test_set = housing.iloc[test_idx]

    # 계층적(stratified) split된 학습 세트와 테스트 세트의 비율
    print(strat_train_set['income_cat'].value_counts() / len(strat_train_set))
    print(strat_test_set['income_cat'].value_counts() / len(strat_test_set))

    # train과 test set에서는 income_cat 컬럼을 삭제
    strat_train_set = strat_train_set.drop(labels='income_cat', axis=1)
    strat_test_set = strat_test_set.drop(labels='income_cat', axis=1)

    print(strat_train_set.iloc[:5])

    # 학습(훈련) 세트 시각화
    # stratified train set의 복사본을 housing 변수로
    housing = strat_train_set.copy()

    # train set의 지리 정보(latitude, longitude)를 시각화
    housing.plot(kind='scatter', x='longitude', y='latitude',
                 alpha=0.4,  # 투명도(0: 투명 ~ 1: 불투명)
                 s=housing['population'] / 100,  # 점의 크기(size)
                 c='median_house_value',  # 점의 색깔(color)
                 cmap=plt.get_cmap('jet')  # color map
                 )
    plt.show()

    # 변수들 간의 상관 관계 - 상관 계수(-1 ~ 1)
    corr_mat = housing.corr()  # 상관 행렬(correlation matrix)
    print(corr_mat)
    print(corr_mat['median_house_value'])

    # 전체 방 개수(total_rooms), 전체 침실 개수(total_bedrooms) 대신에
    # 가구(household)당 방 개수, 침실 개수와의 상관 관계?
    # 가구(household)당 인구수와의 상관 관계?
    # 침실과 방의 비율과의 상관 관계?
    housing['rooms_per_household'] = \
        housing['total_rooms'] / housing['households']
    housing['bedrooms_per_household'] = \
        housing['total_bedrooms'] / housing['households']
    housing['population_per_household'] = \
        housing['population'] / housing['households']
    housing['bedrooms_per_room'] = \
        housing['total_bedrooms'] / housing['total_rooms']

    corr_mat = housing.corr()
    print(corr_mat['median_house_value'].sort_values(ascending=False))

    print('\n', '*' * 30, '\n')
    # 머신 러닝에 사용할 train set을 준비
    # Stratified Sampling된 train set를 다시 복사
    # - 설명 변수와 레이블을 각각 다른 DF으로 만듦.
    # - 나중에 scikit 패키지의 fit 메소드를 호출할 때 이용.
    housing = strat_train_set.drop(labels='median_house_value', axis=1)
    housing_labels = strat_train_set['median_house_value'].copy()

    # 데이터 정제 1) null 처리
    housing.info()
    # total_bedrooms 컬럼의 null을 중앙값으로 대체
    # -> train set의 null을 대체할 때 사용한 값은
    # 모델 평가 단계에서 test set의 null을 대체할 때도 사용해야 함.
    # median_total_rooms = housing['total_bedrooms'].median()
    # housing['total_bedrooms'] = \
    #     housing['total_bedrooms'].fillna(median_total_rooms)
    # print(housing['total_bedrooms'].describe())

    # scikit-learn 패키지 기능을 사용한 null 처리
    imputer = SimpleImputer(strategy='median')

    # train set에서 수치형 데이터(numeric data)만 선택
    housing_num = housing.drop(labels='ocean_proximity', axis=1)

    imputer.fit(housing_num)  # NA를 대체할 값들 찾음.
    print(imputer.statistics_)

    X = imputer.transform(housing_num)
    # NA가 모두 특정값으로 대체된 2-d "ndarray"
    print(X)

    # 2d ndarray -> DataFrame 변환
    housing_tr = pd.DataFrame(data=X,
                              columns=housing_num.columns,
                              index=housing_num.index)
    housing_tr.info()

    # 변수들 추가: 가구당 방의 개수, 가구당 인구수, 침실/방의 비율
    # 변수들을 추가하는 기능(메서드)를 가지고 있는 클래스를 정의하면,
    # scikit-learn 패키지의 다른 기능들과 함께 사용할 수 있음.
    attrs_adder = CombineAttributesAdder(False)  # 생성자 호출 -> 인스턴스 생성
    # print(attrs_adder.add_bedrooms_per_room)  # 인스턴스 변수
    # print(attrs_adder.get_params())  # BaseEstimator로 부터 상속받은 메서드
    print(X[:2, :])
    X2 = attrs_adder.fit_transform(X)
    print(X2[:2, :])

    # Scaling: 컬럼들마다 서로 다른 단위들을 일정하게 맞추는 과정
    std_scaler = StandardScaler()
    X3 = std_scaler.fit_transform(X)
    print(X3[:2, :])

    # 대부분의 머신 러닝 알고리즘에서는 텍스트(문자열) 데이터를 직접 처리하기 보다는
    # 숫자로 변환해서 처리를 해야만 하는 경우들이 있음.
    # housing 데이터 프레임에서 카테고리 변수들로만 이루어진 부분집합(DF)
    housing_cat = housing[['ocean_proximity']]
    print(housing_cat.head())

    print('\n', '*' * 30, '\n')
    # Ordinal Encoding: 카테고리를 숫자로 매핑
    ordinal_enc = OrdinalEncoder()
    housing_cat_ord_enc = ordinal_enc.fit_transform(housing_cat)
    print(ordinal_enc.categories_)
    print(housing_cat_ord_enc[:5])

    print('\n', '*' * 30, '\n')
    # One-Hot Encoding: 카테고리 개수만큼 컬럼 추가,
    # 해당 카테고리 컬럼의 값 1, 그 이외에는 0을 채워주는 방식
    one_hot_enc = OneHotEncoder()
    housing_cat_1hot = one_hot_enc.fit_transform(housing_cat)
    print(one_hot_enc.categories_)
    print(housing_cat_1hot)  # 희소 행렬(sparse matrix)

    print('\n', '*' * 30, '\n')
    # Pipeline: 여러개의 transformer를 순서대로 적용.
    # 수치형 데이터에 사용되는 Pipeline
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('attrs_adder', CombineAttributesAdder(add_bedrooms_per_room=True)),
        ('std_scaler', StandardScaler())
    ])

    housing_num_tr = num_pipeline.fit_transform(housing_num)
    print(housing_num_tr[:3])

    print('\n', '*' * 30, '\n')
    # 데이터 프레임은 수치형 특성(컬럼)과 문자열 특성(컬럼)들을 함께 갖고 있는
    # 경우가 많음.
    # -> 수치형 컬럼들에만 pipeline을 적용,
    # 문자열 컬럼들에만 다른 pipeline을 적용 후, 하나로 합치는 기능.

    numeric_attrs = list(housing_num)  # 수치형 컬럼의 이름들 추출
    category_attrs = ['ocean_proximity']  # 카테고리 컬럼의 이름들
    print('수치형 특성 이름:', numeric_attrs)
    print('카테고리 특성 이름:', category_attrs)

    full_pipeline = ColumnTransformer([
        ('num_trans', num_pipeline, numeric_attrs),
        ('cat_trans', OneHotEncoder(), category_attrs)
    ])

    housing_prepared = full_pipeline.fit_transform(housing)
    print(housing_prepared[:2])  # 학습 데이터 세트(training set)

    # 전처리 끝

    print('\n', '*' * 30, '\n')
    # 전처리가 끝난 housing_prepared를 여러가지 머신 러닝 알고리즘에 적용
    # 1) 선형 회귀(Linear Regression)
    # 머신 러닝 모델 선택
    lin_reg = LinearRegression()
    # 머신 러닝 모델을 학습 데이터로 학습시킴.
    lin_reg.fit(X=housing_prepared, y=housing_labels)
    # 학습이 끝난 후 예측
    predict = lin_reg.predict(housing_prepared[:5])
    print(predict)  # 학습 데이터의 예측값
    print(housing_labels[:5])  # 학습 데이터의 실제값

    # 회귀: 수치형 자료의 예측
    # 회귀의 평가 지표 - RMSE(Root Mean Squared Errors), MAE(Mean Absolute Error)
    # RMSE 또는 MAE의 값이 작을 수록 더 좋은 모델
    housing_predict = lin_reg.predict(X=housing_prepared)
    lin_mse = mean_squared_error(y_true=housing_labels,
                                 y_pred=housing_predict)
    lin_rmse = np.sqrt(lin_mse)
    print('선형 회귀 RMSE:', lin_rmse)

    print('\n', '*' * 30, '\n')
    # Decision Tree Regression (결정 트리 회귀)
    tree_reg = DecisionTreeRegressor()  # 모델 선택
    tree_reg.fit(X=housing_prepared, y=housing_labels)  # 모델 학습
    tree_predict = tree_reg.predict(X=housing_prepared)  # 예측
    print(tree_predict[:5])
    print(housing_labels[:5])
    tree_mse = mean_squared_error(y_true=housing_labels,
                                 y_pred=tree_predict)
    tree_rmse = np.sqrt(tree_mse)
    print('결정 트리 회귀 RMSE:', tree_rmse)
    # 과대 적합(overfitting): 머신 러닝 모델이 학습 데이터만 너무 잘 설명.

    print('\n', '*' * 30, '\n')
    # k-fold Cross Validation(k-fold 교차 검증)
    tree_cv_scores = cross_val_score(estimator=tree_reg,
                                     X=housing_prepared,
                                     y=housing_labels,
                                     scoring='neg_mean_squared_error',
                                     cv=10)
    tree_rmse_scores = np.sqrt(-tree_cv_scores)
    print(tree_rmse_scores)
    print('트리 회귀 CV 평균:', np.mean(tree_rmse_scores))

    lin_cv_scores = cross_val_score(estimator=lin_reg,
                                    X=housing_prepared,
                                    y=housing_labels,
                                    scoring='neg_mean_squared_error',
                                    cv=10)
    lin_rmse_scores = np.sqrt(-lin_cv_scores)
    print(lin_rmse_scores)
    print('선형 회귀 CV 평균:', np.mean(lin_rmse_scores))

    print('\n', '*' * 30, '\n')
    # Random Forest Regression
    forest_reg = RandomForestRegressor()
    # 모델 학습, 예측, MSE, RMSE 계산
    forest_reg.fit(X=housing_prepared, y=housing_labels)
    forest_predict = forest_reg.predict(X=housing_prepared)
    forest_mse = mean_squared_error(housing_labels, forest_predict)
    forest_rmse = np.sqrt(forest_mse)
    print('랜덤 포레스트 RMSE:', forest_rmse)
    # cross_val_score() 계산
    forest_cv_scores = cross_val_score(estimator=forest_reg,
                                       X=housing_prepared,
                                       y=housing_labels,
                                       scoring='neg_mean_squared_error',
                                       cv=10)
    forest_rmse_scores = np.sqrt(-forest_cv_scores)
    print(forest_rmse_scores)
    print('랜덤 포레스트 CV 평균:', np.mean(forest_rmse_scores))

    print('\n', '*' * 30, '\n')
    # Support Vector Machine Regression
    svm_reg = SVR(kernel='linear')
    # 모델 학습, 예측 , MSE, RMSE 계산
    # cross_val_score() 계산
