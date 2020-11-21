import pyautogui
import requests
import bs4
import time
import os
import smtplib
import imghdr
from email.message import EmailMessage
from datetime import datetime, date

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = [EMAIL_ADDRESS]

msg = EmailMessage()
msg['Subject'] = 'Update!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

url = "https://www.shilav.co.il/safety-at-home/isofix-car-seat/booster-seat-6810153537"

#Massege to indecate that the program start running
msg.set_content("Web scraping start running on Heruko!")
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print("Massege sent")


def send_massege(price):
    msg.set_content('המחיר של הבוסטר הוא ' + str(price) + "\n" + url)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("Massege sent")

while (True):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content,"html5lib")
    prices = soup.select(".price") #find price in site
    my_price = prices[0].text # sae first price (items' price)
    temp = my_price.split(".") #split to save pirce
    my_price2 = int(temp[0]) #parse to int

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    myDate = today.strftime("%d/%m/%Y")

    print(myDate +", "+current_time + ": current price:",my_price2)
    if (my_price2 != 399):
        send_massege(my_price2)
    time.sleep(3600)

