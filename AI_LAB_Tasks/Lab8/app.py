

import matplotlib.pyplot as plt
from flask import Flask, render_template
import pandas as pd
import os
import io

import matplotlib
matplotlib.use('Agg')  # <-- Add this line
app = Flask(__name__)


@app.route("/")
def data_analysis():
    # Load dataset
    df = pd.read_csv("Social_Network_Ads.csv")

    # First few rows
    first_rows = df.head().to_html(classes='table table-striped', index=False)

    # Data Info
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue().replace('\n', '<br>')

    # Missing values
    missing_values = df.isnull().sum()

    # Descriptive statistics
    num_records = len(df)
    means = df.mean(numeric_only=True)
    medians = df.median(numeric_only=True)
    std_devs = df.std(numeric_only=True)

    # Ensure plots folder exists
    if not os.path.exists("static/plots"):
        os.makedirs("static/plots")

    # Histogram: Purchased distribution
    plt.figure()
    df['Purchased'].value_counts().plot(
        kind='bar', title="Purchased Distribution")
    plt.xlabel("Purchased")
    plt.ylabel("Count")
    plt.savefig("static/plots/histogram.png")
    plt.close()

    # Scatter Plot: Age vs Estimated Salary
    plt.figure()
    plt.scatter(df['Age'], df['EstimatedSalary'],
                c=df['Purchased'], cmap='bwr', alpha=0.6)
    plt.title("Age vs Estimated Salary")
    plt.xlabel("Age")
    plt.ylabel("Estimated Salary")
    plt.savefig("static/plots/scatter.png")
    plt.close()

    return render_template("data_analysis.html",
                           first_rows=first_rows,
                           info_str=info_str,
                           missing_values=missing_values,
                           num_records=num_records,
                           means=means,
                           medians=medians,
                           std_devs=std_devs)


if __name__ == "__main__":
    app.run(debug=True)
