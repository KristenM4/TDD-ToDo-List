from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Someone heard about our website, a to-do list maker, and wants to check it out
        self.browser.get('http://localhost:8000')

        #They see that to-do lists are mentioned in the page title and header
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        #The option to add a to-do list item is visible on the homepage

        #The user adds "Get car oil changed" into the form

        #After hitting enter, the page updates and says
        #"1: Get car oil changed" as a list item

        #The option to add another item to the to-do list is there
        #User adds "Wash car" as the second item on the list

        #The page is updated and now shows 2 items in the to-do list

        #The site has a unique URL for this user and contains an explanation
        #to save the URL and revisit it to view the list again

        #The user visits the unique URL and sees their list

        #The user then closes their browser

if __name__ == "__main__":
    unittest.main()
