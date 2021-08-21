import requests
import json
import base64
import config
import csv
import os
import sys


def main(fofa_query_base64_list, fofa_size, fofa_fields, fofa_output_file, fofa_email, fofa_key):
    tmp_list = list(fofa_fields.split(','))

    fields_list = []
    for field in tmp_list:
        if field in fields_list:
            continue
        fields_list.append(field)
    fields_list.append('fofa_query')

    print("创建{}文件".format(fofa_output_file))
    fw = open(fofa_output_file, 'w', encoding='utf-8', newline='')
    writer = csv.writer(fw)
    writer.writerow(fields_list)

    for fofa_query_base64 in fofa_query_base64_list:
        fofa_query = str(base64.b64decode(fofa_query_base64), "utf-8")
        print("正在查询语句：{}".format(fofa_query))

        current_page = 1
        total_page = 1
        total_size = 0
        while current_page <= total_page:
            print("当前page：{}".format(current_page))
            print("总page：{}".format(total_page))
            api_url = "https://fofa.so/api/v1/search/all?email={}&key={}&qbase64={}&size={}&page={}&fields={}".format(fofa_email,fofa_key,fofa_query_base64,fofa_size,current_page,fofa_fields)
            print("当前请求api：{}".format(api_url))
            resp = requests.get(api_url)
            if not resp:
                break
            data_model = json.loads(resp.text)  # 将请求到的json字符串解码为python对象
            if data_model['error'] is True:
                break
            # print(data_model)
            total_size = data_model['size']
            # print(total_size)
            results = data_model['results']
            total_page = int(total_size / fofa_size) + 1 if total_size % fofa_size != 0 else int(total_size / fofa_size)
            for data in results:
                data.append(fofa_query)
                # print(data)
                writer.writerow(data)
            current_page += 1


if __name__ == '__main__':

    fofa_email = config.FOFA_EMAIL
    fofa_key = config.FOFA_KEY
    fofa_fields = config.FOFA_FIELDS
    fofa_size = config.FOFA_SIZE
    fofa_output_file = config.FOFA_OUTPUT_FILE
    fofa_read_file = config.FOFA_READ_FILE

    size = os.path.getsize(fofa_read_file)
    if size == 0:
        print("请填写fofa查询语句！")
        sys.exit()

    fofa_query_base64_list = []
    fr = open(fofa_read_file, "r", encoding="utf-8")
    for line in fr.readlines():
        fofa_query_base64 = base64.b64encode(line.strip('\n').encode("utf-8")).decode('utf-8')  # 先转换utf-8格式再加密再转回utf-8
        fofa_query_base64_list.append(fofa_query_base64)

    # print(fofa_query_base64_list)
    main(fofa_query_base64_list, fofa_size, fofa_fields, fofa_output_file, fofa_email, fofa_key)
