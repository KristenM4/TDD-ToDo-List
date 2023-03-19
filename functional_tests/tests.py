from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import unittest
from django.test import LiveServerTestCase

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, "id_list_table")
                rows = table.find_elements(By.TAG_NAME, "tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Someone heard about our website, a to-do list maker, and wants to check it out
        self.browser.get(self.live_server_url)

        # They see that to-do lists are mentioned in the page title and header
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("To-Do", header_text)

        # The option to add a to-do list item is visible on the homepage
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item"
        )

        # The user adds "Get car oil changed" into the form
        inputbox.send_keys("Get car oil changed")

        # After hitting enter, the page updates and says
        # "1: Get car oil changed" as a list item
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Get car oil changed")

        # The option to add another item to the to-do list is there
        # User adds "Wash car" as the second item on the list
        #inputbox.send_keys("Wash car")
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Wash car")
        inputbox.send_keys(Keys.ENTER)

        # The page is updated and now shows 2 items in the to-do list
        self.wait_for_row_in_list_table("1: Get car oil changed")
        self.wait_for_row_in_list_table("2: Wash car")

        # The site has a unique URL for this user and contains an explanation
        # to save the URL and revisit it to view the list again
        self.fail("Finish the test!")

        # The user visits the unique URL and sees their list

        # The user then closes their browser