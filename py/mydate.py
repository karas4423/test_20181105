from datetime import datetime, timedelta

def from_date(fix_date, interval):
    date1 = datetime.strptime(fix_date, '%Y-%m-%d')
    delta1 = timedelta(days=interval)
    date1 = (date1 + delta1).strftime('%Y-%m-%d')
    return date1

