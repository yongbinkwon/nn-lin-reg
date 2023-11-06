import os
import numpy as np
import random
from skimage import io, color, transform
from functools import reduce

monkeydir = "./monke"
humandir = "./human"

learning_rate = 0.01
iterations = 1000

def readImage(dir, file):
    return io.imread(os.path.join(dir, file))

def preprocess(image):
    return (image/255).flatten()

def imagesAndLabels(dir, label):
    images = []
    labels = []
    for filename in os.listdir(dir):
        if filename.endswith(".jpg"):
            image = readImage(dir, filename)
            images.append(preprocess(image))
            labels.append(label)
    return images, labels

def shuffle(images, labels):
    indices = np.arange(labels.shape[0])
    np.random.shuffle(indices)
    return images[indices], labels[indices]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def result(a, b):
    diff = a-b
    result = reduce(lambda acc, number: acc+1 if number==0 else acc, diff, 0)
    return result/len(a-b)

def binaryClassificationDataset(class0_dir, class1_dir):
    images0, labels0 = imagesAndLabels(class0_dir, 0)
    images1, labels1 = imagesAndLabels(class1_dir, 1)
    images = np.array(images0 + images1)
    labels = np.array(labels0 + labels1)
    return images, labels

images, labels = binaryClassificationDataset(monkeydir, humandir)

A = np.random.rand(images.shape[1])
print(images.T)
print("AAAA")
print(images)
B = random.uniform(0, 1)

for i in range(iterations):
    X, Y = shuffle(images, labels)
    Y_pred = sigmoid(A.dot(X.T) + B)
    
    dw = (1/len(X)) * X.T.dot(Y_pred - Y)
    db = (1/len(X)) * np.sum(Y_pred - Y)

    A -= learning_rate * dw
    B -= learning_rate * db
    
test_images, test_labels = binaryClassificationDataset("./test/monke", "./test/human")

Y_regression = sigmoid(test_images.dot(A) + B)
classification = list(map(lambda x: 1 if x >= 0.5 else 0, Y_regression))
result = result(test_labels, classification)
print(result)
print(classification)
print(test_labels)
