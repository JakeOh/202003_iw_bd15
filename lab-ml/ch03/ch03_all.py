import pickle

import numpy as np


def load_mnist_from_pickle(file='mnist.pkl'):
    with open(file, mode='rb') as f:
        mnist = pickle.load(f)
    return mnist


def split_mnist(mnist_data, test_size=10_000):
    # 데이터, 레이블
    X, y = mnist_data['data'], mnist_data['target'].astype(np.int8)
    train_size = 70_000 - test_size
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    return X_train, y_train, X_test, y_test
