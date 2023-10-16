from bs4 import BeautifulSoup
import requests as re
print("SOME AVAILABLE JOBS ON LINKEDIN")
url = 'https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0'
page = re.get(url)
soup = BeautifulSoup(page.text, 'lxml')

jobs = soup.find_all('a', class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')


for job in jobs:
    titles = job.find_all('span', class_='sr-only')
    
    for info in titles:
        print(info.text.strip())
        print('============================================')
        
