import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Data
X = np.array([[1], [2], [3], [4], [6], [7], [8], [9], [10]])
y = np.array([20, 35, 45, 55, 70, 75, 85, 90, 95])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Prediction for 7.5 hours of study
new_X = np.array([[7.5]])
predicted_y = model.predict(new_X)
print(f"Predicted score for 7.5 hours of study: {predicted_y[0]:.2f}")

# Plotting the data and regression line
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.scatter(new_X, predicted_y, color='green', marker='o', s=100, label='Prediction')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Simple Linear Regression")
plt.legend()
plt.grid(True)
plt.show()

# Coefficient and intercept
print(f"Coefficient (slope): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

# Prediction for 5 hours of study
prediction_5_hours = model.predict([[5]])
print(f"Predicted score for 5 hours of study: {prediction_5_hours[0]:.2f}")
