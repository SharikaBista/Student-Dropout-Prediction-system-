import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("data/students.csv")

# Map categorical features to numeric values
data["financial_status"] = data["financial_status"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

# Select features and target variable
X = data[["attendance", "gpa", "engagement", "financial_status"]]
y = data["dropout"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 1. Decision Tree Model
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_acc = accuracy_score(y_test, dt_model.predict(X_test))

# 2. Random Forest Model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
rf_acc = accuracy_score(y_test, rf_model.predict(X_test))

print(f"Decision Tree Accuracy: {dt_acc * 100:.1f}%")
print(f"Random Forest Accuracy: {rf_acc * 100:.1f}%")
