import xmltodict, requests, shutil, os, csv

def xml_by_url(url):
	response = requests.get(url)
	root = xmltodict.parse(response.content)
	return root

def download_apk(file, directory):

    if not os.path.exists(directory):
        os.makedirs(directory)

    destination = directory + file.name

    if not os.path.exists(destination):
        response = requests.get(file.location, stream=True)
        with open(destination, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

        print("File {} - download success!".format(destination))
    else:
        print("File {} - already exists".format(destination))

def download_image(media, directory):

    if not os.path.exists(directory):
        os.makedirs(directory)

    destination = directory + media.name

    if not os.path.exists(destination):
        response = requests.get(media.location, stream=True)
        with open(destination, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

        print("Image {} - download success!".format(destination))
    else:
        print("Image {} - already exists".format(destination))

def generate_csv1(directory, fieldnames_list, dictionary_list):

    with open(filename + '.csv', 'w') as csvfile:
        for fieldnames in fieldnames_list:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for dictionary in dictionary_list:
                for item in dictionary:
                    writer.writerow(item)

def generate_csv2(directory, fieldnames_list, dictionary_list):

    with open(filename + '.csv', 'w') as csvfile:
        for fieldnames in fieldnames_list:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for dictionary in dictionary_list:
                for item in dictionary:
                    writer.writerow(item)
