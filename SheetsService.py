import gspread
from gspread.spreadsheet import Spreadsheet
from oauth2client.service_account import ServiceAccountCredentials

class SheetsService:
    def __init__(self, credentials_path: str) -> None:

        scopes = ["https: //www.googleapis.com/auth/spreadsheets"]
        credentials = ServiceAccountCredentials.from_service_account_file(credentials_path, scopes)
        self.client = gspread.authorize(credentials)

    def get_sheet_by_id(sheet_id: str) -> Spreadsheet:
        sheet = self.client.open_by_key(sheet_id)
        return sheet