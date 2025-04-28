from flask import Blueprint, render_template
from app.services.chart_service import generate_charts_from_data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    chart_paths = generate_charts_from_data(filepath="test_data.csv")
    return render_template("index.html", charts=chart_paths)
