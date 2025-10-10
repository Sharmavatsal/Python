import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Load data from CSV
data = pd.read_csv('study_scores.csv')  # Ensure this file is in the same folder
X = data[['Hours']].values              # 2D array for sklearn
y = data['Score'].values                # 1D array for output

# Step 2: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 3: Predict for 7.5 hours
new_X = np.array([[7.5]])
predicted_y = model.predict(new_X)
print(f"Predicted score for 7.5 hours of study: {predicted_y[0]:.2f}")

# Step 4: Plot
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.scatter(new_X, predicted_y, color='green', marker='o', s=100, label='Prediction (7.5 hrs)')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Simple Linear Regression")
plt.legend()
plt.grid(True)
plt.show()

# Step 5: Print coefficients
print(f"Coefficient (slope): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

# Step 6: Predict for 5 hours
a=input(int("Enter your working hours"))
prediction_5_hours = model.predict([[5]])
print(f"Predicted score for 5 hours of study: {prediction_5_hours[0]:.2f}")
