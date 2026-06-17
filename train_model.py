import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. Load Data
# 👈 CHANGED: Swapped absolute path for the relative path
file_path = "Default_Fin.csv"
df = pd.read_csv(file_path)

# 2. Drop Index and split features (X) and target (y)
X = df.drop(columns=['Index', 'Defaulted?'])
y = df['Defaulted?']

# 3. Train/Test Split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("Training model...")

# 4. Initialize Random Forest with class_weight='balanced' to handle the 3% imbalance
model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# 5. Evaluate
y_pred = model.predict(X_test)
print("\n" + "="*20 + " Evaluation Report " + "="*20)
print(classification_report(y_test, y_pred))

# 6. Save the trained model to use in Streamlit later
with open('src/loan_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model saved successfully inside the 'src/' folder as 'loan_model.pkl'!")