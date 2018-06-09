import mechanicalsoup
import os

browser = mechanicalsoup.StatefulBrowser()
browser.open('https://www.7novels.com/the-light-fantastic/page-1-112353.html')

content = browser.get_current_page().find("div, .chapter-content").text

path = os.getcwd()+"/pages/1"
print(path)
file = open(path, "w")
file.write(content)
