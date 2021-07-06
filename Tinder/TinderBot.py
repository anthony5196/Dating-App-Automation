from random import random


from selenium import webdriver 
from time import sleep

 
from secrets import username, password
        
        
class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://tinder.com')  
        
        sleep(2)
        
        cookie_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        cookie_btn.click()
        
        sleep(3)
        
        #login_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/button[2]')
       # login_btn.click()
        
        email_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
        email_btn.click()
        
        sleep(4)
        
        
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])
        
        sleep(1)
        
        email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_input.send_keys(username)
        
        next_bttn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
        next_bttn.click()
        
        sleep(2)
        
        SecNext_bttn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]') 
        SecNext_bttn.click()
        
        
        password_input = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password_input.send_keys(password)
        
        
        password_next = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
        password_next.click()
        
        sleep(5)
        
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        sleep(3)
        
        Location_bttn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        Location_bttn.click()
        
        Notif_bttn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        Notif_bttn.click()
        
        sleep(7)
        
        
        
    
    def like(self):
        like_bttn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_bttn.click()
        
        
        
    def dislike(self):    
        dislike_bttn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
        dislike_bttn.click()
        
    
    def auto_swipe(self):
        while True:
           sleep(0.5)
           try:
               self.like()  
           except Exception as e:
               try:
                   print(e)
                   sleep(3)
                   self.close_popup()   
               except Exception as d:
                   print(d)
                   self.close_match()       
                    
           
          
        
    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()   
        
        
        
    def close_match(self):
        popup_4 = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        popup_4.click()
        
    def message_all(self):
        

        lines =['You up?']

     
        
        condition = 1
        
        while condition < 50:
            
            pickup_line = random.choice(lines)
            
            sleep(2)
        
            match_tab = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
            match_tab.click()
            
            sleep(1)
        
            first_match = self.driver.find_element_by_xpath('//*[@id="matchListNoMessages"]/div[1]/div[1]/a/div[1]')
            first_match.click()
        
            text_box = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            text_box.send_keys(pickup_line)
        
            send = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
            send.click()
            
            condition += 1
        
        
        
       
        
bot = TinderBot()
bot.login()
sleep (5)
bot.auto_swipe()

        



   
        
        
        
        
      
        
        
        
        
        
            
