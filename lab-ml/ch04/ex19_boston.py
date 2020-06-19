import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    boston = datasets.load_boston()  # class dict
    print(boston.DESCR)  # 집값 예측 - regression
    # Train/Test 세트 분리 -> MSE 계산, 모델 평가
    X, y = boston['data'], boston['target']
    print(X.shape, y.shape)

    boston_df = pd.DataFrame(data=X, columns=boston.feature_names)
    print(boston_df.head())
    print(boston_df.describe())
    print(boston_df.isnull().sum())

    # Train/Test 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        random_state=1)
    lin_reg = LinearRegression()  # 모델 생성
    lin_reg.fit(X_train, y_train)  # 모델 학습, 훈련 - 모델을 학습 데이터 맞춤.
    # 훈련 세트의 예측값
    y_train_pred = lin_reg.predict(X_train)
    train_mse = mean_squared_error(y_true=y_train,
                                   y_pred=y_train_pred)
    train_rmse = np.sqrt(train_mse)
    print('Linear Regression Train RMSE:', train_rmse)
    train_r2 = r2_score(y_train, y_train_pred)
    print('Linear Regression Train R^2:', train_r2)

    # 테스트 세트의 예측값
    y_test_pred = lin_reg.predict(X_test)
    test_mse = mean_squared_error(y_test, y_test_pred)
    test_rmse = np.sqrt(test_mse)
    test_r2 = r2_score(y_test, y_test_pred)
    print('Linear Regression Test RMSE:', test_rmse)
    print('Linear Regression Test R^2:', test_r2)

    # LinearRegression vs SGDRegressor
    sgd_reg = SGDRegressor(random_state=1)  # 모델 생성
    sgd_reg.fit(X_train, y_train)  # 모델 훈련
    y_train_pred = sgd_reg.predict(X_train)  # 학습 세트 예측값
    # -> 학습 세트의 RMSE, R2-score
    y_test_pred = sgd_reg.predict(X_test)  # 테스트 세트 예측값
    # -> 테스트 세트의 RMSE, R2-Score

    # Scaler 사용 -> Pipeline
    pipe1 = Pipeline([
        ('scaler', StandardScaler()),
        ('regressor', LinearRegression())
    ])
    pipe1.fit(X_train, y_train)  # 학습
    y_train_pred = pipe1.predict(X_train)  # Train 예측값
    # -> Train RMSE, R2-score
    y_test_pred = pipe1.predict(X_test)  # Test 예측값

    scaler = StandardScaler()
    X_train_scale = scaler.fit_transform(X_train)
    X_test_scale = scaler.transform(X_test)

    # cancer = datasets.load_breast_cancer()
    # print(cancer.DESCR)  # 암 양성/암 음성 분류(classification)


