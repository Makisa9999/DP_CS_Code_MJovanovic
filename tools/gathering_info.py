import bs4
import requests
from bs4 import BeautifulSoup
import time


a = input("Enter a symbol: ")

def part_Price ():
    r = requests.get("https://ca.finance.yahoo.com/quote/" + str(a))
    soup = bs4.BeautifulSoup(r.text, "lxml")

    price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price


while True:
    file = open(a + ".txt", "w")
    while True:
        print("The price of " + a + " is: " + str(part_Price()))
        file.write(time.strftime("%H:%M:%S") + " Price of " + a + " is: " + str(part_Price() + "\n"))
    file.close()

