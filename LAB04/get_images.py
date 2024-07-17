import os
import requests
from bs4 import BeautifulSoup

pageTarget = 'https://xe.chotot.com/mua-ban-xe-may-yamaha-sdmb2?q=xe%20may'
page = requests.get(pageTarget)
soup = BeautifulSoup(page.content, 'html.parser')
wrapper = soup.find('body')

images = wrapper.find_all("img")
downloadPath = 'yamaha/'

if not os.path.exists(downloadPath):
    os.makedirs(downloadPath)

for image in images:
    imgData = image['src']
    filename = imgData.split('/')[-1]

    try:
        response = requests.get(imgData)
        response.raise_for_status()  # Raise an HTTPError if the response was unsuccessful
    except requests.exceptions.RequestException as e:
        print(f"Could not download image {imgData}. Reason: {e}")
        continue

    file_path = os.path.join(downloadPath, filename)

    try:
        with open(file_path, "wb") as file:
            file.write(response.content)
    except Exception as e:
        print(f"Could not write to file {file_path}. Reason: {e}")