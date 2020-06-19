import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from ch07.ex06_gradientboost import plot_prediction

if __name__ == '__main__':
    # GBRT(Gradient Boosted Regression Tree)

    np.random.seed(42)
    m = 100  # 샘플 개수
    X = np.random.rand(m, 1) - 0.5  # -0.5 <= X < 0.5
    y = 3 * X[:, 0]**2 + 0.05 * np.random.randn(m)

    gbr = GradientBoostingRegressor(max_depth=2,
                                    n_estimators=3,
                                    learning_rate=1.0,
                                    random_state=42)
    gbr.fit(X, y)
    predicts = gbr.predict([[0.3]])
    print('predicts:', predicts)

    axes = [-0.5, 0.5, -0.1, 1.0]
    plot_prediction([gbr], X, y, axes)
    plt.show()

    # GBRT를 사용할 때, n_estimators와 learning_rate는 서로 trade-off
    # 학습률(learning rate)이 작으면, 앙상블 학습에 사용되는 Tree의 개수
    # (n_estimators)가 많아져야 성능이 좋아짐.
    # 학습률이 크면, Tree의 개수가 작아도 비슷한 성능을 보임.

    gbr_slow = GradientBoostingRegressor(learning_rate=0.1,
                                         n_estimators=50,
                                         max_depth=2,
                                         random_state=42)
    gbr_slow.fit(X, y)
    print('GBR score:', gbr_slow.score(X, y))
    plot_prediction([gbr_slow], X, y, axes)
    plt.show()

    # GradientBoostingRegressor가 각 단계에 예측하는 값들을 찾을 수 있음.
    # -> n_estimators에서 설정한 값보다 작을 때에 일찍 종료시킬 수 있음.
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.2, random_state=42)

    gbr = GradientBoostingRegressor(learning_rate=0.1,
                                    n_estimators=150,
                                    max_depth=2,
                                    random_state=42)
    gbr.fit(X_train, y_train)
    print(gbr.score(X_train, y_train))  # overfitting된 모델

    staged_errors = [mean_squared_error(y_test, y_pred)
                     for y_pred in gbr.staged_predict(X_test)]
    # print(len(staged_errors))
    # staged_errors의 최솟값과 최솟값의 위치
    min_error = np.min(staged_errors)
    min_error_index = np.argmin(staged_errors)
    print(f'min error: {min_error}, index: {min_error_index}')

    # staged_errors 시각화
    plt.plot(staged_errors, color='blue', ls='solid', marker='o')
    plt.axhline(y=min_error, c='red', ls='dashed')
    plt.axvline(x=min_error_index, c='red', ls='dashed')
    plt.show()
