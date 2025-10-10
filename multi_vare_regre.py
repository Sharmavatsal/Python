import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample dataset (10 students): Subject scores → IQ
# Columns: [Science, Physics, Chemistry, Biology]
X = np.array([
    [78, 75, 72, 80],
    [85, 82, 80, 88],
    [60, 58, 55, 65],
    [90, 92, 88, 94],
    [70, 68, 65, 72],
    [88, 85, 83, 89],
    [55, 50, 52, 58],
    [95, 90, 93, 96],
    [65, 62, 60, 67],
    [82, 80, 78, 84],
])

# Target: IQ scores
y = np.array([110, 125, 95, 130, 105, 128, 90, 135, 100, 120])

# Feature names for clarity
subjects = ['Science', 'Physics', 'Chemistry', 'Biology']

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict IQ for a new student
new_student = np.array([[85, 83, 80, 86]])  # Example subject scores
predicted_iq = model.predict(new_student)

print(f"\n📊 Predicted IQ for student with scores {new_student[0]}:")
print(f"➡️ IQ: {predicted_iq[0]:.2f}")

# Print model coefficients
print("\n📈 Model Coefficients (weight of each subject):")
for i, subject in enumerate(subjects):
    print(f"  {subject}: {model.coef_[i]:.2f}")

print(f"\n🧠 Intercept (baseline IQ): {model.intercept_:.2f}")

# Optional: Bar plot to show subject influence
plt.figure(figsize=(8, 5))
plt.bar(subjects, model.coef_, color='teal')
plt.title("Effect of Subject Scores on Predicted IQ")
plt.ylabel("Coefficient (Impact on IQ)")
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.show()
