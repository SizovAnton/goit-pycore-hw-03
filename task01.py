from datetime import datetime

def get_days_from_today (date):
  try:

    datetime_obj = datetime.strptime(date, '%Y.%m.%d').date()
    current_date = datetime.today().date()

    interval = current_date.toordinal() - datetime_obj.toordinal()
    # return interval

    print(interval)

  except:
    print(f'Date must be yyyy.mm.dd format')

  
get_days_from_today("2024.07.14")