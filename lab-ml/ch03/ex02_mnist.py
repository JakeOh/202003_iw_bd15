import pickle
import numpy as np
import matplotlib.pyplot as plt


def plot_digit(im_array):
    """
    1-d ndarray 흑백 이미지 배열을 전달받아서, 이미지를 그래프로 출력

    :param im_array: 784 pixel인 1차원 배열
    :return: None
    """
    image = im_array.reshape((28, 28))  # 1d (784,)-> 2d (28, 28)
    plt.imshow(image, cmap='binary')
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    # 객체(object) -> 파일 저장: pickle.dump(obj, file)
    # 파일 -> 객체(object): var = pickle.load(file)

    # mnist.pkl 파일을 읽어서 데이터 복원
    with open('mnist.pkl', mode='rb') as file:
        mnist = pickle.load(file)
    print(mnist.keys())

    # 손글씨 데이터
    X = mnist['data']
    # 손글씨 데이터 레이블
    y = mnist['target'].astype(np.int8)  # 문자열 레이블 -> 숫자 레이블

    # 데이터, 레이블 shape 확인
    print(X.shape, y.shape)

    # 데이터 확인
    digit0 = X[0]
    # print(digit0)  # 784개 숫자, 0 ~ 255
    print(digit0.reshape((28, 28)))
    print(y[0])

    # (28, 28) ndarray를 이미지로 그리기
    plt.imshow(digit0.reshape((28, 28)), cmap='binary')
    plt.axis('off')
    plt.show()

    # 손글씨 data 5개 정도를 그래프 출력, 레이블 비교
    for i in np.random.randint(0, 70_000, size=5):
        print(y[i])
        plot_digit(X[i])
