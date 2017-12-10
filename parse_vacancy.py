import requests
from bs4 import BeautifulSoup
import time


headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
    }


def parseint(s):
    s1 = u""
    for i in s:
        if i.isdigit():
            s1 += i
    return s1


def start_parse(start):
    count = 0
    while start >= 0:
        try:
            url = 'https://www.superjob.ru/resume/'+str(start)
            req = requests.get(url, headers=headers)
            soup = BeautifulSoup(req.text, 'html.parser')
            salary = soup.find('span', {'class': 'h_font_weight_medium'})
            proff = soup.find('h1', {'class': 'sj_h1 sj_block m_b_2 h_font_weight_light h_word_wrap_break_word'})

            if (salary is None):
                print('salary is none!')
                time.sleep(0.2)
                start -= 1
                continue
            else:
                salary = str(parseint(salary.text))

            if (proff is None):
                print('proff is none!')
                time.sleep(0.2)
                start -= 1
                continue
            else:
                proff = proff.text

            if (salary == ''):
                print('salary is none!')
                time.sleep(0.1)
                start -= 1
                continue

            img_url = soup.find('img', {'class': 'ResumeMainHRNew_photo'})
            if (img_url is None):
                print('img is none!')
                time.sleep(0.1)
                start -= 1
                continue

            img_data = requests.get(img_url['src']).content
            with open('resume_img/'+str(start)+'.jpg', 'wb') as f:
                f.write(img_data)
            with open('resume_id.txt', 'a') as f:
                f.write(str(start)+'\n')
            with open('resume_salaryes.txt', 'a') as f:
                f.write(salary+','+proff+'\n')

            count += 1
            print(count)

        except Exception as e:
            print(e)
        if start % 100 == 0:
            time.sleep(3.2)
        time.sleep(0.2)
        start -= 1


start_parse(40866378)