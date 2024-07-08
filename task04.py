from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
   today = datetime.today().date()
   upcoming_birthdays = []

   for user in users:
      birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
      birthday_this_year = birthday.replace(year=today.year)
      
      if birthday_this_year < today:
         birthday_this_year = birthday_this_year.replace(year=today.year + 1)

      days_untill_birthday = (birthday_this_year - today).days
      
      if 0 <= days_untill_birthday <=7:
         congratulation_date = birthday_this_year
         
         if birthday_this_year.weekday() >= 5:
            congratulation_date += timedelta(days=(7 - birthday_this_year.weekday()))
            
         upcoming_birthdays.append({
            'name': user['name'],
            'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
         })

   return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1990.07.13"},
    {"name": "Jane Smith", "birthday": "1992.07.09"},
    {"name": "Charlie", "birthday": "1985.07.10"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)