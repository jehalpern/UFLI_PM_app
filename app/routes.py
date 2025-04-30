from flask import Blueprint, render_template, request, redirect, url_for
redirect, url_for
from app.services.chart_service import generate_charts_from_data
from app.services.google_sheets_service import fetch_sheet_as_csv


main = Blueprint('main', __name__)

@main.route('/')
def index():
    chart_paths = generate_charts_from_data(filepath="test_data.csv")
    return render_template("index.html", charts=chart_paths)

@main.route('/upload', methods=['GET', 'POST'])
def upload_sheet():
    if request.method == 'POST':
        sheet_url = request.form.get('sheet_url')

        if sheet_url:
            # Fetch and save the sheet as a local CSV
            fetch_sheet_as_csv(sheet_url)

            # Generate charts from new CSV
            chart_paths = generate_charts_from_data(filepath="temp_sheet.csv")

            return render_template("index.html", charts=chart_paths)
        
    return render_template("upload.html")