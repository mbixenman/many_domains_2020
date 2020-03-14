import pandas as pd
import os
from urllib.request import urlopen
import time
from tld import get_tld, get_fld # we can use these to get rid of subdomain names


if not os.path.exists("domain_html"):
	os.mkdir("domain_html")

df = pd.read_csv("domains.csv")

# for link in df['domain_name']:
# 	print("original: ", link)
# 	print("fld version: ", get_fld('http://' + link))

for link in df['domain_name']:
	f = open('domain_html/' + link, "wb")
	try:
		print("Downloading (first attempt): ", link)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
		fld_link = get_fld('http://' + link)
		request_link = "http:www." + fld_link
		req = Request(url=link, headers=headers)
		response = urlopen(req)
		html = response.read()
		f.write(html)
		f.close()
	except:
		print("Downloading (second attempt): ", link)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
		fld_link = get_fld('http://' + link)
		request_link = "http://" + fld_link
		req = Request(url=link, headers=headers)
		response - urlopen(req)
		html = response.read()
		f.write(html)
		f.close()

	time.sleep(10)

