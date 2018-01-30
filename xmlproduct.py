import xmltodict, time
from object_products import (generate_product, Territory, PriceClass, Media, Resource, Handset, Category, File, Binary, SupportedLanguage, Product)
from helpers import xml_by_url, download_apk, download_image

if __name__ == "__main__":
#    url = 'http://cmserver.spoiledmilk.com/ContentManagement/xmlFeed?action=88&productCode=9082'
#    doc_prod = xml_by_url(url)
#    product = generate_product(doc_prod['product'])

    codes = [
        #'29237', //NO BINARY TAG
        '29151',
        '9139',
        '28967',
        '28563',
        '9754',
        '11910',
        '22483',
        '29031',
        '28288',
        '28970',
        '28486',
        '29248',
        '27451',
        '27775',
        '28759',
        '28701',
        '29312',
        '10929',
        '21811',
        '28895',
        '29295',
        '8102',
        '27948',
        '26472',
        '28889',
        '29150',
        '27316',
        '8930',
        '9549',
        '29314',
        '10035',
        '10046',
        '11575',
        '11587',
        '9879',
        '9889',
        '9862',
        '9870',
        '28488',
        '28614',
        '28900',
        '29313',
        '10252',
        '21994',
        '10092',
        '28224',
        '10253',
        '21992',
        '10484',
        '21985',
        '5955',
        '28222',
        '29320',
        '26542',
        '29306',
        '28989',
        '20703',
        '10780',
        '7083',
        '25548',
        '22395',
        '26497',
        '28781',
        '7141',
        '28521',
        '28262',
        '28864',
        '24852',
        '28913',
        '8295',
        '8204',
        '25740',
        '27040',
        '26612',
        '28700',
        '22546',
        '22810',
        '26786',
        '9795',
        '29161',
        '10809',
        '10307',
        '29290',
        '7145',
        '9550',
        '10782',
        '21245',
        '24092',
        '9481',
        '29299',
        '29287',
        '10750',
        '29277',
        '29276',
        '27518',
        '29281',
        '29274',
        '29198',
        '27751',
        '28173',
        '27519',
        '29275',
        '27532',
        '28017',
        '29007',
        '29273',
        '29300',
        '28018',
        '29278',
        '27666',
        '27750',
        '29241',
        '29297',
        '29296',
        '27667',
        '27520',
        '29200',
        '27533',
        '29004',
        '29239',
        '27594',
        '29201',
        '27753',
        '27580',
        '27531',
        '27772',
        '27589',
        '29265',
        '29006',
        '27593',
        '9600',
        '10480',
        '7533',
        '7319',
        '7298',
        '7532',
        '10566',
        '28743',
        '26614',
        '26160',
        '9838',
        '28684',
        '28910',
        '11691',
        '19950',
        '10031',
        '27743',
        '11167',
        '26409',
        '26162',
        '26009',
        '26615',
        '24845',
        '10905',
        '27347',
        '29301',
        '9680',
        '10666',
        '25080',
        '29049',
        '11692',
        '27984',
        '27315',
        '28528',
        '27851',
        '9728',
        '29152',
        '27317',
        '29191',
        '29209',
        '10033',
        '22707',
        '27345',
        '10659',
        '10598',
        '24385',
        '19970',
        '28902',
        '28816',
        '29280',
        '24846',
        '23936',
        '29188',
        '28990',
        '29242',
        '29156',
        '24409',
        '27340',
        '4998',
        '4999',
        '5011',
        '5012',
        '4996',
        '4995',
        '4993',
        '28066',
        '10735',
        '10921',
        '7705',
        '10738',
        '10268',
        '9431',
        '9433',
        '9458',
    ]

    for code in codes:
        url = 'http://cmserver.spoiledmilk.com/ContentManagement/xmlFeed?action=88&productCode=' + code
        doc_prod = xml_by_url(url)
        product = generate_product(doc_prod['product'])
        print("READ XML SUCCESSFUL")

        files = product.binary.files
        for file in files:
            print("Start!")
            print(file.file_attr.mime_type)
            print(file.file_attr.download_sequence)
            print(file.file_attr.size)
            print(file.name)
            print(file.location) # Download apk here
            download_apk(file, 'files/apk/')
            print("Wait 5 secs")
            print("===========================")
            time.sleep(5)

"""
    single_fieldnames = [
        'product_code', 
        'product_name', 
        'last_modified', 
        'xsi_schema_location', 
        'xmlns_xsi',
        'description_language',
        'description_language_code',
        'description_language_name',
        'title',
        'short_description',
        'title',
        'short_description',
        'long_description',
        'sms_description',
        'category_id',
        'category_is_adult',
        'category_text',
        'asset_type',
        'instructions',
        'objective_description',
        'publisher',
        'copyright1',
        'copyright2',
        'price_class_name',
        'price_class_rate',
        'price_class_currency',
        'resource_last_modified',
    ]

    single_row = {
        'product_code': product.product_attr.product_code, 
        'product_name': product.product_attr.product_name, 
        'last_modified': product.product_attr.last_modified, 
        'xsi_schema_location': product.product_attr.xsi_schema_location, 
        'xmlns_xsi': product.product_attr.xmlns_xsi,
        'description_language_code': product.description_language_attr.code,
        'description_language_name': product.description_language_attr.name,
        'title': product.title,
        'short_description': product.short_description,
        'long_description': product.long_description,
        'sms_description': product.sms_description,
        'category_id': product.category.category_attr.id ,
        'category_is_adult': product.category.category_attr.is_adult,
        'category_text': product.category.text,
        'asset_type': product.asset_type,
        'instructions': product.instructions,
        'objective_description': product.objective_description,
        'publisher': product.publisher,
        'copyright1': product.copyright1,
        'copyright2': product.copyright2,
        'price_class_name': product.price_class.price_class_attr.name,
        'price_class_rate': product.price_class.rate,
        'price_class_currency': product.price_class.currency,
        'resource_last_modified': product.resource.resource_attr.last_modified,
    }

    print(single_row)

    territory_fieldnames = [
        'territory_code',
        'territory_name'
    ]

    territory_row_list = []
    territories = product.price_class.territories
    for territory in territories:
        territory_row = {}
        territory_row['territory_name'] = territory.territory_attr.name
        territory_row['territory_code'] = territory.territory_attr.code
        territory_row_list.append(territory_row)

    print(territory_row_list)

    media_fieldnames = [
        'media_content_type',
        'media_mime_type',
        'media_width',
        'media_height',
        'media_name',
        'media_location'
    ]  

    media_row_list = []
    medias = product.resource.medias
    for media in medias:
        media_row = {}
        media_row['media_content_type'] = media.media_attr.content_type
        media_row['media_mime_type'] = media.media_attr.mime_type
        media_row['media_width'] = media.media_attr.width
        media_row['media_height'] = media.media_attr.height
        media_row['media_location'] = media.location # Download image here
        media_row['media_name'] = media.name
        #download_image(media, 'files/{}/images/'.format(product.title))
        media_row_list.append(media_row)
        #time.sleep(5)

    print(media_row_list)

    file_fieldnames = [
        'file_mime_type',
        'file_download_sequence',
        'file_size',
        'file_name',
        'file_location'
    ]

    file_row_list = []
    files = product.binary.files
    for file in files:
        file_row = {}
        file_row['file_mime_type'] = file.file_attr.mime_type
        file_row['file_download_sequence'] = file.file_attr.download_sequence
        file_row['file_size'] = file.file_attr.size
        file_row['file_name'] = file.name
        file_row['file_location'] = file.location # Download apk here
        #download_apk(file,files/{}/apk/'.format(product.title))
        file_row_list.append(file_row)
        #download_apk(file, 'files/apk/')
        #time.sleep(5)

    print(file_row_list)

    handset_fieldnames = [
        'handset_id',
        'handset_make',
        'handset_model',
        'handset_groupid',
        'handset_useragent'
    ]

    handset_row_list = []
    handsets = product.binary.handsets
    for handset in handsets:
        handset_row = {}
        handset_row['handset_id'] = handset.handset_id
        handset_row['handset_make'] = handset.make
        handset_row['handset_model'] = handset.group_id
        handset_row['handset_useragent'] = handset.user_agent
        handset_row_list.append(handset_row)

    print(handset_row_list)

    supported_language_fieldnames = [
        'supported_language_name',
        'supported_language_code'
    ]

    supported_language_row_list = []
    supported_languages = product.binary.supported_languages
    for supported_language in supported_languages:
        supported_language_row = {}
        supported_language_row['supported_language_code'] = supported_language.supported_language_attr.code
        supported_language_row['supported_language_name'] = supported_language.supported_language_attr.name
        supported_language_row_list.append(supported_language_row)

    print(supported_language_row_list)
"""