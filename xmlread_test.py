import requests, time
from xml.etree import ElementTree as ET

def delete_product():
    """
    Delete product if attribute 'expired' is True
    :return:
    """
    pass

product_list_tree = ET.parse('example_productList.xml')
product_list_tree_root = product_list_tree.getroot()

#for child in product_list_tree_root:
#    print(child) # Will print Element categoryList and productList

products = product_list_tree_root.find('productList')
for product in products:

    product_attrib = product.attrib
    expired = product_attrib['expired']

    if expired is True:
        #delete product in server
        #execute delete_product()
        pass
    else:
        # get more details about the product

        #feed_url = product.find('feedUrl').text
        #response = requests.get(feed_url)
        product_tree = ET.parse('example_product.xml')
        product_tree_root = product_tree.getroot()
        #print(product_tree_root)
        for child in product_tree_root:
            if child:
                print("has child")
            else:
                print("has no child")
            print(child.attrib)
            print(child.text)