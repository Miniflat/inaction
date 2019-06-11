import calendar

try:
    x = input("Inter a day of week: ").upper()
    days_of_days = {
        "MONDAY": 0,
        "TUESDAY": 1,
        "WEDNESDAY": 2,
        "THURSDAY": 3,
        "FRIDAY": 4,
        "SATURDAY": 5,
        "SUNDAY": 6
    }
    my_date = days_of_days[x]
except KeyError:
    print("Invalid input")
    exit()
flag = 0


def list_of_year(my_year):
    global flag
    for month in range(12, 0, -1):
        mycal = calendar.monthcalendar(my_year, month)
        week1 = mycal[0]
        week2 = mycal[1]
        if week1[my_date] != 0:
            number_day = week1[my_date]
        else:
            number_day = week2[my_date]

        if number_day == 1 and my_year == 2019 and month <= 6:
            print(calendar.month_name[month], my_year)
            my_year -= 1
            flag = 1
            break
        if number_day == 1 and my_year == 2018:
            print(calendar.month_name[month], my_year)
            break


list_of_year(2019)
if flag == 0:
    list_of_year(2018)