from bs4 import BeautifulSoup
import requests as re

print("SOME AVAILABLE JOBS")
print('===============================================================')
url = 'https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0'
page = re.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
link_parts = soup.find_all('a', class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')
division = soup.find_all('div', class_='base-search-card__info')
for i in range(len(division)):
    title = division[i].find('h3', class_='base-search-card__title')
    location = division[i].find('span', class_='job-search-card__location').text
    company = division[i].find('h4', class_='base-search-card__subtitle').text

    if title:
        print("Title:", title.text.strip())
        print("Location:", location.strip())
        print('Company:', company.strip())
        print('Link:', link_parts[i]['href'])
        print('============================================')

url = "https://www.learn4good.com/jobs/index.php?controller=job_list&action=display_search_results&page_number=1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = re.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    job_listings = soup.find_all('td', class_='job_cell')

    for listing in job_listings:
        job_title = listing.find('a', class_='job_title').text.strip()

        additional_info_div = listing.find('div', class_='additional_job_info')
        company_name_element = listing.find('div', class_='additional_job_info').find('a')
        location = listing.find('h3', class_='loc_title').text.strip()

        company_name = company_name_element.text.strip() if company_name_element else "Company name not found"
        link = listing.find('a', class_='view_job_button')['href']
        print("Title:", job_title.strip())
        print("Location:", location.strip())
        print("Company:",company_name.strip())
        print('Link:',link)
        print("==============================================")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
    print("Failed to retrieve the webpage. Status code:", response.status_code)