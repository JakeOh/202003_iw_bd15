from sklearn import datasets

if __name__ == '__main__':
    boston = datasets.load_boston()
    print(boston.DESCR)  # 집값 예측 - regression
    # Train/Test 세트 분리
    # -> MSE 계산, 모델 평가

    cancer = datasets.load_breast_cancer()
    print(cancer.DESCR)  # 암 양성/암 음성 분류(classification)


