import os
import re
import json


def get_avg_rtt(server):
    cmd = 'ping {host} -c 3'.format(host=server)
    ping_output = os.popen(cmd).read().strip()
    avg_rtt = ping_output.split("\n")[-1].split("/")[4]
    return '{}ms'.format(avg_rtt)


# 识别图片中的文本
img_name = 'ss.PNG'
cmd = 'tesseract -l chi_sim --psm 4 {} stdout'.format(img_name)
raw_text = os.popen(cmd).read().strip()
# 对图片中的文本进行格式化
formated_text = raw_text.replace(". ", ".").replace(": ", ":")
formated_text = re.sub(r" +", "\t", formated_text)
print(formated_text)

# 提取文本中的信息
server_array = formated_text.split()
server_array = [x for x in server_array if ':' in x]
# server1
server1_array = server_array[:4]
server1 = {}
server1["server_name"] = server1_array[0].split(':')[0]
server1["server"] = server1_array[0].split(':')[1]
server1["server_port"] = server1_array[1].split(':')[1]
server1["password"] = server1_array[2].split(':')[1].lower()
server1["method"] = server1_array[3].split(':')[1].lower()
server1["avg_ttr"] = get_avg_rtt(server1["server"])
print(server1)
# server2
server2_array = server_array[:4]
server2 = {}
server2["server_name"] = server2_array[0].split(':')[0]
server2["server"] = server2_array[0].split(':')[1]
server2["server_port"] = server2_array[1].split(':')[1]
server2["password"] = server2_array[2].split(':')[1].lower()
server2["method"] = server2_array[3].split(':')[1].lower()
server2["avg_ttr"] = get_avg_rtt(server2["server"])
print(server2)

best_server = server1 if server1["avg_ttr"] < server2["avg_ttr"] else server2

# 生成配置文件
config_template = {
    "local_address": "127.0.0.1",
    "local_port": 1080,
    "timeout": 300,
    "fast_open": False,
}
config = {**best_server, **config_template}
with open('config.json', 'w') as f:
    json.dump(config, f, ensure_ascii=False)
