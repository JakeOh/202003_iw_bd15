# XGBoost(Extreme Gradient Boost) - early stopping이 구현되어 있음
# conda prompt 실행
# >>> pip install xgboost
import xgboost
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

if __name__ == '__main__':
    print(xgboost.__version__)

    np.random.seed(42)
    m = 100
    X = np.random.rand(m, 1) - 0.5
    y = 3 * X[:, 0] ** 2 + 0.05 * np.random.randn(m)

    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.2, random_state=49)

    xgb_reg = XGBRegressor()
    xgb_reg.fit(X_train, y_train,
                eval_set=[(X_test, y_test)],
                early_stopping_rounds=5)
