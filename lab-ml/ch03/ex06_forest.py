# SGDClassifier와 RandomForestClassifier 비교
import joblib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, roc_auc_score, precision_recall_curve
from sklearn.model_selection import cross_val_predict

from ch03.ch03_all import load_mnist_from_pickle, split_mnist

if __name__ == '__main__':
    # joblib 라이브러리를 사용해서 저장했던 SGDClassifier의 결과를 불러옴.
    sgd_results = joblib.load('sgd_clf_bin.joblib')
    print(sgd_results.keys())  # joblib 저장 객체의 key값들
    sgd_decision_scores = sgd_results['y_pred_scores']
    print(sgd_decision_scores)

    # pickle에 저장된 mnist 데이터를 로드
    mnist = load_mnist_from_pickle()
    # train set/test set로 분리
    X_train, y_train, X_test, y_test = split_mnist(mnist)
    # 2진 분류 레이블(5 vs 5 아님)
    y_train_5 = (y_train == 5)

    # SGDClassifier의 ROC(Receiver Operation Characteristic) 곡선
    x, y, _ = roc_curve(y_true=y_train_5, y_score=sgd_decision_scores)
    plt.plot(x, y)
    plt.axis([0, 1, 0, 1])
    plt.show()

    # SGDClassifier의 AUC(Area Under the Curve) 계산
    sgd_auc = roc_auc_score(y_true=y_train_5,
                            y_score=sgd_decision_scores)

    # RandomForestClassifier를 사용
    forest_clf = RandomForestClassifier(n_estimators=10, random_state=1)

    # 교차 검증 예측값, 정확도(accuracy) -> SGD의 정확도 비교
    forest_predicts = cross_val_predict(estimator=forest_clf,
                                        X=X_train,
                                        y=y_train_5,
                                        cv=3,
                                        method='predict')
    print(forest_predicts)

    forest_acc = np.mean(y_train_5 == forest_predicts)

    sgd_predicts = sgd_results['y_predicts']
    sgd_acc = np.mean(y_train_5 == sgd_predicts)

    print(f'Random Forest 정확도: {round(forest_acc, 3)}, SGD 정확도: {round(sgd_acc, 3)}')

    # ROC 곡선을 그리기 위해서 예측 score를 계산
    forest_pred_scores = cross_val_predict(estimator=forest_clf,
                                           X=X_train,
                                           y=y_train_5,
                                           cv=3,
                                           method='predict_proba')
    print(forest_pred_scores)
    forest_scores = forest_pred_scores[:, 1]
    # 이미지가 '5'일 확률만 선택

    # 예측 점수와 정답 레이블을 사용해서 ROC 곡선을 그림.
    fpr, tpr, _ = roc_curve(y_true=y_train_5, y_score=forest_scores)
    # AUC(Area Under the Curve): ROC 곡선 아래 면적
    forest_auc = roc_auc_score(y_true=y_train_5,
                               y_score=forest_scores)

    plt.plot(x, y, label=f'SGD auc({round(sgd_auc, 3)})')
    plt.plot(fpr, tpr, label=f'Random Forest auc({round(forest_auc, 3)})')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('FPR(False Positive Rate) = 1 - specificity')
    plt.ylabel('TPR(True Positivie Rate), Recall, Sensitivity')
    plt.title('ROC')
    plt.legend()
    plt.show()

    # SGD, Random Forest의 Precision-Recall 곡선
    sgd_precision, sgd_recall, _ = \
        precision_recall_curve(y_train_5, sgd_decision_scores)
    forest_precision, forest_recall, _ = \
        precision_recall_curve(y_train_5, forest_scores)

    plt.plot(sgd_recall, sgd_precision, lw=2, label='SGD')
    plt.plot(forest_recall, forest_precision, lw=2, label='Random Forest')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Plot')
    plt.legend()
    plt.show()
