import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service('C:\\path\\to\\chromedriver.exe')  # Update this path
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.jiosaavn.com/artist/s.-p.-balasubrahmanyam-songs/Ix5AC5h7LSg_"
driver.get(url)

language_dropdown = driver.find_element(By.XPATH, '//div[contains(@class, "lang-filter")]//span[contains(text(), "All Languages")]')
language_dropdown.click()
time.sleep(2)

while True:
    try:
        load_more_button = driver.find_element(By.XPATH, '//button[contains(text(), "Load more")]')
        load_more_button.click()
        time.sleep(2)
    except Exception:
        break

songs = driver.find_elements(By.XPATH, '//div[@class="song-item"]')
aditya_music_count = 0

for song in songs:
    song_link = song.find_element(By.TAG_NAME, 'a').get_attribute('href')
    driver.get(song_link)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    copyright_info = soup.find('div', class_='copyright').text.strip()
    
    if "Aditya Music" in copyright_info:
        aditya_music_count += 1
    
    driver.back()
    time.sleep(2)

print(aditya_music_count)

driver.quit()
