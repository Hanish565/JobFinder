from bs4 import BeautifulSoup
import requests as re

print("SOME AVAILABLE JOBS ON LINKEDIN")
print('===============================================================')
url = 'https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0'
page = re.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
division = soup.find_all('div', class_='base-search-card__info')
for item in division:
    title = item.find('h3', class_='base-search-card__title')
    location = item.find('span', class_='job-search-card__location').text
    company = item.find('h4', class_='base-search-card__subtitle').text
    
    if title:
        print("Title:", title.text.strip())
        print("Location:", location.strip())
        print('Company:',company.strip())
        print('============================================')


