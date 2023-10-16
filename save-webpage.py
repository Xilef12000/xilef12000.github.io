# save-webpage.py

import urllib.request, urllib.error
from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from time import sleep
import os
import argparse
import json
from pathlib import Path

script_dir = os.path.dirname(__file__)

parser = argparse.ArgumentParser(
                    prog='save-webpage.py',
                    description='render any webpage into a static webpage',
                    epilog='or see the README.md file')
parser.add_argument("-c", "--configfile", required=True, help="relative path to condig .json file")
parser.add_argument("-f", "--fast", action='store_const', default=False, const=True, help="fast render mode: only files already in db will be parsed")

args = parser.parse_args()

f = open(os.path.join(script_dir, args.configfile))
config = json.load(f)
f.close()

elements_href = config["elements_href"]
elements_src = config["elements_src"]

urls = config["start_urls"]

if args.fast:
    print("fast mode")
    Path(os.path.join(script_dir, config["db"])).touch()
    #print(os.stat(os.path.join(script_dir, config["db"])).st_size)
    if os.stat(os.path.join(script_dir, config["db"])).st_size != 0:
        #print("not emty")
        f = open(os.path.join(script_dir, config["db"]))
        db_in = json.load(f)
        f.close()
        #print(db_in)
        for url in db_in["parse"]:
                urls.append(url)
        #print(urls)

server = config["server"]
parsed = []
while True:
    br = True
    #print(urls)
    for url in urls:
        if url not in parsed:
            #print(url)
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
            if not args.fast:
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
                file = "{}{}".format(config["out_dir"],path)
            else:
                file = "{}{}.html".format(config["out_dir"],path)
            #print("        "+file)

            os.makedirs(os.path.dirname(file), exist_ok=True)
            f = open(file, 'wb')
            f.write(webContent)
            f.close
    if br == True:
        break

sleep(1)

db_out = {
    "parse":parsed
}
db_out_obj = json.dumps(db_out, indent=4)
with open(config["db"], "w") as outfile:
    outfile.write(db_out_obj)