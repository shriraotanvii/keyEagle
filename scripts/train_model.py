import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load labeled dataset
df = pd.read_csv("data/labeled_keystrokes_data.csv")

# Prepare features & labels
X = df.drop(columns=["Label", "Keystroke", "Timestamp"])  # Features
y = df["Label"]  # Target variable

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "models/keylogger_model.pkl")
print("✅ Model trained and saved as models/keylogger_model.pkl")
