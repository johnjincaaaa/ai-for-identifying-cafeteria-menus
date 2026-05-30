import time
import requests
from DrissionPage import ChromiumPage

page = ChromiumPage()

page.get("https://cn.bing.com/images/search?q=口水鸡&form=IRFLTR&first=1")
time.sleep(3)
page.run_js('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(2)
images = page.eles(r'xpath://div[@class="img_cont hoff"]/img')
print(len(images))
index = 1
for image in images:
    print(image.attr('src'))
    try:
        resp = requests.get(image.attr('src'))
        with open(f'dataset/images/train/g{index}.jpg','wb')as f:
            f.write(resp.content)
        index = index + 1
    except:
        pass


input("jdwoi")