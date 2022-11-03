from hashlib import new
from urllib import request
import requests
from bs4 import BeautifulSoup
import smtplib

# sender='nu_vreau_spam@coneasorin.ro'
# subject='pretul a scazut'
# to_addr_list=['marcu.reutki@gmail.com']
# cc_addr_list=['']
# def sendemail(sender,message,subject,to_addr_list,cc_Addr_list=[]):
#     try:
#         smtpserver='mail.x-it.ro:26'
#         header='From: %s\n'%sender
#         header+='To: 9ss\n'
#         header+='Cc: 8s\n'
#         header+='Subject:%s\n'%sender
#         message = header + message
#
#         server=smtplib.SMTP(smtpserver)
#         server.starttls()
#         server.login(sender,'stinte215_2022')
#         problems = server.sendmail(sender,to_addr_list, message)
#         server.quit()
#         return True
#     except:
#         print('Error:unable to send email')
#         return False
#

# import string
# import requests
# from bs4 import BeautifulSoup
# # from apscheduler.schedulers.blocking import BlockingScheduler
# from hashlib import new
# import smtplib

sender = 'nu_vreau_spam@coneasorin.ro'
subject = 'Pretul a scazut la:'
to_addr_list = ['marcu.reutki@outlook.com']
cc_addr_list = ['']


def sendemail(sender, message, subject, to_addr_list, cc_addr_list=[]):
    try:
        smtpserver = 'mail.x-it.ro:26'
        header = 'From: %s\n' % sender
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender, "stiinte216_2022")
        problems = server.sendmail(sender, to_addr_list, message)
        server.quit()
        print("Email Trimis")
        return True
    except:
        print("Error: unable to send email")
        return False


# sendemail(sender, "Pretul a scazut la: ", subject, to_addr_list, cc_addr_list)

def data_scraping():
    req = requests.get(
        "https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-128gb-5g-deep-purple-mq9t3rx-a/pd/DXDY4LMBM/?X-Search-Id=8078e075de34c00fc8f2&X-Product-Id=101075766&X-Search-Page=1&X-Search-Position=0&X-Section=search&X-MB=0&X-Search-Action=view")
    soup = BeautifulSoup(req.text, "html.parser")
    price = soup.find('p', attrs={'class': 'product-new-price'}).text
    new_price = price[0:5]
    new_price = new_price.replace(".", "")
    new_price = int(new_price)
    pret_referinta = 7969
    if (new_price < pret_referinta):
        sendemail(sender, "Pretul a scazut la: " + str(new_price), subject, to_addr_list, cc_addr_list=[])
        print("Pretul a scazut ")
    else:
        print("Pretul nu a scazut")


# sendemail(sender, "Pretul a scazut la: ", subject, to_addr_list, cc_addr_list)
# # scheduler = BlockingScheduler()
# # scheduler.add_job(data_scraping, 'interval', seconds=10)
# # scheduler.start()
data_scraping()

# def trimitere_email():
#     server=smtplib.SMTP('mail.x-it.ro',26)
#     server.starttls()
#     server.login("nu_vreau_spam@coneasporin.ro","stiinte216_2022")
#     server.sendemail("nu_vreau_spam@coneasporin.ro","marcu.reutki@gmail.com","Subject: Pretul a scazut |n|n Pretul a scazut la 1000 lei")
#     print("Email Trimis")
#     server.quit()
#
#
# def data_scraping():
#     req = requests.get('https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-256gb-5g-deep-purple-mq9x3rx-a/pd/DJDY4LMBM/?X-Search-Id=58c3393741264bcc3995&X-Product-Id=101075770&X-Search-Page=1&X-Search-Position=1&X-Section=search&X-MB=0&X-Search-Action=view')
#     soup=BeautifulSoup(req.text, 'html.parser')
#     price=soup.find('p', attrs={'class':'product-new-price'}).text
#     new_price=price[0:5]
#     new_price=new_price.replace(".","")
#     new_price=int(new_price)
#     # if(new_price<10000):
#     #     trimitere_email()
#     #     print("Pretul sa modificat  :)")
#     # else:
#     #     print("Pretul e acelasi :(")
#     print(price)
#     print(new_price)
#
# data_scraping()

