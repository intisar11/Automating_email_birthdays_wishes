##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import smtplib
import random
email = "intisar.a42@yahoo.com"
password = "mwyunjmofrkddjmh"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

date_month = dt.datetime.today().month
date_day = dt.datetime.today().day
today = (date_month, date_day)
print(today)

data = pd.read_csv("birthdays.csv")

new_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}






# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv




if today in new_dict:
    file_path = (f"./letter_templates/letter_{random.randint(1,3)}.txt")
    with open (file_path) as letter:
        birthday_person = new_dict[today]
        data = letter.read()
        data.replace("[NAME]", birthday_person["name"])
        print(data)


# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP as connection:
    connection.starttls()
    connection.login(email, password)
    connection.sendmail()



