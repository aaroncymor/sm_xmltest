class Category:

    def __init__(self, category_id, is_adult, text):

        self.category_id = category_id
        self.is_adult = is_adult
        self.text = text

    def __str__(self):

        return "Category ID: {0}, Is Adult: {1}, Text: {2}".format(
            self.category_id,
            self.is_adult,
            self.text
        )


class Product:

    def __init__(self,
                 code,
                 name,
                 asset_type,
                 expired,
                 last_modified,
                 category_id,
                 publisher,
                 language_code,
                 feed_url):

        self.code = code
        self.name = name
        self.asset_type = asset_type
        self.expired = expired
        self.last_modified = last_modified
        self.category_id = category_id
        self.publisher = publisher
        self.language_code = language_code
        self.feed_url = feed_url

    def __str__(self):

        display = "Code: {0}, Name: {1}, Asset Type:{2}"
        display += "Expired: {3}, Last Modified: {4}, Category ID: {5}"
        display += "Publisher: {6}, Language Code: {7}"

        return display.format(
            self.code,
            self.name,
            self.asset_type,
            self.expired,
            self.last_modified,
            self.category_id,
            self.publisher,
            self.language_code
        )


class Territory:

    def __init__(self, code, name):

        self.code = code,
        self.name = name

    def __str__(self):

        display = "Territory[Code: {0}, Name: {1}]"

        return display.format(
            self.code,
            self.name
        )


class Pricing:

    def __init__(self,
                 name,
                 rate,
                 currency,
                 licensed_territories=[]):

        self.name = name
        self.rate = rate
        self.currency = currency
        self.licensed_territories = licensed_territories

    def __str__(self):

        display = "Pricing[Name:{0}, Rate:{1}, "
        display += "Licensed Territories: {2}]"

        return display.format(
            self.name,
            self.rate,
            len(self.licensed_territories)
        )


class Media:

    def __init__(self,
                 content_type,
                 mime_type,
                 width,
                 height,
                 location,
                 name):
        self.content_type = content_type
        self.mime_type = mime_type
        self.width = width
        self.height = height
        self.location = location
        self.name = name

    def __str__(self):

        display = "Media[Content Type: {0}, Mime Type: {1}, "
        display += "Width: {2}, Height: {3}, Location: {4}, "
        display += "Name: {5}]"

        return display.format(
            self.content_type,
            self.mime_type,
            self.width,
            self.height,
            self.location,
            self.name
        )


class Resource:

    def __init__(self, last_modified, medias=[]):

        self.last_modified = last_modified
        self.medias = medias

    def __str__(self):

        return "Resource[Last Modified: {0}, Medias: {1}]".format(
            self.last_modified,
            len(self.medias)
        )


class File:

    def __init__(self,
                 mime_type,
                 download_sequence,
                 size,
                 name,
                 location):

        self.mime_type = mime_type
        self.download_sequence = download_sequence
        self.size = size
        self.name = name
        self.location = location

    def __str__(self):

        display = "File[Mime Type: {0}, Download Sequence: {1},"
        display += "Size: {2}, Name: {3}, Location: {4}]"

        return display.format(
            self.mime_type,
            self.download_sequence,
            self.size,
            self.name,
            self.location
        )


class Handset:

    def __init__(self,
                 handset_id,
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


class SupportedLanguage:

    def __init__(self, code, name):

        self.code = code
        self.name = name

    def __str__(self):

        display = "SupportedLanguage[Code:{0}, Name:{1}]"

        return display.format(self.code, self.name)


class Binary:

    def __init__(self,
                 last_modified,
                 binary_id,
                 files=[],
                 handsets=[],
                 supported_languages=[]
                 ):
        self.last_modified = last_modified
        self.binary_id = binary_id
        self.files = files
        self.handsets = handsets
        self.supported_languages = supported_languages

    def __str__(self):

        display = "Binary[Last Modified: {0}, ID: {1}, Files: {2}"
        display += "Handsets: {3}]"

        return display.format(
            self.last_modified,
            self.binary_id,
            len(self.files),
            len(self.handsets)
        )


class DescriptionLanguage:

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):

        display = "DescriptionLanguage[Code:{0}, Name:{1}]"

        return display.format(self.code, self.name)


class ProductDetail:

    def __init__(self,
                 product_code,
                 product_name,
                 last_modified,
                 description_language,
                 title,
                 short_description,
                 long_description,
                 sms_description,
                 category,
                 asset_type,
                 instructions,
                 publisher,
                 copyright_1,
                 copyright_2,
                 pricing,
                 resource,
                 binary
                 ):

        self.product_code = product_code
        self.product_name = product_name
        self.last_modified = last_modified
        self.description_language = description_language
        self.title = title
        self.short_description = short_description
        self.long_description = long_description
        self.sms_description = sms_description
        self.category = category
        self.asset_type = asset_type
        self.instructions = instructions
        self.publisher = publisher
        self.copyright_1 = copyright_1
        self.copyright_2 = copyright_2
        self.pricing = pricing
        self.resource = resource
        self.binary = binary

