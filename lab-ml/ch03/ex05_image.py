import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from ch03.ch03_all import load_mnist_from_pickle, split_mnist


def image_to_array(image_file):
    image = Image.open(image_file)
    im_arr = np.array(image).astype(np.uint8)
    return im_arr


if __name__ == '__main__':
    # 이미지 파일(bmp, jpg, png, ...)을 읽어서 numpy.ndarray로 변환
    # 1) 이미지 파일 열기
    image3 = Image.open('digit3.bmp')
    print(image3)
    # 2) Image 객체를 ndarray로 변환
    # -> 8 bit unsigned int(부호 없는 정수) 타입 변환
    im_arr = np.array(image3).astype(np.uint8)
    print(im_arr)
    print(im_arr.shape)

    image1 = image_to_array('digit1.bmp') + 255
    # image1 = np.where(image1 == 0, 1, 0)
    print(image1)

    image3 = image_to_array('digit3.bmp') + 255
    # image3 = np.where(image3 == 0, 1, 0)
    print(image3)

    image5 = image_to_array('digit5.bmp') + 255
    # image5 = np.where(image5 == 0, 1, 0)
    print(image5)

    plt.imshow(image5, cmap='binary')
    plt.show()

    # ML 알고리즘을 테스트할 때 사용할 테스트 세트
    X_test = [image1.reshape((784,)),
              image3.reshape((784,)),
              image5.reshape((784,))]

    # mnist 예제 세트 로드
    mnist = load_mnist_from_pickle()
    # SGDClassifier를 mnist로 학습 - 2진 분류기
    X_train, y_train, _, _ = split_mnist(mnist)
    print(X_train.shape, y_train.shape)

    sgd_clf = SGDClassifier(random_state=1)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    y_train_5 = (y_train == 5)
    sgd_clf.fit(X_train_scaled, y_train_5)

    # X_test로 SGD 분류기 테스트
    X_test_scaled = scaler.transform(X_test)
    predicts = sgd_clf.predict(X_test_scaled)
    pred_scores = sgd_clf.decision_function(X_test_scaled)
    print(predicts)
    print(pred_scores)

