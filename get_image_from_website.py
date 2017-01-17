import urllib.request
import re
import chardet



def get_html(url):
    '''
    Get the source code of a webpage
    '''
    response = urllib.request.urlopen(url)
    data = response.read()
    charset = chardet.detect(data).get('encoding')
    html = data.decode(charset)
    return html

def get_img(html):
    '''
    '''
    re_str = r'src="(.*\.jpg)"\s+'
    re_str1 = r'src=(\/.*\.jpg)'
    re_str2 = r'https:[^\s]*?(jpg|png|gif)'
    pattern = re.compile(re_str2)
    image_list = pattern.findall(html)

    for image in image_list:
        print(image)

html = get_html(r'https://www.douban.com/')
get_img(html)
# res = urllib.request.urlopen(r'http://img.sccnn.com/simg/339/18561.jpg')
# with open(r'C:\Users\okieM\Desktop\python\image1.jpg', 'wb') as f:
#     f.write(res.read())
