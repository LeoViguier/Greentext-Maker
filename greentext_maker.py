# -*- coding: utf-8 -*-
import os
from PIL import Image
from datetime import datetime
import random
from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
import requests

def get_image_data(image_path):
    """
    Returns the image data of the image at the given path.
    """
    image = Image.open(image_path)
    height = image.height
    width = image.width
    size = int(os.path.getsize(image_path) / 1024)
    file_info = f"({size} KB, {width}x{height})"

    if height > 150:
        width = int(width * 150 / height)
        height = 150
    
    if width > 250:
        height = int(height * 250 / width)
        width = 250
    
    
    return (height, width, file_info)


def get_date():
    now = datetime.now()
    year = str(now.year)[2:]
    part_a = datetime.now().strftime("%m/%d")
    part_b = datetime.now().strftime("%H:%M:%S")
    part_c = now.strftime("%A")[:3]
    return f"{part_a}/{year}({part_c}){part_b}"


def get_path():
    files = os.listdir(f"./screenshots")
    if files != []:
        latest = max(files, key=lambda x: x.split("_")[1].split(".")[0])
        latest_int = int(latest.split("_")[1].split(".")[0]) + 1
        new_path = f"./screenshots/result_{latest_int}.png"
    else:
        new_path = f"./screenshots/result_1.png"

    return new_path


def create_blockquote(rtext):
    lines = rtext.split("\n")
    ret = []
    for i in lines:
        if i.startswith(">"):
            ret.append(f'<span class="quote">{i}</span>')
        else:
            ret.append(i)
    
    final = "<br>".join(ret)
    final.replace(">", "&gt;")

    return final


def greentext(message):
    elements = message.split(';')
    post_subject = elements[0]
    image = elements[1]
    text = elements[2]

    image_name = image.split("/")[-1]
    
    # download the picture
    r = requests.get(image, stream=True)
    with open(f'./pictures/{image_name}', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)

    path = get_path()

    blockquote = create_blockquote(text)
    height, width, file_info = get_image_data(f'./pictures/{image_name}')
    date = get_date()

    with open("./web/index_source.html", "r") as f:
        file = f.read()


    file = file.replace("[FILE_NAME]", image_name)
    file = file.replace("[FILE_PATH]", os.path.abspath(f'./pictures/{image_name}'))
    file = file.replace("[FILE_INFO]", file_info)
    file = file.replace("[IMAGE_HEIGHT]", str(height))
    file = file.replace("[IMAGE_WIDTH]", str(width))
    file = file.replace("[POST_SUBJECT]", post_subject)
    file = file.replace("[DATE]", date)
    file = file.replace("[RANDOM_INT_REPLY]", str(random.randint(10000000, 99999999)))
    file = file.replace("[BLOCKQUOTE]", blockquote)

    with open("./web/index.html", "w") as f:
        f.write(file)
    
    cwd = os.getcwd()
    URL = f"file://{cwd}/web/index.html"

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = wb.Chrome(options=chrome_options)

    driver.set_window_size(800, 600)
    driver.get(URL)
    el = driver.find_element_by_tag_name('body')
    el.screenshot(path)
    driver.quit()

    return path


def main():
    with open("text.txt", "r") as f:
        rtext = f.read()
    path = greentext(rtext)
    print("Your greentext is located at:", os.path.abspath(path))

if __name__ == "__main__":
    main()

