import sys
sys.path.append("D:\App\Anaconda3\envs\SPI")

from selenium import webdriver
import unittest 

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        ## 查看应用首页
        self.browser.get('http://localhost:8000')

        # 网页显示
        self.assertIn('To-Do',self.browser.title), "Brower title was" + self.browser.title
        self.fail('Finish the test')


        # 文本输入框，输入后更新为页面显示
        # 生成url，记住输入内容


if __name__ == '__main__':
    unittest.main()