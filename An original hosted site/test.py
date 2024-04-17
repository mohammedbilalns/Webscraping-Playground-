from bs4 import BeautifulSoup
import requests 



def skill_compare(list1, list2):
    result = False
    # traverse in the 1st list
    for x in list1:
        # traverse in the 2nd list
        for y in list2:
            # if one common
            if x == y:
                result = True
                return result    
    return result
     
print('Put some skill that you are not familiar with')
unfamiliar_skills =input('>').split()
print(unfamiliar_skills)
print(f'filtering out {unfamiliar_skills} ')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all( 'li',class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if not "few" in published_date:
        skills = job.find('span', class_ = 'srp-skills' ).text.split()          
        if not skill_compare(unfamiliar_skills,skills):
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
            link = job.header.h2.a['href']
            print(f'Company Name:{company_name}')
            print(f'Required Skills: {skills}')

            print(f'More Info: {link}')



            print('')