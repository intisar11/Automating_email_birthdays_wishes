##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

date_month = dt.datetime.today().month
date_day = dt.datetime.today().day
print(date_month)
print(date_day)

birthday = pd.read_csv("birthdays.csv")
birthday_dataframe = pd.DataFrame(birthday)
month = birthday_dataframe['month']
day = birthday_dataframe['day']





# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




