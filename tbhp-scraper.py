from bs4 import BeautifulSoup
import requests

def search(carname, reviews):
    for k in reviews:
        if carname in k.lower():
            print(k, reviews[k])

def get_soup(link):
    r = requests.get(link)
    if r.status_code != requests.codes.ok:
        return None
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup

def main():
    soup = get_soup('https://www.team-bhp.com/forum/official-new-car-reviews/')
    if soup == None:
        print("Error fetching page")
        exit(0)

    navigation_pages = set()
    navigation_pages.add('https://www.team-bhp.com/forum/official-new-car-reviews/')
    review = dict()

    # get list of all links to be navigated to
    # go to each of those links, and get links to vehicle reviews

    for link in soup.find_all('a'):
        link_title = link.get('title')
        if(str(link_title).startswith("Show results")):
            # print(link_title, link.get('href'))
            navigation_pages.add(link.get('href'))

    counter = 0
    # now go to each page, and get the vehicle review list
    for page in navigation_pages:
        soup = get_soup(page)
        if soup != None:
            for link in soup.find_all('a'):
                link_id = link.get('id')
                if str(link_id).startswith('thread'):
                    counter += 1
                    print(counter, link.text, link.get('href'))
                    review[link.text] = link.get('href')

    
    search("mercedes", review)

if __name__ == "__main__":
    main()