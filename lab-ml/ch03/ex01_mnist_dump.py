import pickle

from sklearn.datasets import fetch_openml

if __name__ == '__main__':
    mnist = fetch_openml(name='mnist_784', version=1)
    # print(mnist)  # dict
    print(mnist.keys())

    print(mnist.DESCR)  # mnist['DESCR']: 데이터 설명

    print()
    print(mnist['data'])  # mnist.data: 숫자 손글씨 이미지 데이터(28x28)
    print(mnist['data'].shape)
    # 70_000개의 28x28(=784 pixel) 크기의 손글씨 이미지들

    print()
    print(mnist['target'])  # mnist.target: 손글씨 레이블(정답)
    print(mnist['target'].shape)
    # 70_000개 손글씨 이미지의 레이블 - 문자열

    # 데이터 셋을 fetch_openml()보다 빠르게 로드하기 위해서,
    # mnist 데이터 셋을 pickle로 저장
    with open('mnist.pkl', mode='wb') as file:  # write binary 모드
        pickle.dump(mnist, file)




