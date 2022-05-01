import smtplib
email = "intisar.a42@yahoo.com"
password = "zarfgxzvnqkvhydl"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr= email,
                        to_addrs="007764088@coyote.csusb.edu",
                        msg="Subject:Hello\n\nThis is the body"
)



