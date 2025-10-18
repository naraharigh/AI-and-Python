import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

# Step 1: Load sample log data
df = pd.read_csv("sample_logs.csv")

# Step 2: Convert timestamp to numerical features
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['minute'] = df['timestamp'].dt.minute

# Step 3: Encode categorical features (username, action, status)
label_cols = ['username', 'action', 'status']
label_encoders = {}
for col in label_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Step 4: Select features for model
feature_cols = ['username', 'action', 'status', 'response_time', 'hour', 'minute']
X = df[feature_cols]

# Step 5: Train Isolation Forest
iso_model = IsolationForest(contamination=0.1, random_state=42)
df['anomaly'] = iso_model.fit_predict(X)

# Step 6: Show results
print(df[df['anomaly'] == -1])  # -1 means anomaly
