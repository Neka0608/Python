import smtplib

#creates SMTP sesion
s = smtplib.SMTP("smtp.gmail.com", 587)

#start TLS for security
s.starttls()

#Authentication 
s.login("nekagowda@gmail.com","racchu229")

#message to be sent
message = "Hello,How are you"

#sending the mail
s.sendmail("nekagowda@gmail.com","suprithashetty2405@gmail.com","Hello,How are you")
print("Message has been sent")
#terminating the session
s.quit()