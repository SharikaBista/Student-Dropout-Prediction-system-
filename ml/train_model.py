import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Load dataset
data = pd.read_csv("data/students.csv")

# 2. Convert categorical column to numbers
data["financial_status"] = data["financial_status"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

# 3. Select all 5 features and target
X = data[[
    "attendance",
    "gpa",
    "engagement",
    "financial_status",
    "previous_performance"
]]
y = data["dropout"]

# 4. Split data (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 5. Initialize and train Random Forest model ONLY
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rf_model.fit(X_train, y_train)

# 6. Evaluate model
predictions = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

# 7. Save model binary for Flask backend
joblib.dump(rf_model, "model.joblib")

print("--- Model Training Complete ---")
print("Random Forest model trained successfully.")
print(f"Test Accuracy: {accuracy * 100:.1f}%")
print("Saved trained model to 'model.joblib'")