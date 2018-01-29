import requests, xmltodict, shutil, time
from object_products import (Territory, PriceClass, Media, Resource, Handset, Category, File, Binary, SupportedLanguage, Product)

###############################################
# example_product.xml                         #
###############################################


def get_territories(territory_list):
    """
    Get territory details
    """
    territories = []
    try:            
        for territory in territory_list:
            territory_obj = Territory(territory['@code'], territory['@name'])
            territories.append(territory_obj)

    except TypeError as e:
        territory_obj = Territory(territory_list['@code'], territory_list['@name'])
        territories.append(territory_obj)

    return territories


def get_medias(media_list):
    """
    Get media details
    """
    medias = []
    try:
        for media in media_list:
            media_obj = Media(
                    media['@contentType'],
                    media['@mimeType'],
                    media['@width'],
                    media['@height'],
                    media['location'],
                    media['name']
                )

            medias.append(media_obj)

#        ctr = 0

        # For testing purposes only. Download only 5 images
#        for media in media_list:
#            print("{}, {}, {}, {}, {}, {}".format(
#                media['@contentType'],
#                media['@mimeType'],
#                media['@width'],
#                media['@height'],
#                media['name'],
#                media['location']
#            ))

    #        if ctr < 5:
    #            location = media['location']
    #            name = media['name']
    #            destination = "media/{}".format(name)
    #            download_image(location, destination, name)
    #            # wait ten(10) seconds before sending another request
    #            time.sleep(10)
    #        else:
    #            break
    #        ctr += 1
    except TypeError as e:
        # media_list contains only one element
        media_obj = Media(
                media_list['@contentType'],
                media_list['@mimeType'],
                media_list['@width'],
                media_list['@height'],
                media_list['location'],
                media_list['name']
            )

        medias.append(media_obj)

    return medias


def get_files(file_list):
    """
    Get file details
    """
    files = []
    try:
        for file in file_list:
            file_obj = File(
                    file['@mimeType'],
                    file['@downloadSequence'],
                    file['@size'],
                    file['name'],
                    file['location']
                )
            files.append(file_obj)
                    
    except TypeError as e:
        file_obj = File(
                file_list['@mimeType'],
                file_list['@downloadSequence'],
                file_list['@size'],
                file_list['name'],
                file_list['location']
            )

        files.append(file_obj)

    return files


def get_handsets(handset_list):
    """
    Get handset details
    """
    handsets = []
    try:
        # handset_list contains only one element
        for handset in handset_list:
            handset_obj = Handset(
                    handset['id'],
                    handset['make'],
                    handset['model'],
                    handset['groupId'],
                    handset['useragent']
                )

            handsets.append(handset_obj)
    except TypeError as e:
        # handset_list contains only one element
        handset_obj = Handset(
            handset_list['id'],
            handset_list['make'],
            handset_list['model'],
            handset_list['groupId'],
            handset['useragent']
        )
        
        handsets.append(handset_obj)

    return handsets


def get_supported_languages(language_list):
    supported_languages = []
    try:
        for language in language_list:
            supported_language_obj = SupportedLanguage(
                    language['@code'],
                    language['@name']
                )
            supported_languages.append(supported_language_obj)
    except TypeError as e:
        supported_language_obj = SupportedLanguage(
                language_list['@code'],
                language_list['@name']
            )
        supported_languages.append(supported_language_obj)

    return supported_languages


def generate_product(product):

    description_language = product['descriptionLanguage']
    
    category = product['category']
    category_obj = Category(category['@id'], category['@isAdult'], category['#text'])

    price_class = product['pricing']['priceClass']
    territory_list = price_class['licencedTerritories']['territory']

    price_class_obj = PriceClass(
        price_class['@name'], 
        price_class['rate'], 
        price_class['currency'],
        territory_list)
    
    resource = product['resource']
    media_list = resource['media']

    resource_obj = Resource(resource['@lastModified'], media_list)

    binary = product['binaries']['binary']

    file_list = binary['files']['file']
    handset_list = binary['supportedHandsets']['handset']
    supported_language_list = binary['supportedLanguages']['language']

    binary_obj = Binary(binary['@lastModified'], binary['@id'], file_list, handset_list, supported_language_list)

    product = Product(
            product['@productCode'],
            product['@productName'],
            product['@lastModified'],
            product['@xsi:schemaLocation'],
            product['@xmlns:xsi'],
            description_language['@code'],
            description_language['@name'],
            product['title'],
            product['shortDescription'],
            product['longDescription'],
            product['smsDescription'],
            category_obj,
            product['assetType'],
            product['instructions'],
            product['publisher'],
            product['copyright1'],
            product['copyright2'],
            price_class_obj,
            resource_obj,
            binary_obj
        )

    return product


if __name__ == "__main__":
    with open('example_product.xml') as fd:
        doc_prod = xmltodict.parse(fd.read())

    product = generate_product(doc_prod['product'])
    territories = product.price_class.territories
    for territory in territories:
        print(territory.territory_attr.name)
        print(territory.territory_attr.code)
    
    print(product.price_class.price_class_attr.name)

    medias = product.resource.medias
    for media in medias:
        print(media.media_attr.content_type)
        print(media.media_attr.mime_type)
        print(media.media_attr.width)
        print(media.media_attr.height)
        print(media.location)
        print(media.name)

    handsets = product.binary.handsets
    for handset in handsets:
        print(handset.handset_id)
        print(handset.make)
        print(handset.group_id)
        print(handset.user_agent)

    supported_languages = product.binary.supported_languages
    for supported_language in supported_languages:
        print(supported_language.supported_language_attr.code)
        print(supported_language.supported_language_attr.name)

    files = product.binary.files
    for file in files:
        print(file.file_attr.mime_type)
        print(file.file_attr.download_sequence)
        print(file.file_attr.size)
        print(file.name)
        print(file.location)

    print(product.category.category_attr.id)
    print(product.category.category_attr.is_adult)
    print(product.category.text)



#language_details(language_list)
################################################
# end example_product.xml                     #
###############################################