
"""
This script is responsible for scraping the content of a Wikipedia page
related to Luke Skywalker and saving it to a text file.
Both the BeautifulSoup and wikipediaapi libraries code is provided.
WikipediaAPI makes more efficeint use of the Wikipedia content
"""

# import requests
# from bs4 import BeautifulSoup

# def scrape_wikipedia(url, file_path):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     content = ""
#     for paragraph in soup.find_all('p'):
#         content += paragraph.text

#     with open(file_path, "w", encoding="utf-8") as file:
#         file.write(content)

#     return file_path

# if __name__ == "__main__":
#     url = "https://en.wikipedia.org/wiki/Luke_Skywalker"
#     file_path = "luke_skywalker_wikipedia_content.txt"
#     scrape_wikipedia(url, file_path)
#     print(f"Content saved to {file_path}")

import wikipediaapi

def scrape_wikipedia(url, file_path):
    wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')
    page = wiki_wiki.page("Luke_Skywalker")

    if not page.exists():
        print("The page does not exist.")
        return

    # Extracting the full text of the page
    full_text = page.text

    # Extracting sections and references
    def extract_sections(section, level=0):
        content = ""
        if level <= 1:  # Adjust the level if you want deeper levels of sections
            content += section.title + "\n" + section.text + "\n"
        for s in section.sections:
            content += extract_sections(s, level + 1)
        return content

    sections_content = extract_sections(page)

    # Note: wikipediaapi does not provide direct access to references separately,
    # so they will be included in the sections text.

    # Splitting paragraphs
    paragraphs = page.text.split('\n\n')
    paragraphs_content = "\n".join(paragraphs)

    content = f"Title: {page.title}\n\nParagraphs:\n{paragraphs_content}\n\nSections:\n{sections_content}"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    return file_path

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Luke_Skywalker"
    file_path = "luke_skywalker_wikipedia_content.txt"
    scrape_wikipedia(url, file_path)
    print(f"Content saved to {file_path}")
