import csv
import requests
from bs4 import BeautifulSoup

i=1
movieschoose=['thisweek','intheaters','comingsoon']
class reptile_movie:
    def i_want_to_watch_movie():
        print("你想看什麼時期?")
        print("[1]本周新片")
        print("[2]上映中")
        class1 =int(input("[3]即將上映\n")) 

        for page in range(1,20):
            url = 'https://movies.yahoo.com.tw/movie_'+movieschoose[class1-1]+'.html?page='+str(page)
            response = requests.get(url=url)
            
            soup = BeautifulSoup(response.text, 'lxml')
            
            info_items = soup.find_all('div', 'release_info')

            with open('本週新片.csv', 'w', encoding='utf-8', newline='') as csv_file:
                
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['電影片名', '電影英文片名', '上映時間', '網友期待度'])
                for item in info_items:
            
                    name = item.find('div', 'release_movie_name').a.text.strip()
                    english_name = item.find('div', 'en').a.text.strip()
                    release_time = item.find('div', 'release_movie_time').text.split('：')[-1].strip()
                    level = item.find('div', 'leveltext').span.text.strip()
                    
                    csv_writer.writerow([name, english_name, release_time, level])
                    print('{}({}) 上映日：{} 期待度：{}'.format(name, english_name, release_time, level))
            with open('上映中.csv', 'w', encoding='utf-8', newline='') as csv_file:
                
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['電影片名', '電影英文片名', '上映時間', '網友期待度'])
            
                for item in info_items:
            
                    name = item.find('div', 'release_movie_name').a.text.strip()
                    english_name = item.find('div', 'en').a.text.strip()
                    release_time = item.find('div', 'release_movie_time').text.split('：')[-1].strip()
                    level = item.find('div', 'leveltext').span.text.strip()
                    
                    csv_writer.writerow([name, english_name, release_time, level])
                    print('{}({}) 上映日：{} 期待度：{}'.format(name, english_name, release_time, level))
            with open('即將上映.csv', 'w', encoding='utf-8', newline='') as csv_file:
                
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['電影片名', '電影英文片名', '上映時間', '網友期待度'])
            
                for item in info_items:
            
                    name = item.find('div', 'release_movie_name').a.text.strip()
                    english_name = item.find('div', 'en').a.text.strip()
                    release_time = item.find('div', 'release_movie_time').text.split('：')[-1].strip()
                    level = item.find('div', 'leveltext').span.text.strip()
                    
                    csv_writer.writerow([name, english_name, release_time, level])
                    print('{}({}) 上映日：{} 期待度：{}'.format(name, english_name, release_time, level))
if __name__ == "__main__":
    i_want_to_watch_movie()