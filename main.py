import scrape
import convert

def main():
    print("Online Novel to PDF")

    title = input("Title of PDF: ")

    address = input("Address of first page: ")
    index = int(input("Incrementing index: "))
    #parse Address
    parts = address.split(str(index))
    prefix = parts[0]
    suffix = parts[1]

    titleKeyword = input("Keyword in Title \
    (To make sure only scraping what is needed): ")

    address = prefix + str(index) + suffix
    scraper = scrape.Scraper(address)

    tag = ''
    attrs = ''

    if input("Do you know which HTML container the content resides in? ") == 'yes':
        tag = input("Element type: ")
        attrName = input("Element Atrribute Name: ")
        attrValue = input("Element Attribute Value: ")
        attrs = {attrName : attrValue}
    else:
        print("You will be shown the text of each of the elements on the page. If \
        the text matches the content you are looking to scrape, type in yes. \
        If not, Just press enter.")
        elems = scraper.getAllElements()
        for i in range(2, len(elems)):
            content = elems[i].text
            if content != "":
                print(elems[i].text)
                if input("Is this correct?") == 'yes':
                    #Find element attributes
                    elem = elems[i]
                    tag = elem.name
                    attrs = elem.attrs
                    break

    if tag == '':
        print("No element selected. Exiting.")
        exit()

    pdf = convert.Converter()

    text = scraper.getText(tag, attrs)
    pdf.addText(text)
    print(text)
    index+=1
    address = prefix + str(index) + suffix
    scraper.goTo(address)

    while titleKeyword in scraper.getText('title'):
        text = scraper.getText(tag, attrs)
        pdf.addText(text)
        print(text)
        index+=1
        address = prefix + str(index) + suffix
        scraper.goTo(address)

    pdf.printPDF(title)
    print("done!")

if __name__ == '__main__':
    main()
