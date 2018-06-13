import mechanicalsoup

class Scraper:

#address of Webseries
    address = ""

#Start page emulator
    browser = mechanicalsoup.StatefulBrowser()

    def __init__(self, address):
        self.address = address
        self.browser.open(address)

#Go to new address
    def goTo(self, address):
        self.browser.open(address)

#Get body of webpage - stuff to be scraped
    def getText(self, elem, details = {}):
        return self.browser.get_current_page().find(elem, attrs = details).text

#Retrieve all elements
    def getAllElements(self):
        return self.browser.get_current_page().findAll()
