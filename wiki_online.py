from bs4 import BeautifulSoup
import requests

must_have_word = 'assemble'
filtering_words = ['muscle', 'sex', 'quiz', 'team']



def extract_links(key_word, filtering):
    wiki_assemble = requests.get(f'https://www.wikihow.com/wikiHowTo?search={key_word}&Search=')
    if wiki_assemble.status_code != 200:
        exit(1)
    wiki_assemble_text = wiki_assemble.text
    #print(wiki_assemble_text)
    assemble_html = BeautifulSoup(wiki_assemble_text, 'lxml')

    results = assemble_html.find_all('a', class_ = 'result_link')
    with open(f'output/{key_word}.txt', 'w') as f:
        for index, result in enumerate(results):
            result_title = result.find('div', class_ = 'result_title').text
            result_link = result['href']
            if not any(word.lower() in result_title.lower() for word in filtering) and key_word.lower() in result_title.lower():
                f.write(f"index: {index}\n")
                f.write(f"Title: {result_title.strip()}\n")
                f.write(f"Link: {result_link.strip()}\n\n")
        print(f'file saved')

extract_links(must_have_word, filtering_words)