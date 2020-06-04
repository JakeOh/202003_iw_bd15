import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import StratifiedShuffleSplit, cross_val_score, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from ch02.ex01 import CombineAttributesAdder


def h_line():
    print('\n', '*' * 30, '\n')


if __name__ == '__main__':
    # 1. 데이터 준비
    path = '../datasets/housing/housing.csv'
    housing_df = pd.read_csv(path)
    print(housing_df.head())

    # 2. 탐색적 데이터 분석 - 데이터 분포 히스토그램, 상관 관계 분석, ...

    # 3. Train/Test set 분리
    # median_income 비율대로 계층적 샘플링(stratified sampling)
    housing_df['income_cat'] = pd.cut(housing_df['median_income'],
                                      bins=[0, 1.5, 3, 4.5, 6, np.inf],
                                      labels=[1, 2, 3, 4, 5])
    h_line()
    print(housing_df['income_cat'].value_counts() / len(housing_df))

    spl = StratifiedShuffleSplit(n_splits=1,  # train/test 1세트
                                 test_size=0.2,  # test set의 비율
                                 random_state=1)
    for train_idx, test_idx in spl.split(housing_df,
                                         housing_df['income_cat']):
        strat_train_set = housing_df.iloc[train_idx]
        strat_test_set = housing_df.iloc[test_idx]
    print(strat_train_set['income_cat'].value_counts() / len(strat_train_set))

    # 계층적 샘플링을 위해서 만들었던 변수 income_cat는 삭제
    strat_train_set = strat_train_set.drop(labels='income_cat', axis=1)
    strat_test_set = strat_test_set.drop(labels='income_cat', axis=1)

    # 4. 학습 세트(train_set)를 전처리(preprocessing)
    # NA 대체, 파생 변수 추가, 변수 스케일링, 원핫 인코딩

    # 학습 세트에서 레이블(정답)을 제거
    housing = strat_train_set.drop(labels='median_house_value', axis=1)
    # 학습 세트의 레이블은 따로 복사해서 저장
    housing_labels = strat_train_set['median_house_value'].copy()

    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),  # NA를 중앙값으로 대체
        ('attrs_adder', CombineAttributesAdder()),  # 파생 변수 추가
        ('std_scaler', StandardScaler())  # 변수 스케일링 - 표준화
    ])

    # 학습 세트에서 수치형 데이터만 추출
    housing_num = housing.drop(labels='ocean_proximity', axis=1)
    num_attrs = list(housing_num)  # 수치형 데이터 변수(컬럼)들의 이름
    cat_attrs = ['ocean_proximity']  # 카테고리 데이터 변수들의 이름

    full_pipeline = ColumnTransformer([
        ('num_pipeline', num_pipeline, num_attrs),
        ('one_hot_enc', OneHotEncoder(), cat_attrs)
    ])

    # Pipeline을 사용한 학습 세트 전처리
    housing_prepared = full_pipeline.fit_transform(X=housing)

    h_line()
    print(housing_prepared[:2])

    # 5. 모델 선택, 학습, 성능 지표 계산
    # Linear Regression(선형 회귀), Decision Tree Regression(결정 트리 회귀)
    # Random Forest Regression, Support Vector Machine Regression, ...
    forest_reg = RandomForestRegressor(random_state=1)  # 모델 선택
    forest_reg.fit(X=housing_prepared, y=housing_labels)  # 모델 학습
    housing_predicts = forest_reg.predict(X=housing_prepared)  # 예측
    # 성능 지표 계산
    forest_mse = mean_squared_error(y_true=housing_labels,
                                    y_pred=housing_predicts)
    forest_rmse = np.sqrt(forest_mse)  # Root Mean Squared Errors

    h_line()
    print('랜덤 포레스트 회귀 RMSE:', forest_rmse)

    # 성능 지표 주의점: 과대적합(overfitting) 여부 확인
    # -> Cross Validation(교차 검증)
    cv_scores = cross_val_score(estimator=forest_reg,
                                X=housing_prepared,
                                y=housing_labels,
                                scoring='neg_mean_squared_error',
                                cv=10)
    cv_scores_rmse = np.sqrt(-cv_scores)
    print('교차 검증 스코어:')
    print('CV RMSE:', cv_scores_rmse)
    print('CV RMSE 평균:', np.mean(cv_scores_rmse))

    # 6. 선택된 모델의 하이퍼 파라미터 튜닝
    param_grid = [
        # 3 estimators x 4 max_features = 12
        {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
        # 2 estimators x 3 max_features = 6
        {'bootstrap': [False], 'n_estimators': [3, 10],
         'max_features': [2, 3, 4]}
    ]
    # 12 + 6 = 18가지 파라미터 조합을 5-fold 교차 검증: 18 x 5 = 90

    grid_search = GridSearchCV(estimator=forest_reg,
                               param_grid=param_grid,
                               scoring='neg_mean_squared_error',
                               return_train_score=True)
    grid_search.fit(X=housing_prepared, y=housing_labels)

    h_line()
    print('Grid Search:')
    print(grid_search)
    print('최적의 하이퍼 파라미터:')
    print(grid_search.best_params_)
    print('최적의 추정기(estimator):')
    print(grid_search.best_estimator_)

    cv_result = grid_search.cv_results_
    for mean_score, params in zip(cv_result['mean_test_score'],
                                  cv_result['params']):
        print(np.sqrt(-mean_score), params)

    # 7. 튜닝까지 끝난 best estimator(최적의 알고리즘)을 테스트 세트에서 테스트
    h_line()
    # 테스트 세트에서 데이터와 레이블 분리
    X_test = strat_test_set.drop('median_house_value', axis=1)  # 데이터
    y_test = strat_test_set['median_house_value'].copy()  # 레이블(정답)

    # 테스트 세트의 데이터도 전처리
    X_test_prepared = full_pipeline.transform(X_test)
    # 주의) 테스트 세트는 fit_transform()이 아니라, transfomr()으로 전처리!

    final_model = grid_search.best_estimator_  # 최종 알고리즘
    # 최종 알고리즘으로 예측
    final_predicts = final_model.predict(X_test_prepared)
    # 최종 모델의 성능 지표 계산
    final_mse = mean_squared_error(y_true=y_test,
                                   y_pred=final_predicts)
    final_rmse = np.sqrt(final_mse)
    print('Final RMSE:', final_rmse)

