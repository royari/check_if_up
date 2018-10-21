#!/usr/local/bin/python3
import urllib.request
import time
import os
import pygame
url="http://reg.exam.dtu.ac.in"
source=urllib.request.urlopen(url).read()
new_source=source
counter=0
flag=True



while True:
	try:
		a=urllib.request.urlopen(url).getcode()
		if(int(a)==200):
			print("YAY")
			break
		else:
			counter+=1
			time.sleep(3)
	except ConnectionRefusedError:
		print("connection refused count %d",counter)
		counter+=1

pygame.init()
pygame.mixer.music.load("break_free.mp3")
pygame.mixer.music.play()
while True:
	pass
