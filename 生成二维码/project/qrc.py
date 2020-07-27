import qrcode
from PIL import Image

def url(url):
    img =qrcode.make(url) # 生成二维码图片对象
    img.save('static/qrimg/1.png') # 保存二维码
    return 'static/qrimg/1.png'