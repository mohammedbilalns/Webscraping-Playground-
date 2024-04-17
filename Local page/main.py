from bs4 import BeautifulSoup

with open('sample.html', 'r') as html_file: #opens and reads html file
    content = html_file.read() #reads html file
    soup = BeautifulSoup(content, 'lxml') # grabs the contents
    cousre_cards = soup.find_all('div', class_='card' ) # finds all classes named card inside all div
    for course in cousre_cards:
        course_name = course.h5.text
        course_price =course.a.text.split()[-1] #finds and split and grabs only the last word of a tag

        print(f'{course_name} costs {course_price}')
