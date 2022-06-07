# url = https://movie.naver.com/movie/sdb/browsing/bmovie_genre.naver
# https://movie.naver.com/movie/sdb/browsing/bmovie.naver?genre=1&page=1
# //*[@id="old_content"]/ul/li[1]/a
# //*[@id="old_content"]/ul/li[20]/a
# category = ['드라마', '판타지', '공포', '로맨스', '모험', '스릴러', '다큐멘터리', '코미디', '가족', '애니메이션', '범죄', '액션', '에로']
# page = 1000
# //*[@id="content"]/div[1]/div[4]/div[1]/div/div/p     # 줄거리 Xpath
# //*[@id="content"]/div[1]/div[4]/div[1]/div/div/p
from selenium import webdriver
import pandas as pd
import re
import time
import datetime

category = ['드라마', '판타지', '공포', '로맨스', '모험', '스릴러', '다큐멘터리', '코미디', '가족', '애니메이션', '범죄', '액션', '에로', '실험']
category_num = [1, 2, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 21]
pages = 300
category_cnt = 3
check_cnt = 3
check_cnt_2 = 3

url = 'https://movie.naver.com/movie/sdb/browsing/bmovie_genre.naver'

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
df_summaries = pd.DataFrame()
for i in category_num:
    category_cnt += 1
    summaries = []
    for j in range(1, pages + 1):
        url = f'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?genre={category_num[category_cnt - 1]}&page={j}'
        driver.get(url)
        time.sleep(0.2)
        for k in range(1, 21):
            xpath = f'//*[@id="old_content"]/ul/li[{k}]/a'
            url = f'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?genre={category_num[category_cnt - 1]}&page={j}'
            driver.get(url)
            try:
                driver.find_element_by_xpath(xpath).click() # 제목 클릭해서 들어가기
                try:
                    summary = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div/p').text
                    summary = re.compile('[^가-힣 ]').sub('', summary)
                    summaries.append(summary)
                except:
                    pass
            except:
                pass
        if j % 30 == 0:
            df_section_summaries = pd.DataFrame(summaries, columns=['summary'])
            df_section_summaries['category'] = category[category_cnt-1]
            df_summaries = pd.concat([df_summaries, df_section_summaries], ignore_index=True)
            df_section_summaries.to_csv('./crawling_data/crawling_data_{}_{}_{}.csv'.format(category[category_cnt-1], j-29, j), index=False)
            summaries = []
            print(check_cnt)
    df_section_summaries = pd.DataFrame(summaries, columns=['summary'])
    df_section_summaries['category'] = category[category_cnt-1]
    df_summaries = pd.concat([df_summaries, df_section_summaries], ignore_index=True)
    df_section_summaries.to_csv('./crawling_data/crawling_data_{}_last.csv'.format(category[category_cnt-1]), index=False)
    summaries = []
    print(check_cnt_2)
df_section_summaries = pd.DataFrame(summaries, columns=['summary'])
df_section_summaries['category'] = category[category_cnt-1]
df_summaries = pd.concat([df_summaries, df_section_summaries], ignore_index=True)
df_summaries.to_csv('./crawling_data/naver_movie_summary_{}.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)
driver.close()