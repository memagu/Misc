import smtplib
import time

print("Please login!")
sender = input("Input your Gmail: ")
sender_pword = input("Inpur your password: ")

receiver = input("Input the email of the recipiant: ")
number_of_emails = int(input("Input the amount of emails to be sent: "))


server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender, sender_pword)

message = f"""\
Subject: Testing!!!


Is good fam?
"""


def loadingbar(progress, length=32, filler=chr(9608), background=chr(9617), prefix="Loading:", suffix="%"):
    filler_amt = int(progress * length)
    print(
        f"|{filler_amt * filler}{(length - filler_amt) * background}|{f' {prefix} '}{round(progress * 100, 1)}{suffix}",
        end="\r")


for i in range(number_of_emails):
    loadingbar(i / number_of_emails, length=100, prefix=f"Sending emails {i}/{number_of_emails} (", suffix="% complete! )")
    server.sendmail(sender, receiver, message)
    time.sleep(1)

server.quit()
