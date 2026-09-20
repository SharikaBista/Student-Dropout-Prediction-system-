import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_data(file_path):
    # 1. Load Dataset
    df = pd.read_csv(file_path)
    print("--- RAW DATA SUMMARY ---")
    print(f"Total Records: {len(df)}")
    
    # Check Class Imbalance
    dropout_counts = df["dropout"].value_counts()
    print("\nTarget Distribution (Dropout vs Retention):")
    print(f"Did not drop out (0): {dropout_counts.get(0, 0)}")
    print(f"Dropped out (1):       {dropout_counts.get(1, 0)}")
    
    # 2. Feature Encoding
    # Convert categorical text column 'financial_status' into numeric values
    financial_map = {"Low": 0, "Medium": 1, "High": 2}
    df["financial_status"] = df["financial_status"].map(financial_map)
    
    # 3. Separate Features (X) and Target Label (y)
    feature_columns = [
        "attendance",
        "gpa",
        "engagement",
        "financial_status",
        "previous_performance"
    ]
    
    X = df[feature_columns]
    y = df["dropout"]
    
    # 4. Train / Test Split (80% Training, 20% Testing)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print("\n--- DATA SPLIT COMPLETE ---")
    print(f"Training Features Shape (X_train): {X_train.shape}")
    print(f"Testing Features Shape (X_test):   {X_test.shape}")
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = prepare_data("data/students.csv")