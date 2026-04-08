import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

X = data[["temperature", "pressure", "vibration", "load"]]
y = data["status"]

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully!")