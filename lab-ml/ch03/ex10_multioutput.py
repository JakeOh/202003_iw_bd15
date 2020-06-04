import numpy as np
from sklearn.neighbors import KNeighborsClassifier

from ch03.ch03_all import load_mnist_from_pickle, split_mnist
from ch03.ex02_mnist import plot_digit

if __name__ == '__main__':
    mnist = load_mnist_from_pickle()
    X_train, y_train, X_test, y_test = split_mnist(mnist)

    # 이미지 데이터 노이즈 값을 더해서 이미지를 변형
    print(X_train[0])  # 원본 데이터: 784 pixel = 28x28
    plot_digit(X_train[0])

    np.random.seed(1)
    # 난수를 X_train과 같은 크기로 생성
    noise = np.random.randint(0, 100, size=X_train.shape)
    # 노이즈(생성된 난수)를 훈련 세트에 더함
    X_train_mod = X_train + noise

    print(X_train_mod[0])
    plot_digit(X_train_mod[0])

    # ML 모델(알고리즘) 선택
    knn_clf = KNeighborsClassifier()
    # 모델 훈련
    knn_clf.fit(X=X_train_mod, y=X_train)

    # 훈련되지 않은 세트(테스트 세트)에서 노이즈가 추가된 이미지로 예측 테스트
    noise = np.random.randint(0, 100, size=X_test.shape)
    X_test_mod = X_test + noise
    plot_digit(X_test_mod[0])

    # 테스트 데이터로 predict
    cleaned = knn_clf.predict([X_test_mod[0]])

    print('\n', '*' * 30, '\n')
    # 예측한 결과 확인
    print(cleaned)  # array
    plot_digit(cleaned)

    



