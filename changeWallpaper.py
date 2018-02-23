import os,signal,re
import urllib.request,requests
import ctypes,sys,time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
search_string=""
if len(sys.argv) > 1:
    search_string = ' '.join(sys.argv[1:])
browser=webdriver.PhantomJS()
if(search_string==""):
	url="https://www.bing.com"
	try:
		page=urllib.request.urlopen(url)
	except:
		sys.exit("Internet Connection problem")
	html_content=str(page.read())
	html_content=html_content.split(",")
	for content in html_content:
		match=re.search(r"g_img={url:(.*jpg)",content)
		if match:
			img_url=match.group(1).replace('"','').strip()
			try:
				img_url.index("//")
				address=img_url
			except:
				address=url+img_url
else:
	try:
		browser.get("https://images.search.yahoo.com")
		search=browser.find_element_by_name("p")
	except:
		sys.exit("Internet Connection Problem")
	search.send_keys(search_string)
	search.submit()
	#search.send_keys("{}".format(search_string) + Keys.RETURN)
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="resitem-0"]/a').click()
	time.sleep(2)
	try:
		browser.find_element_by_link_text("View Image").click()
	except NoSuchElementException:
		assert 0, "View Image"
		browser.close()
	time.sleep(3)
	address=browser.current_url
img_data=urllib.request.urlretrieve(address,"image.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\polaris\AppData\Local\Programs\Python\Python36-32\image.jpg" , 0)
#browser.service.process.send_signal(signal.SIGTERM)
browser.close()
