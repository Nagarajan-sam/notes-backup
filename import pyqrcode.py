import pyqrcode
url='https://www.msystechnologies.com/'
k=pyqrcode.create(url)
k.svg('Qr.svg',scale=10)