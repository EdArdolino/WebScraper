from requests_html import HTMLSession

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)


    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first = True).text,
        'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first = True).text

    }
    print(product)
    return product

getPrice('https://www.amazon.com/DJI-Mavic-Mini-More-Combo/dp/B07ZJZQQ8K/ref=sr_1_3?crid=1BTJ2SVI54EW&dchild=1&keywords=mavic+mini&sprefix=mavic+m%2Caps%2C184&sr=8-3')