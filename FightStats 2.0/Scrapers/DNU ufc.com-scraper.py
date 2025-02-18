import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo

#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]

webnodata = db["WEBFighterNoData"]



# Launch Chrome browser and navigate to UFC athletes page
driver = webdriver.Chrome()
driver.get('https://www.ufc.com/athletes/all')

# Wait for the page to load
wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.views-element-container')))







# Click the 'load more' button twice
#for i in range(2):
#    load_more_button = driver.find_element(By.CSS_SELECTOR, '#block-mainpagecontent > div > div > div.views-element-container.block.block-views.block-views-blockall-athletes-page > div > div > ul > li > a')
#    driver.execute_script("arguments[0].click();", load_more_button)
#    time.sleep(2)
    





# Click the 'load more' button repeatedly until all fighters are loaded
while True:
    try:
        load_more_button = driver.find_element(By.CSS_SELECTOR, '#block-mainpagecontent > div > div > div.views-element-container.block.block-views.block-views-blockall-athletes-page > div > div > ul > li > a')
        driver.execute_script("arguments[0].click();", load_more_button)
        time.sleep(2)
    except:
        break












# Find all the athlete names and URLs and print them out
athlete_elements = driver.find_elements(By.CSS_SELECTOR, '.c-listing-athlete-flipcard__back')
for athlete in athlete_elements:
    name = athlete.find_element(By.CSS_SELECTOR, '.c-listing-athlete__name').text
    fighter_url = athlete.find_element(By.CSS_SELECTOR, '.c-listing-athlete-flipcard__action > a').get_attribute('href')
    
    try:
        first, last = name.strip().lower().split(maxsplit=1)
        first = first.capitalize()
        last = last.capitalize()
        name = f"{first} {last}"
    except ValueError:
        name = name.capitalize()
    
    # Open the fighter URL in a new window
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(fighter_url)
    
    # Find the fighter record, weight class, age, height, reach, and location
    try:
        record = driver.find_element(By.CSS_SELECTOR, '#block-mainpagecontent > div > div > div > div.hero-profile-wrap > div > div > div.hero-profile__info > div.hero-profile__division > p.hero-profile__division-body').text
    except:
        record = "N/A"
    
    try:
        weight_class = driver.find_element(By.CSS_SELECTOR, '#block-mainpagecontent > div > div > div > div.hero-profile-wrap > div > div > div.hero-profile__info > div.hero-profile__division > p.hero-profile__division-title').text
    except:
        weight_class = "N/A"
    
    # Find the fighter's age
    try:
        age = driver.find_element(By.CSS_SELECTOR, '#tab-panel-1 > div > div > div > div > div > div:nth-child(4) > div:nth-child(1) > div.c-bio__text > div').text
    except:
        age = "N/A"

    # Find the fighter's height
    try:
        height = driver.find_element(By.CSS_SELECTOR, '#tab-panel-1 > div > div > div > div > div > div:nth-child(4) > div:nth-child(2) > div.c-bio__text').text
    except:
        height = "N/A"

    # Find the fighter's reach
    try:
        reach = driver.find_element(By.CSS_SELECTOR, '#tab-panel-1 > div > div > div > div > div > div:nth-child(5) > div:nth-child(2) > div.c-bio__text').text
    except:
        reach = "N/A"

    # Find the fighter's location
    try:
        location = driver.find_element(By.CSS_SELECTOR, '#tab-panel-1 > div > div > div > div > div > div:nth-child(2) > div > div.c-bio__text').text
    except:
        location = "N/A"
    try:
        heightfloat = float(height)
        feet = int(heightfloat // 12)
        inches = int(heightfloat % 12)
        height = f"{feet}'{inches}\""
    except:
        height = 'N/A'
    
    if weight_class.endswith(" Division"):
        weight_class2 =  weight_class[:-9]
        weight_class = weight_class2
    
    #Fixes location capitalization
    try:
        location = location.title()
    except:
        location = location
    
    #Makes sure location is not DOB or some other stat by checking if it contains nums
    if re.search('\d', location):
        location = 'N/A'
    
    try:   
        wins, losses, draws = map(int, record.split(' ')[0].split('-'))
    except:
        wins = 'N/A'
        losses = 'N/A'
        draws = 'N/A'
    
    
    if name.endswith(' -'):
        name = name[:-2]
    
    
    #Creates a MongoDB document for each fighter
    mydict = {
        "fighterName": name,
        "fighterURL": fighter_url,
        "wins": wins,
        "loss": losses,
        "draw": draws,
        "weightClass": weight_class,
        "fighterAge": age,
        "fighterHeight": height,
        "fighterReach": reach,
        "fighterLOC": location,
    }
    
    webnodata.insert_one(mydict)
    
    # Close the current window and switch back to the main window
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# Close the browser
driver.quit()
