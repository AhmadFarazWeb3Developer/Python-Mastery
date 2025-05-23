import os
import seaborn as sns
from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')  # Avoid GUI issues

app = Flask(__name__)

# Create directory for plots
os.makedirs('static/plots', exist_ok=True)

# Load and clean dataset
dataset = pd.read_csv('./churn.csv')
dataset_clean = dataset.dropna()


@app.route('/')
def data_analysis():
    # Top 10 rows
    head_data = dataset_clean.head(10).to_dict(orient='records')

    # Column info
    column_info = {
        'columns': dataset_clean.columns.tolist(),
        'dtypes': dataset_clean.dtypes.astype(str).to_dict(),
        'missing': dataset.isnull().sum().to_dict()
    }

    # Unique values
    unique_counts = dataset_clean.nunique().to_dict()

    # Descriptive statistics
    numeric_data = dataset_clean.select_dtypes(include='number')
    stats = {
        'mean': numeric_data.mean().round(2).to_dict(),
        'median': numeric_data.median().round(2).to_dict(),
        'std': numeric_data.std().round(2).to_dict()
    }

    # Preprocessing
    X = dataset_clean.drop(['Churn', 'customerID'], axis=1)
    y = dataset_clean['Churn'].map({'No': 0, 'Yes': 1})
    X_encoded = pd.get_dummies(X, drop_first=True)

    # Bar plots
    cat_columns = dataset_clean.select_dtypes(
        include='object').columns.drop('Churn')
    bar_plot_files = []
    for col in cat_columns:
        plt.figure(figsize=(4, 3))
        dataset_clean[col].value_counts().plot(kind='bar', color='skyblue')
        plt.title(f'{col} Distribution')
        plt.tight_layout()
        filename = f'static/plots/bar_{col}.png'
        plt.savefig(filename)
        bar_plot_files.append(f'bar_{col}.png')
        plt.close()

    # Pie chart
    plt.figure(figsize=(4, 4))
    dataset_clean['Churn'].value_counts().plot.pie(
        autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'])
    plt.title('Churn Distribution')
    plt.ylabel('')
    churn_pie_file = 'churn_pie.png'
    plt.tight_layout()
    plt.savefig(f'static/plots/{churn_pie_file}')
    plt.close()

    # Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    heatmap_file = 'correlation_heatmap.png'
    plt.tight_layout()
    plt.savefig(f'static/plots/{heatmap_file}')
    plt.close()

    return render_template('index.html',
                           data=head_data,
                           info=column_info,
                           unique=unique_counts,
                           stats=stats,
                           plots=bar_plot_files,
                           churn_pie=churn_pie_file,
                           heatmap=heatmap_file)


if __name__ == '__main__':
    app.run(debug=True)
