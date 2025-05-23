from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.datasets import load_iris

# Load data and split into train and test sets

X, y = load_iris(return_X_y=True, as_frame=True, )
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Define hidden layers separately
hidden_layer_1 = 10
hidden_layer_2 = 10
# hidden_layer_3 = 10
hidden_layers = (hidden_layer_1, hidden_layer_2)

# Train the MLP Classifier
mlp = MLPClassifier(hidden_layer_sizes=hidden_layers,
                    max_iter=1000, random_state=42)
mlp.fit(X_train, y_train)

# Predicting the test set
y_pred = mlp.predict(X_test)

# Evaluate and visualize
plt.plot(mlp.loss_curve_)
plt.title('MLP Loss Curve')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.show()

# Calculate and print evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

print(f'Accuracy : {accuracy:.3f}')
print(f'Precision: {precision:.3f}')
print(f'Recall   : {recall:.3f}')
print(f'F1 Score : {f1:.3f}')

# Display detailed classification report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
