import joblib  # 아나콘다에 포함된 패키지 - 중간 단계 저장/복원
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import precision_recall_curve, roc_curve, roc_auc_score
from sklearn.model_selection import cross_val_predict, cross_val_score

from ch03.ch03_all import load_mnist_from_pickle, split_mnist

if __name__ == '__main__':
    mnist = load_mnist_from_pickle()
    X_train, y_train, X_test, y_test = split_mnist(mnist)
    # 2진 분류 레이블
    y_train_5 = (y_train == 5)

    sgd_clf = SGDClassifier(random_state=1)  # 분류기, ML 알고리즘

    # 교차 검증(Cross Validation) 예측
    cv_predicts = cross_val_predict(estimator=sgd_clf,  # ML 알고리즘
                                    X=X_train,  # 학습 세트
                                    y=y_train_5,  # 레이블(정답)
                                    cv=3,  # 교차 검증 횟수
                                    method='predict')
    print(cv_predicts)

    # 교차 검증에서 정확도
    cv_acc = np.mean(y_train_5 == cv_predicts)
    print('교차 검증 정확도:', cv_acc)

    # 각 교차 검증 세트의 평가 지표(정확도)들의 리스트를 반환
    cv_scores = cross_val_score(estimator=sgd_clf,
                                X=X_train, y=y_train_5, cv=3)
    print('교차 검증 점수:', cv_scores)
    print(np.mean(cv_scores))

    # cross_val_predict()는 method argument 값에 따라서 다른 결과를 리턴.
    #   method='predict' (기본값): 예측 값(True/False)
    #   method='decision_function': 결정 함수 값
    #   method='predict_proba': 예측 확률
    cv_decision_scores = cross_val_predict(estimator=sgd_clf,
                                           X=X_train, y=y_train_5, cv=3,
                                           method='decision_function')
    print(cv_decision_scores)

    # 교차 검증에서의 P-R 곡선
    precisions, recalls, _ = precision_recall_curve(y_train_5,
                                                    cv_decision_scores)
    plt.plot(recalls, precisions)
    plt.title('P-R Curve')
    plt.show()

    # 교차 검증에서의 ROC 곡선, AUC 계산
    fpr, tpr, _ = roc_curve(y_train_5, cv_decision_scores)
    auc = roc_auc_score(y_train_5, cv_decision_scores)

    plt.plot(fpr, tpr, label=f'AUC: {auc}')
    plt.title('ROC Curve')
    plt.legend()
    plt.show()

    # Python dict 객체
    sgd_clf_binary = {
        'model': sgd_clf,
        'y_predicts': cv_predicts,
        'y_pred_scores': cv_decision_scores
    }
    # dict 객체 (중간 결과)를 파일로 저장
    joblib.dump(sgd_clf_binary, 'sgd_clf_bin.joblib')
