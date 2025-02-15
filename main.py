import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from post_gen import create_content

EMAIL = ""
PASSWORD = ""

class LinkedinPostBot:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def post_at_linkedin(self):
        # Opens Linkedin
        self.driver.get("https://www.linkedin.com/login")
        time.sleep(2)  # Delay in seconds not recommended 0

        # Logs into your account
        username = self.driver.find_element(By.ID, value="username")
        username.send_keys(EMAIL, Keys.TAB, PASSWORD)
        login_button = self.driver.find_element(
            By.CSS_SELECTOR,
            value='#organic-div > form > div.login__form_action_container > button'
        )
        login_button.click()
        time.sleep(5)

        post = self.driver.find_element(
            By.CSS_SELECTOR,
            value='#ember32'
        )
        post.click()
        time.sleep(2)

        # Opens and writes the post
        post_box = self.driver.find_element(
            By.XPATH,
            value='/html/body/div[4]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]'
        )

        post_written_content = create_content()
        post_box.send_keys(post_written_content)

        time.sleep(2)

        post_it = self.driver.find_element(
            By.XPATH,
            value='/html/body/div[4]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/button'
        )
        post_it.click()


bot = LinkedinPostBot()
bot.post_at_linkedin()
