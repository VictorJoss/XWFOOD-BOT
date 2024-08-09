import gspread
from gspread.spreadsheet import Spreadsheet
from google.oauth2.service_account import Credentials

class SheetsService:
    def __init__(self, credentials_path: str) -> None:

        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        credentials = Credentials.from_service_account_file(credentials_path, scopes = scopes)
        self.client = gspread.authorize(credentials)

    def get_sheet_by_id(self, sheet_id: str) -> Spreadsheet:
        sheet = self.client.open_by_key(sheet_id)
        return sheet
    
