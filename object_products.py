from collections import namedtuple


class Territory:

    def __init__(self, code, name):

        self.territory_attr = self.__get_territory_attr(code, name)

    def __get_territory_attr(self, code, name):
        """
        """
        price_territory_attr = namedtuple("territory_attr", ["code", "name"])
        return territory_attr(code, name)


class PriceClass:

    def __init__(self, name, rate, currency, territories):
        self.name = self.__get_price_class_attr(name)
        self.rate = rate
        self.currency = currency
        self.territories = territories 

    def __get_price_class_attr(self, name):
        """
        """
        price_class_attr = namedtuple("price_class_attr", ["name"])
        return price_class_attr(name)


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

    def __str__(self):
        pass


class Resource:

    def __init__(self, last_modified, medias):
        self.resource_attr = self.__get_resource_attr(last_modified)
        self.medias = medias

    def __get_resource_attr(self, last_modified):
        """
        """
        resource_attr = namedtuple("resource_attr", ["last_modified"])
        return resource_attr(last_modified)


class Handset:

    def __init__(self,
                 id,
                 make,
                 model,
                 group_id,
                 user_agent):
        self.handset_id = handset_id
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


class Category:

    def __init__(self, category_id, is_adult, text):
        """
        """
        self.category_id = category_id
        self.is_adult = is_adult
        #self.category_attr = self.__get_category_attr(category_id, is_adult)
        self.text = text

    def __get_category_attr(id, is_adult):
        category_attr = namedtuple("category_attr", ["id", "is_adult"])
        return category_attr(id, is_adult)


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

    def __init__(self, last_modified, id, files, supported_handsets, supported_languages):

        self.binary_attr = self.__get_binary_attr(last_modified, id)
        self.files = files
        self.supported_languages = supported_languages
        self.supported_handsets = supported_handsets

    def __get_binary_attr(self, last_modified, id):
        """
        """
        binary_attr = namedtuple("binary_attr", ["last_modified", "id"])
        return binary_attr(last_modified, id)


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
        self.publisher = publisher
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
