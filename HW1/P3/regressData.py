import pdb
import random
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
import math

# X is an array of N data points (one dimensional for now), that is, NX1
# Y is a Nx1 column vector of data values

def poly_phi(X, M, function='polynomial'): # returns phi Vandermonde
    X_hold = np.ones((X.shape[0], M)) #  make X.shape[0] (N) x M ones array (M+1 because 0, 1, 2... M)
    for i in xrange(1, M):
        if (function == 'polynomial'):
            X_hold[:, [i]] = np.matrix(np.power(X, i))
        elif (function == 'cosine'):
            X_hold[:, [i]] = np.matrix(np.cos(math.pi*X*i))
    return X_hold

def regress_theta(X, Y, M, reg, function='polynomial'): # returns weight vector theta,
    p = poly_phi(X, M + 1, function)
    rI = reg * np.identity(M+1)
    # weight = np.linalg.inv(rI + np.transpose(X).dot(X)).dot(np.transpose(X)).dot(Y)
    pTp = np.dot(p.transpose(), p)
    mid = np.linalg.inv(rI + pTp)
    mid2 = np.dot(mid, p.transpose())
    weight = np.dot(mid2, Y)
    print weight
    return weight

def getData(name):
    data = pl.loadtxt(name)
    # Returns column matrices
    X = data[0:1].T
    Y = data[1:2].T
    return X, Y

def regressAData():
    return getData('regressA_train.txt')

def regressBData():
    return getData('regressB_train.txt')

def validateData():
    return getData('regress_validate.txt')

def curveData():
    return getData('curvefittingp2.txt')

def training_plot():
    X, Y = getData('curvefittingp2.txt')
    plt.scatter(X, Y, facecolors='none', edgecolors='b')
    x = np.arange(0, 1, 0.001)
    y = np.cos(x* np.pi) + 1.5 * np.cos(2 * np.pi * x)
    plt.plot(x, y, label = "Training Plot")
    plt.xlabel('x')
    plt.ylabel('y')

def main():

    X, Y = curveData()
    #print X.shape, Y.shape
    M = 10
    l = [0, 0.1, 0.001, 1]
    for i in range(0, len(l)):
        theta = regress_theta(X, Y, 10, l[i], function='polynomial')
        X_basis = np.matrix([np.linspace(0, 1, 100)]).transpose()
        X_plotting = poly_phi(X_basis, 11)
        Y_plot = np.dot(X_plotting, theta)
        print X_plotting.shape, Y_plot.shape
        plt.plot(X_basis, Y_plot, label = "lambda: %.2f" % l[i])

    plt.scatter(X, Y)
    training_plot()
    plt.legend()
    plt.show()

    X, Y = regressAData()
    #print X.shape, Y.shape
    M = [1, 4, 10]
    l = [0, 0.1, 0.001, 1]
    for j in range(0, len(M)):
        for i in range(0, len(l)):
            theta = regress_theta(X, Y, M[j], l[i], function='polynomial')
            X_basis = np.matrix([np.linspace(-3, 2, 20)]).transpose()
            X_plotting = poly_phi(X_basis, M[j] + 1)
            Y_plot = np.dot(X_plotting, theta)
            print X_plotting.shape, Y_plot.shape
            plt.scatter(X_basis, Y_plot, label = "lambda: %.2f" % l[i])

        x_val, y_val = validateData()
        plt.scatter(x_val, y_val, label = "points")
        plt.title("Regress A Train (M = %d)" % M[j])
        plt.legend()
        plt.show()

    X, Y = regressBData()
    #print X.shape, Y.shape
    M = [1, 4, 10]
    l = [0, 0.1, 0.001, 1]
    for j in range(0, len(M)):
        for i in range(0, len(l)):
            theta = regress_theta(X, Y, M[j], l[i], function='polynomial')
            X_basis = np.matrix([np.linspace(-3, 2, 20)]).transpose()
            X_plotting = poly_phi(X_basis, M[j] + 1)
            Y_plot = np.dot(X_plotting, theta)
            print X_plotting.shape, Y_plot.shape
            plt.scatter(X_basis, Y_plot, label = "lambda: %.2f" % l[i])

        x_val, y_val = validateData()
        plt.scatter(x_val, y_val, label = "points")
        plt.title("Regress B Train (M = %d)" % M[j])
        plt.legend()
        plt.show()


if __name__ == "__main__":
    main()
