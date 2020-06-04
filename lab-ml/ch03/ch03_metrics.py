import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, \
    precision_recall_curve, roc_curve, roc_auc_score

from ch03.ch03_all import load_mnist_from_pickle, split_mnist

if __name__ == '__main__':
    # mnist 데이터 셋 준비
    mnist = load_mnist_from_pickle()

    # train set/test set 분리
    X_train, y_train, X_test, y_test = split_mnist(mnist)
    print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

    # 2진 분류 - 레이블의 클래스가 2개(5, 5가 아님)
    y_train_5 = (y_train == 5)  # 2진 분류에서 사용할 레이블

    # SGD 분류기 생성
    sgd_clf = SGDClassifier(random_state=1)
    # 분류기를 학습(ML 모델(알고리즘) 학습)
    sgd_clf.fit(X=X_train, y=y_train_5)
    # train set의 예측값
    y_binary_predicts = sgd_clf.predict(X=X_train)
    print('예측값(predicts):', y_binary_predicts)
    print('실제값(actual):', y_train_5)

    # 정확도: 전체 샘플에서 정확하게 예측한 비율
    # accuracy = (TP + TN) / (TP + TN + FP + FN)
    accuracy = np.mean(y_train_5 == y_binary_predicts)
    print('SGD 분류기 정확도(accuracy):', accuracy)

    acc = accuracy_score(y_true=y_train_5,
                         y_pred=y_binary_predicts)
    print('acc =', acc)

    # 혼동(오차) 행렬(confusion matrix)
    conf_mat = confusion_matrix(y_true=y_train_5,
                                y_pred=y_binary_predicts)
    print(conf_mat)
    tn, fp = conf_mat[0, 0], conf_mat[0, 1]
    fn, tp = conf_mat[1, 0], conf_mat[1, 1]
    acc = (tn + tp) / (tn + fp + fn + tp)  # 정확도
    precision = tp / (tp + fp)  # 정밀도
    recall = tp / (tp + fn)  # 재현율
    f1 = 2 / (1 / precision + 1 / recall)  # F1 점수

    print('정확도(accuracy):', acc)
    print('정밀도(precision):', precision)
    print('재현율(recall):', recall)
    print('f1-score:', f1)

    print('-' * 30)
    precision = precision_score(y_true=y_train_5,
                                y_pred=y_binary_predicts)
    recall = recall_score(y_true=y_train_5,
                          y_pred=y_binary_predicts)
    f1 = f1_score(y_true=y_train_5,
                  y_pred=y_binary_predicts)

    print('precision =', precision)
    print('recall =', recall)
    print('f1-scroe =', f1)

    print('-' * 30)

    # 정밀도(Precision)-재현율(Recall) 트레이드오프(Trade-off)

    samples = X_train[-3:]
    sample_labels = y_train_5[-3:]
    print(sample_labels)

    # 결정 함수(decision function): 예측을 하기 위한 점수를 만듦.
    sample_scores = sgd_clf.decision_function(X=samples)
    # predict() 메서드는 결정 함수가 주는 점수들에 따라서 예측(Positive/Negative)함.
    sample_predicts = sgd_clf.predict(X=samples)

    print(sample_scores)
    print(sample_predicts)

    # 결정 함수가 계산한 값들 중에서 양성/음성을 판별하는 기준: 임계값(threshold)
    # 임계값을 변경할 수는 없지만, 일반적으로
    # 임계값이 커지면, 정밀도(precision)가 커지고 재현율(recall)은 낮아짐.
    # 임계값이 작아지면, 정밀도가 낮아지고 재현율이 높아짐.
    # 이런 관계를 "정밀도-재현율 트레이드오프"라 함.

    y_train_scores = sgd_clf.decision_function(X=X_train)
    precisions, recalls, thresholds = \
        precision_recall_curve(y_true=y_train_5,
                               probas_pred=y_train_scores)

    # 정밀도-재현율 트레이드오프(precision-recall trade-off) 그래프
    plt.plot(thresholds, precisions[:-1], label='Precision')
    plt.plot(thresholds, recalls[:-1], label='Recall')
    plt.vlines(x=0, ymin=0, ymax=1, color='r', linestyles='dashed')
    plt.xlim([-20_000, 20_000])
    plt.ylim([0, 1])
    plt.legend()
    plt.show()

    # P-R graph(정밀도-재현율 그래프)
    # x축: 재현율(recall), y축: 정밀도(precision)
    plt.plot(recalls, precisions, 'b-')  # 'b-': color='blue', linestyles='-'
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision vs Recall')
    plt.xlim([0, 1])
    plt.xlim([0, 1])
    plt.show()

    # ROC 곡선(Receiver Operation Characteristic Curve)
    # FPR(False Positive Rate)에 대한 TPR(True Positive Rate)의 그래프
    # FPR(가짜 양성 비율) = FP / (FP + TN)
    # TPR(진짜 양성 비율) = TP / (TP + FN) = 재현율(recall), 민감도(sensitivity)
    # 특이도(specificity) = TN / (TN + FP)
    # FPR = 1 - 특이도

    fpr, tpr, thresholds = roc_curve(y_true=y_train_5,
                                     y_score=y_train_scores)
    plt.plot(fpr, tpr)
    plt.xlabel('FPR(False Positive Rate)')
    plt.ylabel('TPR(True Positive Rate)')
    plt.title('ROC Curve')
    plt.axis([0, 1, 0, 1])
    plt.show()

    # AUC(Area Under the Curve): ROC 곡선 아래쪽의 넓이
    # AUC=1: 완변학 분류기, AUC=0.5: 랜덤 분류기
    # AUC가 클 수록 좋은 분류기
    auc = roc_auc_score(y_true=y_train_5,
                        y_score=y_train_scores)
    print('AUC =', auc)

    # 분류 문제에서 타겟의 분포가 균일하지 않은 경우(5:10%, 5 아님:90%)
    # 정확도가 높아도 정밀도가 떨어질 수 있듯이,
    # ROC 곡선은 1에 가까운 모습이 될 수 있음.
    # 그런 경우에는 ROC 곡선보다는 P-R 그래프를 분류기의 성능 그래프로 사용.
