# 📦 Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(
    'C:\\Users\\MMO\\OneDrive\\Desktop\\Python\\AI_LAB_Tasks\\Lab_12\\loan_prediction_dataset_training.csv')

# 1. Rename Columns
df.rename(columns={
    'Loan_ID': 'loan_id',
    'Gender': 'gender',
    'Married': 'married',
    'Dependents': 'dependents',
    'Education': 'education',
    'Self_Employed': 'self_employed',
    'ApplicantIncome': 'applicant_income',
    'CoapplicantIncome': 'coapplicant_income',
    'LoanAmount': 'loan_amount',
    'Loan_Amount_Term': 'loan_amount_term',
    'Credit_History': 'credit_history',
    'Property_Area': 'property_area',
    'Loan_Status': 'loan_status'
}, inplace=True)

# 2. Audit Dataset
df['dependents'] = df['dependents'].astype(str).replace('3+', '3')
df['dependents'] = df['dependents'].fillna('0')

# Fill missing numerical and categorical values
df[['loan_amount', 'loan_amount_term', 'credit_history']] = df[['loan_amount', 'loan_amount_term',
                                                                'credit_history']].fillna(df[['loan_amount', 'loan_amount_term', 'credit_history']].median())
df[['gender', 'married', 'self_employed']] = df[['gender', 'married', 'self_employed']
                                                ].fillna(df[['gender', 'married', 'self_employed']].mode().iloc[0])

# 3. Outlier Handling
for col in ['applicant_income', 'coapplicant_income', 'loan_amount']:
    q_low = df[col].quantile(0.05)
    q_high = df[col].quantile(0.95)
    df[col] = np.clip(df[col], q_low, q_high)

# 4. Feature Engineering
df['total_income'] = df['applicant_income'] + df['coapplicant_income']
df['emi'] = df['loan_amount'] / df['loan_amount_term']
df['balance_income'] = df['total_income'] - (df['emi'] * 1000)

# 5. Encoding Strategy
le = LabelEncoder()
df['education'] = le.fit_transform(df['education'])
df['dependents'] = le.fit_transform(df['dependents'])

# One-hot encode all categories (no drop_first to retain all dummy columns)
df = pd.get_dummies(df, columns=[
                    'gender', 'married', 'self_employed', 'property_area'], drop_first=False)

# Encode target
df['loan_status'] = df['loan_status'].map({'Y': 1, 'N': 0})

# -------------------------------
# Part B: Exploratory Data Analysis (EDA)
# -------------------------------

# 1. Visualize Distributions
df[['applicant_income', 'coapplicant_income', 'loan_amount', 'loan_amount_term',
    'total_income', 'emi', 'balance_income']].hist(figsize=(15, 10), bins=20)
plt.tight_layout()
plt.show()

# Bar plots for encoded categorical variables
for col in ['education', 'gender_Female', 'gender_Male', 'married_No', 'married_Yes',
            'self_employed_No', 'self_employed_Yes', 'property_area_Rural', 'property_area_Semiurban', 'property_area_Urban']:
    if col in df.columns:
        sns.countplot(x=col, data=df)
        plt.title(f'Distribution of {col}')
        plt.show()

# 2. Explore Relationships
sns.countplot(x='education', hue='loan_status', data=df)
plt.title('Loan Status by Education')
plt.show()

sns.countplot(x='property_area', hue='loan_status', data=pd.read_csv(
    'C:\\Users\\MMO\\OneDrive\\Desktop\\Python\\AI_LAB_Tasks\\Lab_12\\loan_prediction_dataset_training.csv'))
plt.title('Loan Status by Property Area')
plt.show()

sns.scatterplot(x='balance_income', y='loan_amount',
                hue='loan_status', data=df)
plt.title('Balance Income vs Loan Amount by Loan Status')
plt.show()

# 3. Class Imbalance Check
sns.countplot(x='loan_status', data=df)
plt.title('Loan Status Distribution')
plt.show()

print("Loan status class distribution:")
print(df['loan_status'].value_counts(normalize=True))
