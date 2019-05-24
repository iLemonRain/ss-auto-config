#!/usr/bin/python3
import spider
import ocr
import text_processor
import config_generator
import pprint

if __name__ == '__main__':
    print('正在抓取免费账号图片...')
    img_name = spider.get_png()
    print('免费账号图片抓取完成')
    print('正在识别图片中的文本...')
    text = ocr.png_to_text(img_name)
    print('文本识别完成')
    print('正在生成服务器列表...')
    server_list = text_processor.generate_server_list(text)
    print('服务器列表生成完毕')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(server_list)
    print('正在生成配置文件...')
    config_generator.generate_config_file(server_list)
    print('gui-config.json 已生成')
