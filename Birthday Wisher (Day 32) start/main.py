
import datetime as DT

import random
import smtplib
now = DT.datetime.today()
weekday = now.weekday()
email = "intisar.a42@yahoo.com"
password = "jucfyusabmbptlei"
print(weekday)
if weekday == 1:

    with open("quotes.txt", "r") as quotes:
        quotes_list = quotes.read().split("\n")
        choice = random.choice(quotes_list)
        print(choice)

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="007764088@coyote.csusb.edu",
                            msg=f"Subject:Quotes\n\n{choice}")







