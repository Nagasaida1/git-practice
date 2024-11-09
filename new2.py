import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Use the appropriate driver for your browser

# URL of the artist's page
url = "https://www.jiosaavn.com/artist/s.-p.-balasubrahmanyam-songs/Ix5AC5h7LSg_"
driver.get(url)

# Wait for the page to load
time.sleep(3)

# Load more songs
while True:
    try:
        load_more_button = driver.find_element(By.XPATH, "//button[text()='Load more']")
        load_more_button.click()
        time.sleep(2)  # Wait for songs to load
    except Exception:
        print("No more songs to load or encountered an error.")
        break

# Now get all song links
soup = BeautifulSoup(driver.page_source, 'html.parser')
song_links = [a['href'] for a in soup.select('a[href*="/song/"]')]

# Convert relative links to absolute links
base_url = "https://www.jiosaavn.com"
absolute_song_links = [urljoin(base_url, link) for link in song_links]

# Count songs with "Aditya Music" copyright
aditya_music_count = 0

for song_link in absolute_song_links:
    driver.get(song_link)
    time.sleep(2)  # Wait for the song page to load
    
    # Scrape copyright information
    song_soup = BeautifulSoup(driver.page_source, 'html.parser')
    copyright_info = song_soup.find(text=lambda text: "©" in text or "℗" in text)

    if copyright_info and 'Aditya Music' in copyright_info:
        aditya_music_count += 1

# Print the final count
print(aditya_music_count)

# Close the driver
driver.quit()
