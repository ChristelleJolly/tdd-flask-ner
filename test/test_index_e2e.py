import unittest
from selenium import webdriver

class E2EIndexTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/chris/AppData/Local/Google/Chrome/chromedriver.exe')
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def _find_element(self, val):
        return self.driver.find_element_by_css_selector(f'[data-test-id="{val}"]')

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity', self.driver.title)

    def test_page_heading_is_as_expected(self):
        heading = self._find_element("heading").text
        self.assertEqual("Named Entity Finder", heading)

    def test_page_has_input_text_element(self):
        input_element = self._find_element("input-text")
        self.assertIsNotNone(input_element)

    def test_page_has_find_button_element(self):
        submit_button = self._find_element("find-button")
        self.assertIsNotNone(submit_button)

    def test_submitting_sentence_creates_table(self):
        input_element = self._find_element("input-text")
        submit_button = self._find_element("find-button")
        input_element.send_keys("France and GErmany share a border in Europe")
        submit_button.click()
        table_element = self._find_element("ner-table")
        self.assertIsNotNone(table_element)

    