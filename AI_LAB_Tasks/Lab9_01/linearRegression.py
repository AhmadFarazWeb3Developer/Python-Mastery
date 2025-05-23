import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pickle
data = pd.read_csv(
    'C:\\Users\\MMO\\OneDrive\\Desktop\\Python\\AI LAB Tasks\\Lab9_01\\SAT_GPA_Data.csv')


X = data[['SAT']].values
y = data['GPA'].values


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=1)


lin_reg = LinearRegression()


lin_reg.fit(X_train, y_train)

predicted = lin_reg.predict(X_test)

print('Coefficient (Slope):', lin_reg.coef_[0])
print('Intercept:', lin_reg.intercept_)

print(
    f"Regression Equation: GPA = {lin_reg.coef_[0]:.2f} * SAT + {lin_reg.intercept_:.2f}")

print('Variance score (R^2):', r2_score(y_test, predicted))


print("Mean squared error: %.2f" % mean_squared_error(y_test, predicted))


plt.title('Actual GPA vs Predicted GPA')
plt.scatter(X_test, y_test, color='blue', label='Actual GPA')
plt.plot(X_test, predicted, color='red', linewidth=2, label='Predicted GPA')
plt.xlabel('SAT')
plt.ylabel('GPA')
plt.legend()
plt.grid(True)
plt.show()

with open('C:\\Users\\MMO\\OneDrive\\Desktop\\Python\\AI LAB Tasks\\Lab9\\saved_models\\linearRegression.pkl', 'wb') as f:
    pickle.dump(lin_reg, f)

print("Model saved successfully!")
