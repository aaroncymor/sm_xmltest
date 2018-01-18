## Save ProductList xml URL to file
url = 'http://cmserver.spoiledmilk.com/ContentManagement/xmlFeed?action=8'
response = requests.get(url)
f = open("example_productList.xml", 'w')
f.write(response.text)
f.close()

## Save Products xml URL to file
url = 'http://cmserver.selatra.com/ContentManagement/xmlFeed?action=88&productCode=29322&resellerID=3591'
response = requests.get(url)
f = open("example_product.xml", 'w')
f.write(response.text)
f.close()
