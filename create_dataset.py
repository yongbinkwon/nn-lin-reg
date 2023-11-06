import os
import requests  # Don't forget to import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time

def fetch_images(query, num_images, save_dir):
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    driver = webdriver.Chrome()
    driver.get(url)

    # Scroll down to load images
    image_count = 0
    while image_count < num_images:
        # Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Adjust as needed

        # Capture image tags
        img_tags = driver.find_elements(By.CSS_SELECTOR, "img.rg_i")

        for img_tag in img_tags:
            try:
                # Get the image source URL
                img_url = img_tag.get_attribute("src")
                if not img_url:
                    img_url = img_tag.get_attribute("data-src")

                if img_url:
                    # Download and process the image
                    img_name = os.path.join(save_dir, f"{query}_{image_count}.jpg")
                    response = requests.get(img_url)
                    with open(img_name, "wb") as f:
                        f.write(response.content)

                    # Resize and convert to black and white
                    img = Image.open(img_name)
                    img = img.resize((64, 64))
                    img = img.convert("L")
                    img.save(img_name)

                    print(f"Downloaded {img_name}")
                    image_count += 1
            except Exception as e:
                print(f"Error processing image: {e}")

    driver.quit()

if __name__ == "__main__":
    query = "face"
    num_images = 100  # Adjust as needed
    save_dir = "./human"

    fetch_images(query, num_images, save_dir)
