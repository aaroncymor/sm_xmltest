import requests, xmltodict, shutil, time

########
# Functions
#######

def download_image(url, destination, name):
    response = requests.get(url, stream=True)

    with open(destination, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    print("Image {} - download success!".format(name))

####
# example_productList.xml
#
###
doc_prod_list = None
with open('example_productList.xml') as fd:
    doc_prod_list = xmltodict.parse(fd.read())

#print(doc_prod_list['ml:lists']['productList'])
#print(len(doc_prod_list['ml:lists']['categoryList']))
#print(len(doc_prod_list['ml:lists']['categoryList']['category']))

category_list = doc_prod_list['ml:lists']['categoryList']['category']

# Getting categories and storing them later in a file
try:
    # category_list contains more than one child element
    for category in category_list:
        print("{}, {}, {}".format(
            category['@id'],
            category['@isAdult'],
            category['#text']))
except TypeError as e:
    #print(e)
    # category_list contains only one child element

    print("{}, {}, {}".format(
        category_list['@id'],
        category_list['@isAdult'],
        category_list['#text']))

product_list = doc_prod_list['ml:lists']['productList']['product']

try:
    """
    TODO: If expired put product in a list for deletion in server.
    """
    # product_list contains more than one child element
    for product in product_list:
        print("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
            product['@code'],
            product['@name'],
            product['@assetType'],
            product['@expired'],
            product['@lastModified'],
            product['@categoryID'],
            product['@publisher'],
            product['@languageCode'],
            product['@languageName'],
            product['feedUrl']
        ))
except TypeError as e:

    """
    TODO: If expired put product in a list(?) for deletion in server.
    """

    #print(e)
    # product_list contains only one child element

    print("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
        product_list['@code'],
        product_list['@name'],
        product_list['@assetType'],
        product_list['@expired'],
        product_list['@lastModified'],
        product_list['@categoryID'],
        product_list['@publisher'],
        product_list['@languageCode'],
        product_list['@languageName'],
        product_list['feedUrl']
    ))

###############################################
# END example_productList.xml                 #
###############################################

###############################################
# example_product.xml                         #
###############################################
print()
doc_prod = None
with open('example_product.xml') as fd:
    doc_prod = xmltodict.parse(fd.read())

"""
TODO: Extract data from other elements. Concentrating on media first
"""
#description_language = doc_prod['product']['descriptionLanguage']
#print(description_language)
#for key, value in description_language.items():
#    print(key, value)

#print(doc_prod['product']['title'])
#print(doc_prod['product']['shortDescription'])
#print(doc_prod['product']['longDescription'])
#print(doc_prod['product']['smsDescription'])
#print(doc_prod['product']['category'])
#print(doc_prod['product']['assetType'])
#print(doc_prod['product']['instructions'])
#print(doc_prod['product']['publisher'])
#print(doc_prod['product']['copyright1'])
#print(doc_prod['product']['copyright2'])
#print(doc_prod['product']['pricing'])
#print(doc_prod['product']['pricing']['priceClass'])
#print(doc_prod['product']['pricing'])
#print(doc_prod['product'])

media_list = doc_prod['product']['resource']['media']
try:
    for media in media_list:
        print("{}, {}, {}, {}, {}, {}".format(
            media['@contentType'],
            media['@mimeType'],
            media['@width'],
            media['@height'],
            media['name'],
            media['location']
        ))

    ctr = 0

    # For testing purposes only. Download only 5 images
    for media in media_list:
        print("{}, {}, {}, {}, {}, {}".format(
            media['@contentType'],
            media['@mimeType'],
            media['@width'],
            media['@height'],
            media['name'],
            media['location']
        ))
        if ctr < 5:
            location = media['location']
            name = media['name']
            destination = "media/{}".format(name)
            download_image(location, destination, name)
            # wait ten(10) seconds every download
            time.sleep(10)
        else:
            break
        ctr += 1
except TypeError as e:
    # media_list contains only one element

    print("{}, {}, {}, {}, {}, {}".format(
        media_list['@contentType'],
        media_list['@mimeType'],
        media_list['@width'],
        media_list['@height'],
        media_list['name'],
        media_list['location']
    ))


################################################
# end example_product.xml                     #
###############################################