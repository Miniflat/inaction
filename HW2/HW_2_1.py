from calendar import weekday

try:
    print("Enter date of birth: ")
    x = [int(i) for i in input().split(".")]
    day_of_the_week = weekday(x[2], x[1], x[0])
except (TypeError, ValueError):
    print("Enter date of birth in format DD.MM.YYYY. ")
else:
    dayweek = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    result = dayweek[day_of_the_week]
    print(result)


