# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:09:27 2021

@author: Sarthak
"""
import smtplib


def sendEmail(emaillist):
    for address in emaillist:
    # sending emails
        sent_from = 'trulinewsdaily@gmail.com'
        gmail_password = "Trulinews2021"
        gmail_user = sent_from
        to = address
        subject = 'you daily news feed'
        body = 'This is a test.'
        
        print(to)
        ## not sure what the following part does.....
        email_text = """\
        From: %s
        To: %s
        Subject: %s
        
        %s
        """ % (sent_from, to, subject, body)
        ## lets skip that and move on...
        
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
            print('Email sent!')
        except:
            print('Something went wrong...')
 

         
emails = ['lavptl836@gmail.com','nclawson4@gmail.com','bsarthak173@gmail.com']
sendEmail(emails)