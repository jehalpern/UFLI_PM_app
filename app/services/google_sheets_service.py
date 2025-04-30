import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def fetch_sheet_as_csv(sheet_url, local_filename="temp_sheet.csv"):
    # Set up the service account
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("your-service-account.json", scope)
    client = gspread.authorize(creds)

    # Extract the Sheet ID from URL
    sheet_id = sheet_url.split('/d/')[1].split('/')[0]

    # Open the Sheet
    sheet = client.open_by_key(sheet_id).sheet1  # Assumes you want the first sheet

    # Fetch all records and save as CSV
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    df.to_csv(local_filename, index=False)
