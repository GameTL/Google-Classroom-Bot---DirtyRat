# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'


# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import re
from bs4 import BeautifulSoup

browser  = webdriver.Firefox() # this open a browser

class ClassRoom:
    def __init__(self, SimpleClassName, SimpleTeacherName, GCClass, GCTeacher, Link):
        self.SimpleClassName = SimpleClassName
        self.SimpleTeacherName = SimpleTeacherName
        self.GCClass = GCClass
        self.GCTeacher = GCTeacher
        self.Link = Link

# %%

list_of_classroom = []

Computer_Science = ClassRoom("Computer Science", "Mr.Kieran", "(Y13) CS", "Kieran OBrien", "https://classroom.google.com/u/0/c/NDEwNjM3NjM5NTha")

list_of_classroom.append(Computer_Science)
print(list_of_classroom[0].SimpleClassName)


# %%
# The goal is to reach the homepage of the Homeroom
def sign_in_function():
    EMAIL = "" ### ENTER USERNAME ###
    PASSWORD = "" ### ENTER PASSWORD ###
    global browser
    browser.get("""https://accounts.google.com/signin/v2/identifier
    ?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=
    GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin""") # Google Sign In Page
    browser.implicitly_wait(2)
    email_fill = browser.find_element_by_xpath("//input[contains(@type,'email')]").send_keys(EMAIL)
    email_click_next = browser.find_element_by_xpath("//div[contains(@class,'VfPpkd-RLmnJb')]").click()
    time.sleep(2)
    password_fill = browser.find_element_by_xpath("//input[contains(@class,'whsOnd zHQkBf')]").send_keys(PASSWORD)
    password_click_next = browser.find_element_by_xpath("//div[contains(@class,'VfPpkd-RLmnJb')]").click()
    browser.get(Computer_Science.Link) ###  CHANGE VARIABLE HERE  ###

sign_in_function()

# %%
def check_for_valid_post_time():
    global post_valid_time
    time_list = ["3 May", "08:", "07:"]  ###  CHANGE VARIABLE HERE  ###
    OPERATOR = "x*"
    global post_valid_time
    post_valid_time = False
    time.sleep(4)
    whole_page = browser.page_source
    top_post = browser.find_element_by_xpath("""//div[contains(@class,'qhnNic LBlAUc Aopndd TIunU')]""").text
    print(top_post)
    for time_string in time_list:
        re_string = time_list[0] + OPERATOR # joining the search string with the operator
        print(re_string)
        valid_time = re.findall(re_string, top_post)
        print(valid_time)
        if valid_time:
            print("Yes, there is at least one match!")
            post_valid_time = True
        else:
            print("No match")
            # PANIC!

check_for_valid_post_time()

# %%
def fill_comment():
    if post_valid_time:
        time.sleep(5)
        FILL_LIST = ["Good Morning! Game here(Bot)", "Here(Bot)", "First test run with checking the time Afternoon (BOT)"]
        comment_fill = browser.find_element_by_xpath("//div[contains(@class,'LsqTRb Lzdwhd-AyKMt tgNIJf-Wvd9Cc Yiql6e iTy5c editable')]").send_keys(FILL_LIST[2])
        time.sleep(4)
        click_reply_button = browser.find_element_by_xpath("//*[name()='path' and @d='M2 3v18l20-9L2 3zm2 11l9-2-9-2V6.09L17.13 12 4 17.91V14z']").click()
        # for xpath for svg format is different for somereason

fill_comment()



# %% Quit 
time.sleep(5)
browser.quit()

