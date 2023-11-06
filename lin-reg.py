import numpy as np
import matplotlib.pyplot as plt

# Tilfeldige punkter hvor X∈[0-100]
X = np.random.randint(0, 101, size=(100, 1))
y = 2 * X + 10 + 10 * np.random.randn(100, 1)

X_test = np.random.randint(0, 101, size=(20, 1))
y_test = 2 * X_test + 10 + 10 * np.random.randn(20, 1)

# Initialize weights and bias
A = 0
B = 1

# Learning rate and number of iterations
learning_rate = 0.0005
iterations = 100000

# Training loop
for i in range(iterations):
    Y_pred = X.dot(A) + B
    
    dw = (1/len(X)) * X.T.dot(Y_pred - y)
    db = (1/len(X)) * np.sum(Y_pred - y)

    A -= learning_rate * dw
    B -= learning_rate * db

# Plot the data points
plt.scatter(X, y, label='Data Points', color='blue')
plt.scatter(X_test, y_test, label='Test Points', color='g')

# Plot the regression line
y_regression = X.dot(A) + B
plt.plot(X, y_regression, label='y = %.2f x + %.2f' %(A, B), color='red')

plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression')
plt.show()

# Print the final weight and bias
print(f'Final Weight (w): {A}, Final Bias (b): {B}')
