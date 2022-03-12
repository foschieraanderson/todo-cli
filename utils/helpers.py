from datetime import datetime

def date_format(date: str) -> str:
    """Format datime to date"""
    date = datetime.fromisoformat(date).strftime('%d/%m/%Y')
    return date
