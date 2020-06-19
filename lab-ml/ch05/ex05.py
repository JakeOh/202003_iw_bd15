# iris 데이터 - 4개 특성을 모두 사용, multi-class(0, 1, 2) 분류
# train/test set을 stratified split(계층적 분리)으로 나눔.
# SVC, LinearSVC를 비교 - test set에서 정확도, 정밀도, ...

import numpy as np
from sklearn import datasets
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC, SVC


def train_test_report(X, y, classifier, scaler=None, title=None):
    # X, y를 train/test set로 분리
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, stratify=y, test_size=0.2, random_state=1)
    if scaler:  # Scaler가 있는 경우
        model = Pipeline([
            ('scaler', scaler),
            ('classifier', classifier)
        ])
    else:  # Scaler가 없는 경우
        model = classifier
    # 모델 훈련 - 모델을 학습 데이터에 fitting
    model.fit(X_train, y_train)
    # train set의 평가 점수(리포트), test set의 평가 점수(리포트)
    sets = [('Train Set', X_train, y_train),
            ('Test Set', X_test, y_test)]
    for label, Xs, ys in sets:
        print('\n=====', title, label, '=====')
        predicts = model.predict(Xs)
        conf_mat = confusion_matrix(y_true=ys, y_pred=predicts)
        report = classification_report(y_true=ys, y_pred=predicts)
        print(conf_mat)
        print(report)


if __name__ == '__main__':
    iris = datasets.load_iris()
    X, y = iris['data'], iris['target']
    print(X.shape, y.shape)
    # X: 150 samples, 4 features
    # y: label with 3 classes(0, 1, 2)
    classes, counts = np.unique(y, return_counts=True)
    print(classes)
    print(counts)

    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, stratify=y, test_size=0.2,
                         random_state=1)
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
    classes, counts = np.unique(y_train, return_counts=True)
    print(classes, counts)

    lin_svc = LinearSVC(random_state=1)  # 모델 생성
    lin_svc.fit(X_train, y_train)  # 모델을 학습 세트에 맞춤 - 학습
    # 학습 세트의 평가 점수 - 정확도, 정밀도, 재현율, ...
    y_train_pred = lin_svc.predict(X_train)
    conf_mat = confusion_matrix(y_train, y_train_pred)
    print(conf_mat)
    report = classification_report(y_train, y_train_pred,
                                   target_names=iris['target_names'])
    print(report)
    # 테스트 세트의 평가 점수
    y_test_pred = lin_svc.predict(X_test)
    conf_mat = confusion_matrix(y_test, y_test_pred)
    print(conf_mat)
    report = classification_report(y_test, y_test_pred,
                                   target_names=iris['target_names'])
    print(report)

    clf2 = LinearSVC(random_state=1, loss='hinge')
    train_test_report(X, y, clf2, title='LinearSVC(hinge)')
    train_test_report(X, y, clf2, scaler=StandardScaler(),
                      title='LinearSVC(hinge) StandardScaler')

    clf3 = SVC(kernel='linear', random_state=1)
    train_test_report(X, y, clf3,
                      title='SVC(linear)')
    train_test_report(X, y, clf3, scaler=StandardScaler(),
                      title='SVC(linear) StandardScaler')

    clf4 = SGDClassifier(random_state=1)
    train_test_report(X, y, clf4, scaler=StandardScaler(),
                      title='SGDClassifier(hinge, l2)')
