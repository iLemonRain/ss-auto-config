import os
import re


def png_to_text(img_name):
    # 识别图片中的文本
    cmd = 'tesseract -l chi_sim --psm 4 {} stdout'.format(img_name)
    raw_text = os.popen(cmd).read().strip()
    # 对图片中的文本进行格式化
    formated_text = raw_text.replace(". ", ".").replace(": ", ":")
    formated_text = re.sub(r" +", "\t", formated_text)
    return formated_text
