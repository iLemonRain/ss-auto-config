import os
import re

img_name = 'ss.PNG'
cmd = 'tesseract -l chi_sim --psm 4 {} stdout'.format(img_name)
raw_text = os.popen(cmd).read().strip()
formated_text = raw_text.replace(". ", ".").replace(": ", ":")
formated_text = re.sub(r" +", "\t", formated_text)
# print(formated_text.split())
for item in formated_text.split():
    print(item.split(":"))
