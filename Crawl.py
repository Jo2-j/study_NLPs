from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime
import pandas as pd
import time
import os

class NaverBlogCrawler:
    def __init__(self):
        # Chrome 옵션 설정
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--window-size=1920x1080')
        self.options.add_argument('--disable-notifications')
        
        # WebDriver 초기화
        self.driver = webdriver.Chrome(options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
        
        # 결과를 저장할 리스트
        self.posts = []

    def crawl_page(self, url):
        try:
            self.driver.get(url)
            time.sleep(2)
            
            posts = self.wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '#PostThumbnailAlbumViewArea > ul > li')))
            
            for post in posts:
                try:
                    title = post.find_element(By.CSS_SELECTOR, 'a > div.area_text').text.strip()
                    date = post.find_element(By.CSS_SELECTOR, 'a > div.area_text > span.date').text.strip()
                    post_url = post.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                    
                    # 리스트에 추가
                    self.posts.append({
                        '제목': title,
                        '날짜': date,
                        'URL': post_url
                    })
                        
                except NoSuchElementException as e:
                    print(f"Element not found: {e}")
                    continue
                
            return True
            
        except TimeoutException:
            print("Page loading timeout")
            return False
        except Exception as e:
            print(f"Error during crawling: {e}")
            return False

    def crawl_all_pages(self, base_url):
        page = 1
        while True:
            url = f"{base_url}&currentPage={page}"
            print(f"Crawling page {page}: {url}")
            
            if not self.crawl_page(url):
                break
                
            try:
                next_page = self.driver.find_element(
                    By.CSS_SELECTOR, 
                    'div.wrap_blog2_paginate > div > a:last-child'
                )
                if 'next' not in next_page.get_attribute('class'):
                    break
                page += 1
                time.sleep(1)
            except NoSuchElementException:
                break

    def run(self, url):
        try:
            self.crawl_all_pages(url)
                
            # DataFrame으로 변환
            df = pd.DataFrame(self.posts)
            
            # 현재 시간을 파일명에 추가
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            excel_filename = f'naver_blog_posts_{timestamp}.xlsx'
            
            # Excel 파일 저장
            df.to_excel(excel_filename, index=False)
            
        finally:
            self.driver.quit()
            
        print(f"Total posts collected: {len(self.posts)}")
        print(f"Data saved to {excel_filename}")

if __name__ == "__main__":
    # 크롤링할 URL 지정
    target_url = "https://blog.naver.com/staffs00/223728553876"
    
    crawler = NaverBlogCrawler()
    crawler.run(target_url)
