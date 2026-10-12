from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import numpy as np

np.random.seed(42)

hours = np.random.uniform(0, 10, 200)
attendance = np.random.uniform(40, 100, 200)
previous_marks = np.random.uniform(20, 100, 200)
score = hours * 5 + attendance * 0.2 + previous_marks * 0.3
labels = (score >= 45).astype(int)

X = np.column_stack((hours, attendance, previous_marks))
y = labels
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
model = make_pipeline(
    StandardScaler(),
    RandomForestClassifier(n_estimators=100, random_state=42)
)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Student Performance Prediction")
print("-" * 35)
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
print(f"Model accuracy: {accuracy:.2%}")
print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))
new_student = np.array([[6.5, 85, 72]])
prediction = model.predict(new_student)[0]
probability = model.predict_proba(new_student)[0]

print("New Student Prediction")
print(f"Study hours: {new_student[0][0]}")
print(f"Attendance: {new_student[0][1]}%")
print(f"Previous marks: {new_student[0][2]}")
print(f"Predicted result: {'PASS' if prediction == 1 else 'FAIL'}")
print(f"Pass probability: {probability[1]:.2%}")