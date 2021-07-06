from random import random

from time import sleep
from selenium import webdriver 

class CupidBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login(self):
        self.driver.get('https://www.okcupid.com/')
        
        sleep(2)
        
        cookie_btn = self.driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')    
        cookie_btn.click()
        
        
        sign_in_btn = self.driver.find_element_by_xpath('//*[@id="main_content"]/div/div/div[1]/div[2]/a')
        sign_in_btn.click()
        
        
        sleep(2)
        
        facebook_btn = self.driver.find_element_by_xpath('//*[@id="OkModal"]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/button[3]')
        facebook_btn.click()
        
        #switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])
        
        sleep(2)
        
        
        email_btn = bot.driver.find_element_by_xpath('//*[@id="email"]')
        email_btn.click()
        
        #add email below in string    
        #email_btn.send_keys('')
        
        password_btn = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_btn.click()

        #add password below in string    
        password_btn.send_keys('')
        
        next_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        next_btn.click()
        
        #switch back to original window
        self.driver.switch_to.window(self.driver.window_handles[0])
        
    def like(self):
        like_bttn = self.driver.find_element_by_xpath('//*[@id="main_content"]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[2]')
        like_bttn.click()
            
    def dislike(self):
        dislike_bttn = self.driver.find_element_by_xpath('//*[@id="main_content"]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]')
        dislike_bttn.click()
        
    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="navigation"]/div/span[2]/div[1]/div[2]/button')
        popup_3.click()    
        
    def auto_swipe(self):
        while True:
            sleep(0.5)
            
            try:
                rand = random()
                if rand < .99:
                    self.like()
                   
               
                else:
                    self.dislike()
                     
                
            except Exception as d:
                try:
                    print(d)
                    sleep(1)
                    self.close_popup()
                
                except Exception as e:
                    print(e)
                    
                     



bot = CupidBot()
sleep(2)
bot.login()
sleep(2)
bot.auto_swipe()               
            
                
        
        
        
        
