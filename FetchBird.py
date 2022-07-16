from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

# Specify git folder path
git_local_path = 'D:/资料/Github/JellyCatBirding/'

# import time
# start = time.time()

#chromdriver: version 103
driver = webdriver.Chrome(git_local_path + 'chromedriver.exe')

# Fetch bird list
birdtofetch = pd.read_csv(git_local_path + 'BirdURL.csv')

stockstatuses = []
urls = birdtofetch["URL"]

for url in urls:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,"html.parser")
        
        ## Locate Stock Status on the page
        mainclass_tags = soup.find('span', {'class':"inline-block align-left"})
        stockstatuses.append(mainclass_tags.get_text())

driver.quit()

birdtofetch['Status'] = stockstatuses

print(birdtofetch)

# # # end = time.time()
# # # print("Time Elapsed: "+str(end - start))
