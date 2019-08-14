#!/usr/local/bin/python3
from selenium import webdriver
from utility_methods.utility_methods import * # imports the dtu_method decorator
from selenium.webdriver.chrome.options import Options
import urllib.request
import time
import os
import pygame
import optparse
import torch
import torchvision
from utility_methods.charDiv import Div #importing from local directory
from PIL import Image
import base64
import cv2
from ocr.CNN import Net #imports the neural net


class bot:
	
	def __init__(self,user,password,url):
		'''
		initialized the username, password, driver and url

		Args:
			user: str: username of the account
			password:str: enter the password
			url: str: the url of the login site
		'''
		self.user=user
		self.password=password
		self.chrome_options=webdriver.ChromeOptions()
		self.chrome_options.add_argument("--disable-infobars")
		self.driver=webdriver.Chrome(executable_path="./chromedriver",options=self.chrome_options)
		#self.driver=webdriver.Chrome("./chromedriver")
		self.url=url                                            #! "https://cumsdtu.in"
		# self.page=page
		# self.music("break_free.mp3") # COMMENT THIS OR change the music name here if neede
		#self.login()
	
	@dtu_method	
	def login(self):

		'''
		method to enter the details and click the login button
		'''
		self.driver.get(f'{self.url}')
		self.driver.find_element_by_name("userName").send_keys(self.user)
		self.driver.find_element_by_name("password").send_keys(self.password)
		self.getCaptcha()
		self.captcha_val = self.breakCaptcha()
		print(f'Captcha Value ---------------- {self.captcha_val}')
		self.driver.find_element_by_name("captcha").send_keys(self.captcha_val)
		button=self.driver.find_element_by_id("submitButton")
		button.click()
	
	#@dtu_method
	def music(self,path):
		'''
		Plays the music once the page is loaded
		args:
			path:str:the path to the mp3 file
		'''
		pygame.init()
		pygame.mixer.music.load(path)
		pygame.mixer.music.play()
		time.sleep(1)

	def getCaptcha(self):
		captcha_element = self.driver.find_element_by_xpath('//*[@id="captchaImg"]')
		img_captcha_base64 = self.driver.execute_async_script("""
    	var ele = arguments[0], callback = arguments[1];
    	ele.addEventListener('load', function fn(){
     	 ele.removeEventListener('load', fn, false);
     	 var cnv = document.createElement('canvas');
     	 cnv.width = this.width; cnv.height = this.height+2;
      	cnv.getContext('2d').drawImage(this, 0, 0);
      	callback(cnv.toDataURL('image/jpeg').substring(22));
   				 }, false);
   			 ele.dispatchEvent(new Event('load'));
    	""", captcha_element)

		# save the captcha to a file
		with open(r"captcha.jpg", 'wb') as f:
			f.write(base64.b64decode(img_captcha_base64))
		return 

	
	
	def breakCaptcha(self):
		classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',\
         'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',\
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',\
                   'X', 'Y', 'Z']
		image_file = "./captcha.jpg"

		img = cv2.imread(image_file)

		tens = torch.zeros(6,1,24,14)
		tens = Div(img)
		net = Net()
		# print(f'the div shape is {tens.size}\n\n {tens}')
		net.load_state_dict(torch.load("ocr/mod.pt"))

		with torch.no_grad():
			result = net(tens)
			_,pred = torch.max(result,1)
		predArray= []
		for i in range(6):
			predArray.append(classes[pred[i]])

		return("".join(predArray))



if __name__ == "__main__":
	parser=optparse.OptionParser(usage="usage: %prog -u <username> -p <password>",version="%prog 2.0")
	parser.add_option('-u',dest="username",type='string',help='Enter the username')
	parser.add_option('-p',dest="password",type='string',help='Enter the password')
	(options,args)=parser.parse_args()
	if(options.username==None)|(options.password==None):
		print(parser.usage)
		exit(0)

	username=options.username
	password=options.password


	url="https://cumsdtu.in/registration_student/login/login.jsp" #! Change the URL if required
    #url="https://webcache.googleusercontent.com/search?q=cache:Yfcv\
	# sRm_o5gJ:https://cumsdtu.in/registration_student/+&cd=1&hl=en&ct=clnk&gl=in"
	counter=0
	while True:
		try:
			a=urllib.request.urlopen(url).getcode()
			if(int(a)==200):
				print("\n\n YAY WE ARE IN \n\n")
				dtu_bot=bot(username,password,url)
				dtu_bot.login()
				while dtu_bot.driver.current_url == url:
					dtu_bot.login()
				break
			else:
				counter+=1
				time.sleep(3)
		except ConnectionRefusedError :
			print("connection refused count %d",counter)
			counter+=1
		except urllib.error.HTTPError as e :
			print(f"{e} count: {counter}")
			counter+=1
	
	





