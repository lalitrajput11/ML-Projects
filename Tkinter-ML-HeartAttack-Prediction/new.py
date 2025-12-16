import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
heart_data = pd.read_csv('/home/lalitrajput/Projects/tkinterMLHeartattack/heart.csv')
# print(heart_data.head())  # Optional: just to verify it loads

# Prepare data
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train model
model = LogisticRegression(max_iter=1000, solver='lbfgs')
model.fit(X_train, Y_train)

# Evaluate
X_train_pred = model.predict(X_train)
X_test_pred = model.predict(X_test)

train_acc = accuracy_score(Y_train, X_train_pred)
test_acc = accuracy_score(Y_test, X_test_pred)

print("\n✅ Accuracy on Training data :", train_acc)
print("✅ Accuracy on Test data :", test_acc)
