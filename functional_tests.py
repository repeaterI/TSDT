import sys
sys.path.append("D:\App\Anaconda3\envs\SPI")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest 
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID,'id_list_table')
        rows = table.find_elements(By.TAG_NAME,'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 查看应用首页
        self.browser.get('http://localhost:8000')

        # 网页显示
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text #(1)
        self.assertIn('To-Do', header_text)

        # 文本输入框：待办事项
        inputbox = self.browser.find_element(By.ID, 'id_new_item') #(1)
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            "Enter a to-do item"
            )
        
        # 输入”Buy flowers“
        inputbox.send_keys('Buy flowers') #(2)

        # 回车更新，表格显示”1：Buy flowers“
        inputbox.send_keys(Keys.ENTER) #(3)
        time.sleep(1) #(4)
        self.check_for_row_in_list_table('1: Buy flowers')

        # 再显示文又文本输入框：待办事项
        # 输入“Give a gift to Lisi”
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Give a gift to Lisi') 
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #页面再次更新，清单中显示两个代办
        self.check_for_row_in_list_table('1: Buy flowers')
        self.check_for_row_in_list_table('2: Give a gift to Lisi')

        # 网站生成唯一的URL，记住清单

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()