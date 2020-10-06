import webbrowser
from bs4 import BeautifulSoup

a = input("Enter a symbol: ")
webbrowser.open("https://ca.finance.yahoo.com/quote/"+str(a))

