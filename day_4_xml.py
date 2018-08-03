import xml.etree.ElementTree as ET



def getXmlPage():
    page = ET.Element('html')
    head = ET.SubElement(page, 'head')
    body = ET.SubElement(page, 'body')
    title = ET.SubElement(head, 'title')
    title.text = "page title here"
    title = ET.SubElement(head, 'rank')
    title.text = '1'
    # dump the page cotents to the console
    ET.dump(page)
    return page
    # sObj =  ET.dump(page)
    # print(sobj)
    # # return page


def main():
    page = getXmlPage()
    print(type(page))
    page.
    print("got page: {}".format(page))
    # root = ET.fromstring(page)
    # tree = ET.parse(page)

if __name__ == "__main__":
    main()
