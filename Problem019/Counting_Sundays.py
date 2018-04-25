from datetime import datetime, date, timedelta

def is_year_leap(year):
    if year == 0:
        print ("There is no year 0. Exiting")
        exit()
    if year % 4 != 0:
        return False
    else:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True



def simple_count_weekdays(date, end, weekday):
    num_weekdays = 0
    while date <= end:
        if datetime.isoweekday(date) == weekday:
            if date.day == 1: num_weekdays += 1
        date += timedelta(days=1)

    return num_weekdays


if __name__ == "__main__":
    start = date(1901, 01, 01)
    end = date(2000, 12, 31)
    # Monday is 1, Sunday is 7
    weekday = 7


    print (simple_count_weekdays(start, end, weekday))