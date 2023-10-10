import unittest
from bs4 import BeautifulSoup
from debian_markdown import convert_tag_to_markdown

class TestConvertTagToMarkdown(unittest.TestCase):
    def test_paragraph_conversion(self):
        html = '<p>Test paragraph</p>'
        expected = 'Test paragraph\n\n'
        result = convert_tag_to_markdown(BeautifulSoup(html, 'html.parser').p)
        self.assertEqual(result, expected)

    def test_heading_conversion(self):
        html = '<h2>Test heading</h2>'
        expected = '## Test heading\n\n'
        result = convert_tag_to_markdown(BeautifulSoup(html, 'html.parser').h2)
        self.assertEqual(result, expected)

    def test_unordered_list_conversion(self):
        html = '<ul><li>Item 1</li><li>Item 2</li></ul>'
        expected = '- Item 1\n- Item 2\n'  # Corrected expected format
        result = convert_tag_to_markdown(BeautifulSoup(html, 'html.parser').ul)
        self.assertEqual(result, expected)

    def test_list_item_conversion(self):
        html = '<li>List item</li>'
        expected = '- List item\n'
        result = convert_tag_to_markdown(BeautifulSoup(html, 'html.parser').li)
        self.assertEqual(result, expected)

    def test_link_conversion(self):
        html = '<a href="https://example.com">Example Link</a>'
        expected = '[Example Link](https://example.com)'
        result = convert_tag_to_markdown(BeautifulSoup(html, 'html.parser').a)
        self.assertEqual(result, expected)

    def test_unknown_tag_conversion(self):
        # Test with an unsupported tag (should return an empty string)
        html = '<div>Unsupported Tag</div>'
        expected = ''
        result = convert_tag_to_markdown(BeautifulSoup(html, 'html.parser').div)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
