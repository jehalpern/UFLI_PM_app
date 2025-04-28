import matplotlib
matplotlib.use('Agg')


from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv("test_data.csv")
    df.columns = ['Student'] + [f'Assessment {i}' for i in range(1, 6)]
    for col in df.columns[1:]:
        df[col] = df[col].str.rstrip('%').astype(float)

    chart_paths = []
    for i, row in df.iterrows():
        student_name = row['Student']
        scores = row[1:]

        plt.figure()
        scores.plot(kind='line', marker='o', title=student_name)
        plt.ylim(0, 100)
        plt.ylabel("Score (%)")
        plt.xlabel("Assessment")
        plt.grid(True)

        chart_filename = f"static/charts/{student_name.replace(' ', '_')}.png"
        plt.savefig(chart_filename)
        plt.close()

        chart_paths.append((student_name, chart_filename))

    return render_template("index.html", charts=chart_paths)

if __name__ == "__main__":
    app.run(debug=True)
