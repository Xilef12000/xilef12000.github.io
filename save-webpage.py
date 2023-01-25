# save-webpage.py

import urllib.request, urllib.error
from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from time import sleep
import os

elements_href = ['a', 'link']
elements_src = ['img', 'script']

urls = ['http://localhost:3000/', 'http://localhost:3000/404', 'http://localhost:3000/sitemap.txt', 'http://localhost:3000/robots.txt']
server = 'http://localhost:3000'
parsed = []
while True:
    br = True
    #print(urls)
    for url in urls:
        if url not in parsed:
            print(url)
            br = False
            parsed.append(url)
            if url.endswith("/"):
                url += "index"
            path = urlparse(url).path
            try:
                response = urllib.request.urlopen(url)
            except Exception as e:
                print(e)
            webContent = response.read()
            soup = BeautifulSoup(webContent, 'lxml')
            if response.info().get_content_type() == "text/html":
                for element in elements_href:
                    for link in soup.findAll(element):
                        href = link.get('href')
                        if href and not href.startswith('http://') and not href.startswith('https://') and not href.startswith('#'):
                            #print(server + href)
                            urls.append(urljoin(url, href))
                for element in elements_src:
                    for link in soup.findAll(element):
                        href = link.get('src')
                        if href and not href.startswith('http://') and not href.startswith('https://') and not href.startswith('#'):
                            #print(server + href)
                            urls.append(urljoin(url, href))
            elif response.info().get_content_type() == "text/css":
                decoded = webContent.decode("utf-8")
                css = decoded.split(';\n', 10)
                for c in css:   
                    if c.find('@import') != -1:
                        urls.append(urljoin(url,c.split('"', 2)[1]))
                if decoded.find('@font-face') != -1:
                    fonts = decoded.split('url')
                    for font in fonts:
                        if font[:1] == '(':
                            #print(font.split(')')[0].replace('(', '').replace("'", ''))
                            urls.append(urljoin(url,font.split(')')[0].replace('(', '').replace("'", '')))
            if path.find('.') != -1:
                file = "docs/{}".format(path)
            else:
                file = "docs/{}.html".format(path)
            print("        "+file)

            os.makedirs(os.path.dirname(file), exist_ok=True)
            f = open(file, 'wb')
            f.write(webContent)
            f.close
    if br == True:
        break

sleep(5)
#print(urls)
#print(parsed)