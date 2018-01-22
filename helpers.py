import requests, xmltodict, shutil, time, zipfile


"""
TODO: Make a script to download files and apk, and print
the Data from the XML.

**So far, items with URL is file (under binary), and media (under resource)
"""


def download_image(url, destination, name):
    response = requests.get(url, stream=True)

    with open(destination, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    print("Image {} - download success!".format(name))


def download_zip(url, destination):

    with requests.get(url, stream=True) as response, open(destination, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        with zipfile.ZipFile(destination) as zf:
            zf.extractall()

    print("File {} - download success!".format(destination))


def get_xml_by_url():
    """

    :return:
    """
    pass


def xml_to_ordered_dict(filename):
    """

    :param filename:
    :return: OrderedDict
    """
    try:
        with open(filename) as fd:
            result = xmltodict.parse(fd.read())
    except FileNotFoundError:
        print("Error: FileNotFoundError")
        return

    return result


def assign_values_to_objects(dictionary):
    """

    :param dictionary:
    :return:
    """
    for key, value in dictionary.items():
        if isinstance(value, dict):
            assign_values_to_objects(value)
        else:
#            if isinstance(value, list):
#                for item in value:
#                    if isinstance(item, dict):
#                        assign_values_to_objects(item)
            print("{0}: {1}".format(key, value))


if __name__ == '__main__':
    doc_prod = xml_to_ordered_dict('example_product.xml')
    assign_values_to_objects(doc_prod)
