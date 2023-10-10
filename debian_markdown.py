"""
- To run this script, I installed dependencies including requests and beautifulsoup4 for web-scraping
    - pip install requests
    - pip install beautifulsoup4

- cd into the directory with the fiie, and run
    - python debian_markdown.py

- If the dependencies installed correctly and the file runs, a new .md file is created called 'debian_wiki,md'


"""
import requests
from bs4 import BeautifulSoup

# URL of the Debian Wiki News page
debian_wiki_url = "https://wiki.debian.org/News"

# Function to fetch and parse the Debian Wiki page
def get_parse_debian():
    try:
        # Send an HTTP GET request to the Debian Wiki page
        response = requests.get(debian_wiki_url)
        
        # Check the HTTP response status code for errors
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        return soup  # Return the entire parsed HTML

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Convert HTML to Markdown format
def convert_tag_to_markdown(element):
    # Check the HTML tag and convert to Markdown accordingly
    if element.name == 'p':
        return element.get_text() + '\n\n'
    elif element.name == 'h2':
        return f"## {element.get_text()}\n\n"
    elif element.name == 'ul':
        return f"{element.get_text()}\n"
    elif element.name == 'li':
        return f"- {element.get_text()}\n"
    elif element.name == 'a':
        # Handle links by converting them to Markdown format
        link_text = element.get_text()
        link_url = element.get('href')
        return f"[{link_text}]({link_url})"
    else:
        return ''

# After getting the parsed content, convert it to Markdown and write it to the file
def markdown_file(soup):
    if soup:
        with open('debian_wiki.md', 'w', encoding='utf-8') as file:
            for element in soup.find_all():
                #Call the convert_tag_to_markdown here to read all the tags and convert them
                markdown_content = convert_tag_to_markdown(element)
                if markdown_content:
                    file.write(markdown_content)
        print("Debian Wiki News page has been written to debian_wiki.md")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Fetch and parse the content from the Debian Wiki page
    debian_news_content = get_parse_debian()
    
    # If content was successfully retrieved and parsed
    ## Call the markdown_file function to save the content to a Markdown file
    if debian_news_content:
        markdown_file(debian_news_content)
