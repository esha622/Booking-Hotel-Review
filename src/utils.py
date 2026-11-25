from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
RAW_DATA = RAW_DIR / "hotel_bookings.csv"

CLEAN_DATA = (
    ROOT_DIR / "data" / "processed"
    / "cleaned_hotel_bookings.csv"
)

FIGURE_DIR = ROOT_DIR / "outputs" / "figures"
TABLE_DIR = ROOT_DIR / "outputs" / "tables"
DASHBOARD_DIR = ROOT_DIR / "outputs" / "dashboard"

FIGURE_DIR.mkdir(parents=True, exist_ok=True)
TABLE_DIR.mkdir(parents=True, exist_ok=True)
DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)
