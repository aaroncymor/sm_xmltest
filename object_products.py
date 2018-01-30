from collections import namedtuple

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

    if isinstance(binary, list):
        file_list = binary[1]['files']['file']
        handset_list = binary[1]['supportedHandsets']['handset']
        supported_language_list = binary[1]['supportedLanguages']['language']
        binary_obj = Binary(binary[0]['@lastModified'], binary[0]['@id'], file_list, handset_list, supported_language_list)  
    elif isinstance(binary, dict):
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
            product['objectiveDescription'],
            product['publisher'],
            product['copyright1'],
            product['copyright2'],
            price_class_obj,
            resource_obj,
            binary_obj
        )

    return product

class Territory:

    def __init__(self, code, name):

        self.territory_attr = self.__get_territory_attr(code, name)

    def __get_territory_attr(self, code, name):
        """
        """
        territory_attr = namedtuple("territory_attr", ["code", "name"])
        return territory_attr(code, name)

    def __str__(self):
        return self.territory_attr.name


class PriceClass:

    def __init__(self, name, rate, currency, territory_list):
        self.price_class_attr = self.__get_price_class_attr(name)
        self.rate = rate
        self.currency = currency
        self.territories = self.__get_territories(territory_list) 

    def __get_price_class_attr(self, name):
        """
        """
        price_class_attr = namedtuple("price_class_attr", ["name"])
        return price_class_attr(name)

    def __get_territories(self, territory_list):
        territories = []
        try:            
            for territory in territory_list:
                territory_obj = Territory(territory['@code'], territory['@name'])
                territories.append(territory_obj)

        except TypeError as e:
            territory_obj = Territory(territory_list['@code'], territory_list['@name'])
            territories.append(territory_obj)

        return territories



class Media:

    def __init__(self,
                 content_type,
                 mime_type,
                 width,
                 height,
                 location,
                 name):
        self.media_attr = self.__get_media_attr(content_type, mime_type, width, height)
        self.location = location
        self.name = name

    def __get_media_attr(self, content_type, mime_type, width, height):
        """
        """
        media_attr = namedtuple("media_attr", ["content_type", "mime_type", "width", "height"])
        return media_attr(content_type, mime_type, width, height)


class Resource:

    def __init__(self, last_modified, media_list):
        self.resource_attr = self.__get_resource_attr(last_modified)
        self.medias = self.__get_medias(media_list)

    def __get_resource_attr(self, last_modified):
        """
        """
        resource_attr = namedtuple("resource_attr", ["last_modified"])
        return resource_attr(last_modified)

    def __get_medias(self, media_list):
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


class Category:

    def __init__(self, category_id, is_adult, text):
        """
        """
        self.category_attr = self.__get_category_attr(category_id, is_adult)
        self.text = text

    def __get_category_attr(self, id, is_adult):
        category_attr = namedtuple("category_attr", ["id", "is_adult"])
        return category_attr(id, is_adult)


class Handset:

    def __init__(self,
                 id,
                 make,
                 model,
                 group_id,
                 user_agent):
        self.handset_id = id
        self.make = make
        self.model = model
        self.group_id = group_id
        self.user_agent = user_agent

    def __str__(self):

        display = "Handset[Handset ID: {0}, Make: {1}, "
        display += "Model: {2}, Group ID: {3}, User Agent: {4}]"

        return display.format(
            self.handset_id,
            self.make,
            self.model,
            self.group_id,
            self.user_agent
        )



class File: 

    def __init__(self, mime_type, download_sequence, size, name, location):
        self.file_attr = self.__get_file_attr(mime_type, download_sequence, size)
        self.name = name
        self.location = location

    def __get_file_attr(self, mime_type, download_sequence, size):
        """
        """
        file_attr = namedtuple("file_attr", ["mime_type", "download_sequence", "size"])
        return file_attr(mime_type, download_sequence, size)


class SupportedLanguage:

    def __init__(self, code, name):
        self.supported_language_attr = self.__get_supported_language_attr(code, name)

    def __get_supported_language_attr(self, code, name):
        """
        """
        supported_language_attr = namedtuple("supported_language_attr", ["code", "name"])
        return supported_language_attr(code, name)


class Binary:

    def __init__(self, last_modified, id, file_list, handset_list, language_list):

        self.binary_attr = self.__get_binary_attr(last_modified, id)
        self.files = self.__get_files(file_list)
        self.handsets = self.__get_handsets(handset_list)
        self.supported_languages = self.__get_supported_languages(language_list)

    def __get_binary_attr(self, last_modified, id):
        """
        """
        binary_attr = namedtuple("binary_attr", ["last_modified", "id"])
        return binary_attr(last_modified, id)


    def __get_files(self, file_list):
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


    def __get_handsets(self, handset_list):
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
                handset_list['useragent']
            )
            
            handsets.append(handset_obj)

        return handsets       


    def __get_supported_languages(self, language_list): 
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



class Product:

    def __init__(
            self,
            product_code,
            product_name,
            last_modified,
            xsi_schema_location,
            xmlns_xsi,
            description_language_code,
            description_language_name,
            title,
            short_description,
            long_description,
            sms_description,
            category, #category class
            asset_type,
            instructions,
            objective_description,
            publisher,
            copyright1,
            copyright2,
            price_class, #priceclass class
            resource, #resource class
            binary, #binary class
        ):

        self.product_attr = self.__get_product_attr(
                product_code, 
                product_name, 
                last_modified, 
                xsi_schema_location, 
                xmlns_xsi
            )
        self.description_language_attr = self.__get_description_language_attr(
                description_language_code,
                description_language_name
            )
        self.title = title
        self.short_description = short_description
        self.long_description = long_description
        self.sms_description = sms_description
        self.category = category
        self.asset_type = asset_type
        self.instructions = instructions
        self.objective_description = objective_description
        self.publisher = publisher
        self.copyright1 = copyright1
        self.copyright2 = copyright2
        self.price_class = price_class
        self.resource = resource
        self.binary = binary

    def __get_product_attr(
            self, 
            product_code, 
            product_name, 
            last_modified, 
            xsi_schema_location, 
            xmlns_xsi
        ):

        """
        Protected product_attr
        """
        product_attr = namedtuple("product_attr", 
            ["product_code", 
            "product_name", 
            "last_modified", 
            "xsi_schema_location", 
            "xmlns_xsi"])
        return product_attr(product_code, product_name, last_modified, xsi_schema_location, xmlns_xsi)

    def __get_description_language_attr(self, code, name):
        """
        """
        description_language_attr = namedtuple("description_language_attr", 
            ["code", "name"])
        return description_language_attr(code, name)

    def __str__(self):
        pass