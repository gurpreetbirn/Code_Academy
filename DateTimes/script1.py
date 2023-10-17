from datetime import datetime

birthday = datetime(1994, 2, 15, 4, 25, 12)

print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.weekday())  # 0 is monday, 1 is tuesday etc

print(datetime.now())

num = datetime(2018,1,1) - datetime(2017,1,1)

print(num)

# parse datetime from a string
parsed_date = datetime.strptime("jan 15, 2018", "%b %d, %Y" )
print(parsed_date.month)
print(parsed_date.year)
print(parsed_date)
#date = datetime()

# takes datetime and lets use grab parts and put them in a string
date_string = datetime.strftime(datetime.now(), "%b %d, %Y")
print(date_string)

