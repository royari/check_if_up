#!/usr/local/bin/python3
#import functools
from selenium import webdriver
from utility_methods.utility_methods import * # imports the dtu_method decorator
from selenium.webdriver.chrome.options import Options
import urllib.request
import time
import os
import pygame
import optparse
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
		self.chrome_options=Options()
		self.chrome_options.add_argument("--disable-infobars")
		self.driver=webdriver.Chrome(executable_path="./chromedriver",options=self.chrome_options)
		#self.driver=webdriver.Chrome("./chromedriver")
		self.url=url                                            #! "https://cumsdtu.in"
		# self.page=page
		self.music("break_free.mp3") # COMMENT THIS OR change the music name here if needed
		self.login()
	
	@dtu_method	
	def login(self):

		'''
		method to enter the details and click the login button
		'''
		self.driver.get(f'{self.url}')
		self.driver.find_element_by_name("userName").send_keys(self.user)
		self.driver.find_element_by_name("password").send_keys(self.password)
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
    #url="https://webcache.googleusercontent.com/search?q=cache:YfcvsRm_o5gJ:https://cumsdtu.in/registration_student/+&cd=1&hl=en&ct=clnk&gl=in"

	# source=urllib.request.urlopen(url).read()
	# new_source=source
	counter=0
	while True:
		try:
			a=urllib.request.urlopen(url).getcode()
			if(int(a)==200):
				print("\n\n YAY WE ARE IN \n\n")
				dtu_bot=bot(username,password,url)
				# time.sleep(10)
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
	
	





