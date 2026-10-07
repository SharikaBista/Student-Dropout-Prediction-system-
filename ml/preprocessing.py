import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Load the sample dataset
data = pd.read_csv("data/students.csv")

# 2. Check dataset details
print("--- Dataset Overview ---")
print(f"Total student records: {len(data)}")
print("\nDropout Distribution:")
print(data['dropout'].value_counts())

# 3. Feature Engineering: Ordinal encoding for financial status
financial_map = {"Low": 0, "Medium": 1, "High": 2}
data["financial_status"] = data["financial_status"].map(financial_map)

# 4. Select Features (X) and Target (y)
feature_cols = [
    "attendance",
    "gpa",
    "engagement",
    "financial_status",
    "previous_performance"
]

X = data[feature_cols]
y = data["dropout"]

# 5. Train/Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.2, 
    random_state=42, 
    stratify=y
)

print("\n--- Data Preprocessing Complete ---")
print(f"Training set size: {len(X_train)} samples")
print(f"Testing set size:  {len(X_test)} samples")