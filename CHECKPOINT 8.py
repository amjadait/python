#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup

# 1.1 Get and parse HTML content from a Wikipedia page
def get_parsed_content(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup

# 1.2 Extract article title
def extract_article_title(soup):
    title = soup.find('h1', {'class': 'firstHeading'}).text
    return title

# 1.3 Extract article text with headings and map them to paragraphs in a dictionary
def extract_article_text(soup):
    article_text = {}
    headings = soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6'])
    
    for heading in headings:
        heading_text = heading.get_text()
        paragraphs = []
        current = heading.find_next_sibling()
        
        while current and current.name not in ['h2', 'h3', 'h4', 'h5', 'h6']:
            if current.name == 'p':
                paragraphs.append(current.get_text())
            current = current.find_next_sibling()
        
        if paragraphs:
            article_text[heading_text] = paragraphs
    
    return article_text

# 1.4 Collect links that redirect to another Wikipedia page
def collect_internal_links(soup):
    internal_links = []
    for link in soup.find_all('a', href=True):
        if link['href'].startswith('/wiki/') and ':' not in link['href']:
            internal_links.append(link['href'])
    return internal_links

# 1.5 Wrap all functions into a single function
def scrape_wikipedia_page(url):
    soup = get_parsed_content(url)
    title = extract_article_title(soup)
    article_text = extract_article_text(soup)
    internal_links = collect_internal_links(soup)
    
    scraped_data = {
        'title': title,
        'article_text': article_text,
        'internal_links': internal_links
    }
    
    return scraped_data

# 1.6 Test the function on a Wikipedia page
wikipedia_link = "https://en.wikipedia.org/wiki/Python_(programming_language)"
scraped_data = scrape_wikipedia_page(wikipedia_link)

print("Title:", scraped_data['title'])
print("\nArticle Text:")
for heading, paragraphs in scraped_data['article_text'].items():
    print(heading)
    for paragraph in paragraphs:
        print("- ", paragraph)
print("\nInternal Links:", scraped_data['internal_links'])

