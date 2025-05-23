from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)


def generate_visualizations(df):
    """Generate and save visualizations to static folder"""
    # Create static directory if it doesn't exist
    if not os.path.exists('static'):
        os.makedirs('static')

    # Histogram of GPA
    plt.figure(figsize=(8, 6))
    df['GPA'].hist(color='skyblue', edgecolor='black')
    plt.title('Distribution of GPA Scores')
    plt.xlabel('GPA')
    plt.ylabel('Frequency')
    histogram_path = 'static/gpa_histogram.png'
    plt.savefig(histogram_path)
    plt.close()

    # Scatter plot of SAT vs GPA
    plt.figure(figsize=(8, 6))
    plt.scatter(df['SAT'], df['GPA'], color='green', alpha=0.6)
    plt.title('SAT Scores vs GPA')
    plt.xlabel('SAT Score')
    plt.ylabel('GPA')
    plt.grid(True)
    scatter_path = 'static/sat_gpa_scatter.png'
    plt.savefig(scatter_path)
    plt.close()

    return 'gpa_histogram.png', 'sat_gpa_scatter.png'


@app.route('/')
def data_analysis():
    # Load the dataset
    df = pd.read_csv('SAT_GPA_Data.csv')

    # Generate visualizations
    histogram_img, scatter_img = generate_visualizations(df)

    # Prepare data for template
    data_info = {
        'columns': list(df.columns),
        'dtypes': df.dtypes.to_dict(),
        'missing': df.isnull().sum().to_dict()
    }

    sat_stats = {
        'mean': round(df['SAT'].mean(), 2),
        'median': df['SAT'].median(),
        'std': round(df['SAT'].std(), 2)
    }

    gpa_stats = {
        'mean': round(df['GPA'].mean(), 2),
        'median': round(df['GPA'].median(), 2),
        'std': round(df['GPA'].std(), 3)
    }

    return render_template(
        'analysis.html',
        head_data=df.head().to_html(classes='data-table', index=False),
        data_info=data_info,
        num_records=len(df),
        sat_stats=sat_stats,
        gpa_stats=gpa_stats,
        histogram_img=histogram_img,
        scatter_img=scatter_img
    )


if __name__ == '__main__':
    app.run(debug=True)
