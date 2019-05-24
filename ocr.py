import os
import re
import json
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# 识别图片中的文本
img_name = 'ss_accounts.png'
cmd = 'tesseract -l chi_sim --psm 4 {} stdout'.format(img_name)
raw_text = os.popen(cmd).read().strip()
# 对图片中的文本进行格式化
formated_text = raw_text.replace(". ", ".").replace(": ", ":")
formated_text = re.sub(r" +", "\t", formated_text)
print(formated_text)
# 提取文本中的信息
server_array = formated_text.split()
server_array = [x for x in server_array if ':' in x]
default_password = b"\x64\x6f\x6e\x67\x74\x61\x69\x77\x61\x6e\x67\x2e\x63\x6f\x6d"
default_method = "aes-256-cfb"
# server1
server1_array = server_array[:4]
server1 = {}
extracted_password = server1_array[2].split(':')[1].lower()
extracted_method = server1_array[3].split(':')[1].lower()
server1["remarks"] = server1_array[0].split(':')[0]
server1["server"] = server1_array[0].split(':')[1]
server1["server_port"] = int(server1_array[1].split(':')[1])
server1["password"] = str(default_password, 'utf-8') if similar(
    str(default_password, 'utf-8'), extracted_password) >= 0.8 else extracted_password
server1["method"] = default_method if similar(
    default_method, extracted_method) else extracted_method
print(server1)
# server2
server2_array = server_array[-6:-2]
server2 = {}
server2["remarks"] = server2_array[0].split(':')[0]
server2["server"] = server2_array[0].split(':')[1]
server2["server_port"] = int(server2_array[1].split(':')[1])
server2["password"] = str(default_password, 'utf-8') if similar(
    str(default_password, 'utf-8'), extracted_password) >= 0.8 else extracted_password
server2["method"] = server2_array[3].split(':')[1].lower()
print(server2)

# 生成配置文件
config = {
    "configs": [server1, server2],
    "localPort": 1080,
    "shareOverLan": False
}
with open('gui-config.json', 'w') as f:
    json.dump(config, f, ensure_ascii=False)
