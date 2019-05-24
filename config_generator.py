import json


def generate_config_file(server_list):
    # 生成配置文件
    config = {
        "configs": server_list,
        "localPort": 1080,
        "shareOverLan": False
    }
    with open('gui-config.json', 'w') as f:
        json.dump(config, f, ensure_ascii=False)
