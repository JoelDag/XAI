import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[0], [1], [2], [3], [4]])
y = np.array([3, 4, 6, 8, 10]) 

model_with_bias = LinearRegression(fit_intercept=True)
model_with_bias.fit(X, y)
y_pred_with_bias = model_with_bias.predict(X)

model_without_bias = LinearRegression(fit_intercept=False)
model_without_bias.fit(X, y)
y_pred_without_bias = model_without_bias.predict(X)

plt.scatter(X, y, color='black', label='Data Points')
plt.plot(X, y_pred_with_bias, color='blue', label='With Bias (fit_intercept=True)')
plt.plot(X, y_pred_without_bias, color='red', linestyle='--', label='Without Bias (fit_intercept=False)')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression: With and Without Bias')
plt.grid(True)
plt.show()
