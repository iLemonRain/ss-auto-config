from difflib import SequenceMatcher

default_method = "aes-256-cfb"
default_password = b"\x64\x6f\x6e\x67\x74\x61\x69\x77\x61\x6e\x67\x2e\x63\x6f\x6d"  # noqa E501


# 计算相似度
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# 提取文本中的信息
def extract_info(text):
    # 去掉冗余信息
    server_info_list = text.split()
    server_info_list = [x for x in server_info_list if ':' in x]
    return server_info_list


def genereate_server(server_info_list):
    server = {}
    extracted_password = server_info_list[2].split(':')[1].lower()
    extracted_method = server_info_list[3].split(':')[1].lower()
    server["remarks"] = server_info_list[0].split(':')[0]
    server["server"] = server_info_list[0].split(':')[1]
    server["server_port"] = int(server_info_list[1].split(':')[1])
    server["password"] = str(default_password, 'utf-8') if similar(
        str(default_password, 'utf-8'), extracted_password) >= 0.8 else extracted_password  # noqa E501
    server["method"] = default_method if similar(
        default_method, extracted_method) else extracted_method
    return server


# 生成服务器列表
def generate_server_list(text):
    server_info_list = extract_info(text)
    server1 = genereate_server(server_info_list[:4])
    server2 = genereate_server(server_info_list[-6:-2])
    return [server1, server2]
