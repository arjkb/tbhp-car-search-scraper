from bs4 import BeautifulSoup
import requests

def main():
    r = requests.get('https://www.team-bhp.com/forum/official-new-car-reviews/')
    
    # TODO: ensure status code is 200

    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup.prettify())

    for link in soup.find_all('a'):
        link_id = link.get('id')
        if(str(link_id).startswith('thread')):
            print(link_id, link.text, link.get('href'))
            print()

if __name__ == "__main__":
    main()