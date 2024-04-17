from bs4 import BeautifulSoup
import requests 
import time



def skill_compare(list1, list2):
    result = False

    for x in list1:

         for y in list2:

            if x == y:
                result = True
                return result    
    return result
     
print('Put some skill that you are not familiar with')
unfamiliar_skills =input('>').split()
print(f'filtering out {unfamiliar_skills} ')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all( 'li',class_='clearfix job-bx wht-shd-bx')

    for index ,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if not "few" in published_date:
            skills = job.find('span', class_ = 'srp-skills' ).text
            skilllist = skills.split()        
            if not skill_compare(unfamiliar_skills,skilllist):
                company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
                link = job.header.h2.a['href']
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name:{company_name} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'More Info: {link}')
                print(f'file saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f' Waiting {time_wait} minutes...')
        time.sleep(time_wait *60)