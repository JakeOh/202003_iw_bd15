import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, log_loss


def calc_scores(samples, bias, weights):
    # samples array에 모든 값이 1인 컬럼을 맨앞에 추가.
    m = len(samples)  # 샘플의 개수(row 개수)
    samples_b = np.c_[np.ones((m, 1)), samples]
    Theta = np.c_[bias.reshape((-1, 1)), weights]
    return samples_b @ Theta.T


def calc_softmax(scores):
    # print(np.exp(scores))
    # print(np.sum(np.exp(scores), axis=1))
    return np.exp(scores) / np.sum(np.exp(scores), axis=1).reshape((-1, 1))


if __name__ == '__main__':
    # scikit의 iris 데이터 셋을 로드
    iris = datasets.load_iris()

    # petal length, petal width를 데이터로 선택
    X = iris.data[:, [2, 3]]
    y = iris.target

    # LogisticRegression 모델 생성, 학습
    log_reg = LogisticRegression(random_state=1)
    log_reg.fit(X, y)

    # 데이터 셋의 예측값을 계산
    y_pred = log_reg.predict(X)

    # confusion matrix, 분류 리포트 출력
    conf_mat = confusion_matrix(y, y_pred)
    print(conf_mat)

    clf_report = classification_report(y, y_pred,
                                       target_names=iris.target_names)
    print(clf_report)

    # 모델에서 학습된 intercept, coef들을 찾음
    bias, weights = log_reg.intercept_, log_reg.coef_
    print('\nbias:')
    print(bias)  # (3,) shape
    print('\nweights:')
    print(weights)  # (3, 2) shape

    # 데이터 셋에서 샘플을 임의로 5개를 선택
    np.random.seed(1)
    sample_idx = np.random.randint(150, size=5)  # 0 <= r < 150 난수 5개
    # print(sample_idx)
    samples = X[sample_idx]
    print('\nsamples:')
    print(samples)

    # 샘플이 각 클래스에 속할 점수, 확률 계산
    sample_scores = calc_scores(samples, bias, weights)
    print('\nsample_scores')
    print(sample_scores)

    sample_probs = calc_softmax(sample_scores)
    print('\nsample probabilities:')
    print(sample_probs)

    # LogisticRegression 모델이 계산한 확률과 비교
    probs = log_reg.predict_proba(samples)
    print(probs)

    # 분류(classification)의 손실(비용) - log_loss
    loss = log_loss(y_true=y[sample_idx], y_pred=sample_probs)
    print('cross entropy:', loss)

