import requests
from bs4 import BeautifulSoup

# URL of the Debian Wiki News page
debian_wiki_url = "https://wiki.debian.org/News"


def get_parse_debian():
    """
    Fetch and parse the Debian Wiki page.
    """
    try:
        # Send an HTTP GET request to the Debian Wiki page
        response = requests.get(debian_wiki_url, allow_redirects=True)

        if response is not None and response.status_code == 200:
            # Check the HTTP response status code for errors
            response.raise_for_status()

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            return soup  # Return the entire parsed HTML
        else:
            raise Exception(
                f"Failed to fetch the Debian Wiki News page: {response.status_code}"
            )
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None  # Return None if there was an error


def convert_tag_to_markdown(element):
    """
    Convert HTML elements to Markdown format.
    """
    # Check the HTML tag and convert to Markdown accordingly
    if element.name == "p":
        return element.get_text().strip() + "\n\n"
    elif element.name == "h2":
        return f"## {element.get_text().strip()}\n\n"
    elif element.name == "ul":
        list_items = [f"- {li.get_text().strip()}" for li in element.find_all("li")]
        return "\n".join(list_items) + "\n"
    elif element.name == "li":
        return f"- {element.get_text().strip()}\n"
    elif element.name == "a":
        # Handle links by converting them to Markdown format
        link_text = element.get_text().strip()
        link_url = element.get("href")
        if link_url.startswith("/"):
            # Check if the link has a relative path
            link_url = f"https://wiki.debian.org{link_url}"
        return f"[{link_text}]({link_url})"
    else:
        return ""


def markdown_file(soup):
    """
    Convert parsed HTML to Markdown and write to a file.
    """
    if soup:
        with open("debian_wiki.md", "w", encoding="utf-8") as file:
            for element in soup.find_all():
                # Call the convert_tag_to_markdown here to read all the tags and convert them
                markdown_content = convert_tag_to_markdown(element)
                if markdown_content:
                    file.write(markdown_content)
        print("Debian Wiki News page has been written to debian_wiki.md")


if __name__ == "__main__":
    # Fetch and parse the content from the Debian Wiki page
    debian_news_content = get_parse_debian()

    # If content was successfully retrieved and parsed
    # Call the markdown_file function to save the content to a Markdown file
    if debian_news_content:
        markdown_file(debian_news_content)
