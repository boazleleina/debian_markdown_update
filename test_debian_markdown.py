import unittest
from bs4 import BeautifulSoup
from debian_markdown import get_parse_debian, convert_tag_to_markdown, markdown_file
from unittest.mock import patch, Mock


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


class TestDebianMarkdownFunctions(unittest.TestCase):
    @patch('debian_markdown.requests.get')
    def test_get_parse_debian(self, mock_get):
        # Case 1: Simulate a successful response (status code 200)
        mock_response_200 = Mock()
        mock_response_200.status_code = 200
        mock_response_200.text = '<p>Test paragraph</p>'
        mock_get.return_value = mock_response_200

        # Test the function for a successful response (status code 200)
        result_200 = get_parse_debian()
        # Ensure that BeautifulSoup is called with the correct HTML
        mock_response_200.raise_for_status.assert_called()
        self.assertIsInstance(result_200, BeautifulSoup)

        # Case 2: Simulate a non-successful response (status code other than 200)
        mock_response_not_200 = Mock()
        # Simulate a non-200 status code (you can change it to any other status code)
        mock_response_not_200.status_code = 404  
        mock_get.return_value = mock_response_not_200
        # Test the function for a non-successful response (status code other than 200)
        with self.assertRaises(Exception) as context:
            get_parse_debian()

        self.assertEqual(str(context.exception), "Failed to fetch the Debian Wiki News page: 404")


    def test_markdown_file(self):
        # Mock the BeautifulSoup object with sample content
        html = '<p>Test paragraph</p><h2>Test heading</h2>'
        soup = BeautifulSoup(html, 'html.parser')

        # Call the function and capture the written content
        markdown_file(soup)

        # Check if the content was written to the file correctly
        with open('debian_wiki.md', 'r', encoding='utf-8') as file:
            written_content = file.read()
            expected_content = "Test paragraph\n\n## Test heading\n\n"
            self.assertEqual(written_content, expected_content)

if __name__ == '__main__':
    unittest.main()
