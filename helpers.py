import requests
from datetime import datetime, timedelta
import json, re, config


match_patterns = ['let', 'const', 'int', 'class', 'print', 'var']

username = config.USERNAME
password = config.PASSWORD
def github(number_of_pates_gists, regex):
    pates = number_of_pates_gists
    links = []
    contents = []
    response = []
    now = datetime.now()
    timeline = now - timedelta(days=300)
    format_timeline_iso = timeline.isoformat()
    c=0
    num_of_pages = int(number_of_pates_gists/100)+1
    for num_page in range(1, num_of_pages):
        get_github = requests.get('https://api.github.com/gists/public?page={}&per_page=100'.format(num_page),
                                  {'since': format_timeline_iso}, auth=(username, password))
        # print(get_github.content)

        # print(get_github.status_code)
        if get_github.status_code == 200:
            get_github = json.loads(get_github.text)
            # print('gi')

            for num in range(pates+1):
                # print((get_github[0]))

                # print('hee')


                print('number:', num)
                github_links = get_github[num]['url']
                # print(github_links)


                links.append(github_links)
                print(len(links))
                if num ==99:
                    break

                    # print('Number of gists should not be more than {0}'.format(len(get_github)))

            for link in links:

                github_content_req = requests.get(link)
                # print('content:', github_content_req)
                # exit()
                my_dict = dict(json.loads(github_content_req.text))
                # print(my_dict)


                try:
                    dict_key_list = [*my_dict["files"]]
                except:
                    continue
                content = my_dict["files"][dict_key_list[0]]["content"]
                content = content.rstrip('\n')
                # content = content.rstrip(r"\"")
                content_tuple = (link, content)
                contents.append(content_tuple)

            for content in contents:
                for pattern in regex:
                    # print(pattern, content)
                    if re.search(pattern, content[1]):
                        available = {'url':content[0], 'matches': pattern}
                        response.append(available)

    return response


print(*github(150, match_patterns), sep='\n')
