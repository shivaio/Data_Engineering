import argparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import gdown
from urllib import request
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def parse_url_to_download(args):

    output_dir_video = args.output_dir_video
    output_dir_trans = args.output_dir_trans
    url = args.url

    chrome_driver_path = "./chrome_driver/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    driver.get(url)
    time.sleep(3)

    element = driver.find_element(By.CLASS_NAME, 'options')
    all_options_main = element.find_elements(By.TAG_NAME, 'span')

    for option in all_options_main:
        if option.text.__eq__('Downloads'):
            option.click()
            time.sleep(3)

    transcripts_part = driver.find_elements(By.TAG_NAME, 'h3')

    for part in transcripts_part:
        if part.text == 'Transcripts':
            part.click()
            time.sleep(3)

    drop_down_list = driver.find_elements(By.TAG_NAME, value='app-nptel-dropdown')
    trans_options_list = driver.find_elements(By.CLASS_NAME, 'pseudo-options')

    for value in drop_down_list:

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(value)).click()
        time.sleep(2)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((trans_options_list[drop_down_list.index(value)]))).click()
        time.sleep(2)

    downloads_page = driver.page_source

    soup = BeautifulSoup(downloads_page, 'lxml')

    all_html = soup.find_all(class_='assignments download-type')

    transcripts_html = soup.find(class_='assignments download-type selected')

    videos_html = None

    for option in all_html:
        headline = option.div.h3.text
        if headline == 'Videos':
            videos_html = option

    video_links = []
    transcripts_links = []

    for link in videos_html.find_all('a'):
        video_links.append(link.get('href'))

    for link in transcripts_html.find_all('a'):
        transcripts_links.append(link.get('href'))

    for link in transcripts_links:
        if link == '':
            transcripts_links.remove('')

    for link in video_links:
        file_name = link.split("/")[-1]
        request.urlretrieve(link, f"{output_dir_video}/{file_name}")

    for link in transcripts_links:
        drive_id = link.split("/")[-2]
        file_name = f'{output_dir_trans}/lec{str(transcripts_links.index(link) + 1)}.pdf'
        gdown.download(id=drive_id, output=file_name)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, help="URL of NPTEL Course")
    parser.add_argument('--output_dir_video', type=str, help="Output directory of videos")
    parser.add_argument('--output_dir_trans', type=str, help="Output directory of transcripts")
    args = parser.parse_args()
    parse_url_to_download(args)
