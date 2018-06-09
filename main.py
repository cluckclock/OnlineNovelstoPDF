import scrape
import convert

print("Webseries to PDF")

title = input("Title of PDF: ")
prefix = input("Prefix of Address: ")
index = int(input("Incrementing index: "))
suffix = input("Suffix (If any): ")
tag = input("Element type: ")
attr = input("Element Atrributes (If any): ")
titleKeyword = input("Keyword in Title (To make sure only scraping what is needed): ")

address = prefix + str(index) + suffix


scraper = scrape.Scraper(address)
pdf = convert.Converter()

text = scraper.getText(tag, attr)
pdf.addText(text)
print(text)
index+=1
address = prefix + str(index) + suffix
scraper.goTo(address)

while titleKeyword in scraper.getText('title'):
    text = scraper.getText(tag, attr)
    pdf.addText(text)
    print(text)
    index+=1
    address = prefix + str(index) + suffix
    scraper.goTo(address)

pdf.printPDF(title)
print("done!")
