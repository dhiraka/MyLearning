import re
import rstr
import grequests
import csv


def generate_list_of_mail_ids_and_save_to_text_file(no_of_ids, text_file_address):
    if not isinstance(no_of_ids, int):
        return
    f = open(text_file_address, "rw+")
    f.seek(0, 0)
    for i in range(no_of_ids):
        mail = rstr.xeger(r'\w[\w\.-]*@\w[\w\.-]+\.\w+')
        f.write(mail + "\n")
    f.close()


generate_list_of_mail_ids_and_save_to_text_file(100, "mail_list.txt")


def read_mail_list(text_file_address):
    with open(text_file_address) as f:
        content = f.readlines()
    return content


def validate_and_write_to_file(lst):
    mail_info = {}
    url_params = {}
    for mail_id in lst:
        mail_info[mail_id] = {}
        mail_info[mail_id][urls] = []
    url_lst = []
    for dictn in mail_info.values():
        url_lst.append(dictn[urls])

    rs = [grequests.get(uri, params=url_params, timeout=120)
          for uri in url_lst if uri]
    responses = grequests.map(rs, size=5)

    for response in responses:
        if response is None:
            continue
        json_response = response.json()

    # Process the data here and get the values

    with open('result.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(
            ["mail_id", "domain_verification_strng",
             "email_verification_strng", "domain_start_date"])

validate_and_write_to_file([])
