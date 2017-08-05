from urllib import request

goog_url = "http://www.google.com/finance/historical?q=NASDAQ%3AGOOG&ei=zvEnWfHUHYeDUcmql-gM&output=csv"

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_urlstr = str(csv)
    links = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url,"w")
    for line in lines:
            fx.write(line + "\n")
            fx.close()

download_stock_data(goog_url)