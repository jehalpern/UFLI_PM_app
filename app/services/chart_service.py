import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def generate_charts_from_data(filepath="test_data.csv"):
    # Read the data
    df = pd.read_csv(filepath)
    df.columns = ['Student'] + [f'Assessment {i}' for i in range(1, 6)]
    for col in df.columns[1:]:
        df[col] = df[col].str.rstrip('%').astype(float)

    # Generate charts
    chart_folder = 'app/static/charts'
    os.makedirs(chart_folder, exist_ok=True)

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

        chart_filename = f"{student_name.replace(' ', '_')}.png"
        full_chart_path = os.path.join(chart_folder, chart_filename)
        plt.savefig(full_chart_path)
        plt.close()

        chart_paths.append((student_name, f'static/charts/{chart_filename}'))

    return chart_paths
