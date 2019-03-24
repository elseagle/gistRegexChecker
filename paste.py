import re
import requests
from bs4 import BeautifulSoup

match_patterns = ['let', 'pass*', '*?@domain.com', '*-mydomain.com',  'class', 'print', 'var', 'if', 'int']


def pastebin(matches):
    response = requests.get('https://pastebin.com/archive')
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    paste_list = soup.find('table', class_='maintable')
    links = []
    titles = []
    response_returned = []
    print(paste_list)
    try:
        pasted = paste_list.find_all('a')
    except:
        response_returned

    for link in pasted:
        #print(link)
        title = link.get_text()
        titles.append(title)
        link = link.get('href')
        links.append(link)
    #print(links)


    for link, title in zip(links, titles):
        url = 'https://pastebin.com{}'.format(link)
        print(link)
        # break
        # url = 'https://pastebin.com/NKL1eN7i'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            content = soup.find('textarea', class_='paste_code')
            content = content.get_text()
        except:
            continue

        #print(type(content))
        for match in match_patterns:
            print()
            # content = content.rstrip(re.match('\*', ''))
            # listcon = list(content)
            # content = ''.join(listcon)
            # print(content)
            print(match)
            try:
                if re.search(match, content, re.MULTILINE):

                    available = {'url': url, 'matches': match}
                    response_returned.append(available)
                else:
                    continue
            except:
                continue

            try:
                if re.search(match, title, re.MULTILINE):

                    available = {'url': title, 'matches': match}
                    response_returned.append(available)
                else:
                    continue
            except:
                continue

            # except:
            #    continue

            print(response_returned)
        return response

pastebin(match_patterns)
# print(*response_returned, sep='\n')