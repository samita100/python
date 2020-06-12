import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random


# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

url = "https://github.com/rock6064/text/blob/master/text.txt"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

rohan = soup.find(id="LC1").text
print(rohan)

os = ["Windows", "OS X"]
selected_os = random.choice(os)
print(selected_os)


if selected_os == "Windows":
  os_version = ['10','8.1','8','7']
  selected_os_version = random.choice(os_version)
  print(f'Selected OS Version:- {selected_os_version}')
else:  
  os_versions = ['Catalina', 'Mojave', 'High Sierra', 'Sierra']
  selected_os_version = random.choice(os_versions)
  print(f'Selected OS Version:- {selected_os_version}')




versions = ['79.0', '78.0', '77.0', '76.0', '75.0', '74.0', '73.0', '72.0', '71.0', '70.0', '69.0', '68.0', '67.0', '66.0', '65.0', '64.0', '63.0', '62.0', '61.0', '60.0']
selected_version = random.choice(versions)



print(f'Selected Browser Version:- {selected_version}')

desired_cap = {
 'browser': 'Chrome',
 'browser_version': selected_version,
 'os': selected_os,
 'os_version': selected_os_version,
 'resolution': '1920x1080',
 'name': 'Bstack-[Python] Sample Test'
}

driver = webdriver.Remote(
    command_executor=rohan,
    desired_capabilities=desired_cap)




driver.maximize_window()



driver.get("https://www.instagram.com/fnatic_ron/")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 300)")
time.sleep(1)
driver.find_element_by_link_text("bitcoin-paradise.web.app").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.execute_script("window.scrollTo(0, 250)")
time.sleep(8)
driver.execute_script("window.scrollTo(0, 310)")
time.sleep(6)
driver.execute_script("window.scrollTo(0, 350)")
time.sleep(6)
driver.execute_script("window.scrollTo(0, -500)")
time.sleep(7)
driver.find_element_by_link_text("Get started with Bitcoin").click()
time.sleep(4)








driver.quit()
