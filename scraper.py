import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Texas'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

# searches for python only jobs
python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
for p_job in python_jobs:
    link = p_job.find("a")["href"]
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")

# all job results from Texas
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

# print(results.prettify())

# UK monster frontend does not use ids.... 
# URL = 'https://www.monster.co.uk/jobs/search?q=software+developer&where=London'
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, 'html.parser')

# results = soup.find_all('section', class='results-list split-screen-mode')
# print(results)
