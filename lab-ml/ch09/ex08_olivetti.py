import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split


def plot_olivetti_faces(faces, labels, ncol=5):
    """

    :param faces: olivetti 얼굴 사진 배열(array)
    :param labels: olivetti 얼굴 사진의 타겟 레이블
    :param ncol: 한개의 row에 그려야할 이미지 개수(컬럼 개수)
    :return: None
    """
    n_faces = len(faces)
    nrow = (n_faces - 1) // ncol + 1
    for i, (face, label) in enumerate(zip(faces, labels)):
        plt.subplot(nrow, ncol, i + 1)
        plt.imshow(face.reshape((64, 64)), cmap=plt.cm.gray)
        plt.title(label)
        plt.axis('off')
    plt.show()


if __name__ == '__main__':
    olivetti = fetch_olivetti_faces()
    print(olivetti.keys())
    print(olivetti.DESCR)

    X, y = olivetti['data'], olivetti['target']
    print(X.shape, y.shape)
    # 샘플 개수 m = 400
    # 특성(feature) 개수 n = 4096 = 64x64 (이미지 가로 64px, 세로 64px)

    plot_olivetti_faces(X[-10:], y[-10:], ncol=5)

    # 데이터(X), 타겟(y)를
    # 훈련 셋(X_train, y_train): 280개 샘플
    # 검증 셋(X_val, y_val): 80개 샘플
    # 테스트 셋(X_test, y_test): 40개 샘플
    # 계층적 샘플링(stratified) 방식으로 나눔.

    # Train/Test 분리
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, stratify=y, test_size=40,
                         random_state=1)
    # Train/Validation 분리
    X_train, X_val, y_train, y_val = \
        train_test_split(X_train, y_train, stratify=y_train,
                         test_size=80, random_state=1)

    print(X_train.shape, X_val.shape, X_test.shape)
    print(y_train.shape, y_val.shape, y_test.shape)

    print(np.unique(y_train, return_counts=True))
    print(np.unique(y_val, return_counts=True))
    print(np.unique(y_test, return_counts=True))
