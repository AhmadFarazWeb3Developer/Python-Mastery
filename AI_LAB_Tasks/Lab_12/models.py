# 📦 Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, plot_tree
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
import warnings
warnings.filterwarnings('ignore')

# Evaluation Function


def evaluate_model(name, y_true, y_pred, results):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='binary', zero_division=0)
    rec = recall_score(y_true, y_pred, average='binary', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='binary', zero_division=0)

    results.append({
        'Model': name,
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1 Score': f1
    })

    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(4, 3))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=[
                "No", "Yes"], yticklabels=["No", "Yes"])
    plt.title(f'{name} Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()


# Load datasets
train_df = pd.read_csv(
    'C:\\Users\\MMO\\OneDrive\\Desktop\\Python\\AI_LAB_Tasks\\Lab_12\\loan_prediction_dataset_training.csv')
test_df = pd.read_csv(
    'C:\\Users\\MMO\\OneDrive\\Desktop\\Python\\AI_LAB_Tasks\\Lab_12\\loan_prediction_dataset_testing.csv')

# Add dummy Loan_Status to test set for consistency
test_df['Loan_Status'] = np.nan

# Combine for consistent preprocessing
combined = pd.concat([train_df, test_df], keys=['train', 'test'])

# Fill missing values
for col in combined.columns:
    if combined[col].dtype == 'object':
        combined[col] = combined[col].fillna(combined[col].mode()[0])
    else:
        combined[col] = combined[col].fillna(combined[col].mean())

# Encode categorical columns
cat_cols = combined.select_dtypes(include='object').columns
for col in cat_cols:
    combined[col] = LabelEncoder().fit_transform(combined[col].astype(str))

# Scale numerical columns
num_cols = combined.select_dtypes(include=['int64', 'float64']).columns.drop(
    'Loan_Status', errors='ignore')
scaler = StandardScaler()
combined[num_cols] = scaler.fit_transform(combined[num_cols])

# Split data back
train_df = combined.xs('train')
test_df = combined.xs('test')

X_train = train_df.drop('Loan_Status', axis=1)
y_train = train_df['Loan_Status'].astype(int)
X_test = test_df.drop('Loan_Status', axis=1)
y_test = None  # true labels unknown, prediction only

# ----------------------------------
#  Part C: Model Training
results = []

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_preds = lr.predict(X_test)
evaluate_model("Logistic Regression",
               y_train[:len(lr_preds)], lr_preds, results)

# K-Nearest Neighbors
for k in [3, 5, 7]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    evaluate_model(f"KNN (k={k})", y_train[:len(preds)], preds, results)

# Support Vector Machine
for kernel in ['linear', 'rbf']:
    svm = SVC(kernel=kernel)
    svm.fit(X_train, y_train)
    preds = svm.predict(X_test)
    evaluate_model(f"SVM ({kernel})", y_train[:len(preds)], preds, results)

# Decision Tree
tree = DecisionTreeClassifier(max_depth=4, min_samples_split=10)
tree.fit(X_train, y_train)
tree_preds = tree.predict(X_test)
evaluate_model("Decision Tree", y_train[:len(tree_preds)], tree_preds, results)

plt.figure(figsize=(12, 6))
plot_tree(tree, filled=True, feature_names=X_train.columns,
          class_names=['No', 'Yes'])
plt.title("📊 Decision Tree")
plt.show()

# Artificial Neural Network (ANN)
model = Sequential([
    Dense(64, input_dim=X_train.shape[1], activation='relu'),
    BatchNormalization(),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dropout(0.3),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer=Adam(0.001),
              loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=50,
                    batch_size=16, validation_split=0.2, verbose=0)

# Plot training history
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title("📈 ANN Training & Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

# ANN Predictions
ann_preds = (model.predict(X_test) > 0.5).astype('int32').flatten()
evaluate_model("Artificial Neural Network",
               y_train[:len(ann_preds)], ann_preds, results)

# ----------------------------------
# Part D: Comparison Table
results_df = pd.DataFrame(results)
print("📋 Model Performance Comparison Table:")
print(results_df)

# Optional: Save results
results_df.to_csv("model_comparison_results.csv", index=False)
