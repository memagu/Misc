from Other_Projects.Other import loadingbar
import smtplib
import credentials as c

sender = c.fgsgc
reciever = c.fgsgc

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender, c.fgsgc_p)


message = f"""\
Subject: Testing!!!


Is good fam?
"""

for i in range(20):
    loadingbar.loadingbar(i / 20)
    server.sendmail(sender, reciever, message)
#
# server.quit()