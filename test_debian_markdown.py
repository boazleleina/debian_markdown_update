import unittest
from bs4 import BeautifulSoup
from debian_markdown import get_parse_debian, convert_tag_to_markdown, markdown_file

class TestDebianMarkdown(unittest.TestCase):
    def test_get_parse_debian(self):
        # Test if the function returns a BeautifulSoup object
        soup = get_parse_debian()
        self.assertIsInstance(soup, BeautifulSoup)

    def test_convert_tag_to_markdown_paragraph(self):
        # Create a BeautifulSoup object for a <p> tag
        p_tag = BeautifulSoup('<p>This is a paragraph</p>', 'html.parser')

        # Convert the <p> tag to Markdown
        p_markdown = convert_tag_to_markdown(p_tag)

        # Check if the conversion is as expected
        self.assertEqual(p_markdown, 'This is a paragraph\n\n')

    def test_convert_tag_to_markdown_header(self):
        # Create a BeautifulSoup object for an <h2> tag
        h2_tag = BeautifulSoup('<h2>Header 2</h2>', 'html.parser')

        # Convert the <h2> tag to Markdown
        h2_markdown = convert_tag_to_markdown(h2_tag)

        # Check if the conversion is as expected
        self.assertEqual(h2_markdown, '## Header 2\n\n')

    def test_convert_tag_to_markdown_unordered_list(self):
        # Create a BeautifulSoup object for a <ul> tag
        ul_tag = BeautifulSoup('<ul><li>Item 1</li><li>Item 2</li></ul>', 'html.parser')

        # Convert the <ul> tag to Markdown
        ul_markdown = convert_tag_to_markdown(ul_tag)

        # Check if the conversion is as expected
        self.assertEqual(ul_markdown, '- Item 1\n- Item 2\n')

    def test_convert_tag_to_markdown_list_item(self):
        # Create a BeautifulSoup object for an <li> tag
        li_tag = BeautifulSoup('<li>Item</li>', 'html.parser')

        # Convert the <li> tag to Markdown
        li_markdown = convert_tag_to_markdown(li_tag)

        # Check if the conversion is as expected
        self.assertEqual(li_markdown, '- Item\n')

    def test_convert_tag_to_markdown_link(self):
        # Create a BeautifulSoup object for an <a> tag
        a_tag = BeautifulSoup('<a href="https://example.com">Link</a>', 'html.parser')

        # Convert the <a> tag to Markdown
        a_markdown = convert_tag_to_markdown(a_tag)

        # Check if the conversion is as expected
        self.assertEqual(a_markdown, '[Link](https://example.com)')
        
    def test_markdown_file(self):
        # Test the markdown_file function
        soup = BeautifulSoup('<p>Test content</p>', 'html.parser')
        markdown_file(soup)
        with open('debian_wiki.md', 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertIn('Test content', content)

if __name__ == '__main__':
    unittest.main()
