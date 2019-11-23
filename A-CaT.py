#!/usr/bin/python3
#-*- coding: utf-8 -*-
__msg__ = '''
Hello, this is my Tool and thanks
for download :)
don't edit a tools -_-
'''
try:
	import os,json,requests,sys,getpass
	from time import sleep
	from random import randint
except:
	import os,sleep
	os.system("cls || clear")
	print("\n\033[32;1m Hello plase Enter for download...\n")
	time.sleep(2)
	os.system("./install.aex")
class start():
	def banner(self):
		if os.name == "nt":
			os.system("cls")
		elif os.name == "prosix":
			os.system("clear")
		else:
			os.system("cls || clear")
		logo = """\033[32;1m	
           |`\\_,--="=--,_//`|
           \ ."  :'. .':  ". /
          ==)  _ :  '  : _  (==
            |>/\033[36;1mO\033[32;1m\   _   /\033[33;1mO\033[32;1m\<|
            | \-"~` _ `~"-/ |
           >|`===. \_/ .===`|<
     .-"-.   \==='  |  '===/   .-"-.
.---{'. '`}---\,  .-'-.  ,/---{.'. '}---.
 )  `"---"`     `~-===-~`     `"---"`  (
(\033[33;1m  By: \033[36;1mFox Benghazi \033[32;1m                   )
(\033[33;1m  mail: \033[36;1mzero.day.attack77@gmail.com \033[32;1m  )
 )\033[33;1m fb: \033[36;1mhttps://m.fb.com/fox.benghazi\033[32;1m   (
'---------------------------------------'
 ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ ____ ____ 
||\033[31;1mF \033[32;1m|||\033[31;1mo\033[32;1m |||\033[31;1mx\033[32;1m |||       |||\033[31;1mB \033[32;1m|||\033[31;1me\033[32;1m |||\033[31;1mn \033[32;1m|||\033[31;1mg\033[32;1m |||\033[31;1mh \033[32;1m|||\033[31;1ma\033[32;1m |||\033[31;1mz \033[32;1m|||\033[31;1mi\033[32;1m ||
||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
		"""
		for ban in range(len(logo)):
			sleep(0.002)
			print(logo[ban],end='')
	def get_token(self):
		print("\n")
		email = str(input("\033[36;1mEnter email :\033[32;1m "))
		print('\033[36;1m')
		password = getpass.getpass()
		url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+str(email)+"&locale=en_US&password="+str(password)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
		r = requests.get(url)
		http = r.content
		http = http.decode("utf-8")
		js = json.loads(http)
		os.system("clear")
		token = js["access_token"]
		print(token)
	
	def __emails__(self):
 		token=str(input("""\033[36;1m
 plase paste a token : \n \033[33;1m
"""))
 		url = str("https://graph.facebook.com/me/friends?access_token={}".format(token))
 		rq = requests.get(url)
 		a = rq.text
 		os.system("clear")
 		if '"error": {' in a:
		 	print("Error:")
		 	print("1) not token")
		 	print("2) account is locked")
		 	print("3) Error unknow")
		 	sys.exit()
 		else:
		 	j = json.loads(a)
		 	for i in j["data"]:
		 		try:
		 			url2 = "https://graph.facebook.com/{}?access_token={}".format(i["id"],token)
		 			ok = requests.get(url2)
		 			ou = ok.text
		 			ju = json.loads(ou)
		 			print("#"*20)
		 			print("-"*20)
			 		em = ju["email"]
			 		print("email : "+str(em))
				 	print("#"*20)
		 		except KeyError:
				 	pass
	
	def info(self):
		token=str(input("""\033[36;1m
 plase paste a token : \n \033[33;1m
"""))
		url = str("https://graph.facebook.com/me/friends?access_token={}".format(token))
		rq = requests.get(url)
		a = rq.text
		os.system("clear")
		if '"error": {' in a:
			print("Error:")
			print("1) not token")
			print("2) account is locked")
			print("3) Error unknow")
			sys.exit()
		else:
			j = json.loads(a)
			for i in j["data"]:
				try:
					url2 = "https://graph.facebook.com/{}?access_token={}".format(i["id"],token)
					ok = requests.get(url2)
					ou = ok.text
					ju = json.loads(ou)
					print("#"*20)
					print("name : "+str(ju["name"]))
					print("id : "+str(ju["id"]))
					print("-"*20)
					em = ju["email"]
					print("email : "+str(em))
					print("#"*20)
				except KeyError:
					pass



num = randint(1,2)
if num == 1:
	os.system("cls || clear")
	sleep(0.1)
	os.system("toilet -f big --filter metal 'A CaT'")
else:
	os.system("cls || clear")
	sleep(0.1)
	os.system("toilet -f bigmono12 'A CaT' | lolcat")

run=start()
print("""
  \033[36;1m[\033[31;1m01\033[36;1m] \033[33;1mget token
  
  \033[36;1m[\033[31;1m02\033[36;1m] \033[33;1mget emails
  
  \033[36;1m[\033[31;1m03\033[36;1m] \033[33;1minfo
  
  \033[36;1m[\033[31;1m00\033[36;1m] \033[33;1mexit
\n
""")
try:
	inpo = str(input("\033[36;1m===> \033[32;1m"))
except KeyboardInterrupt:
	print("\033[33;1m\n \t CTRL + C \n ")
	sys.exit()
if inpo == "1" or inpo == "01":
	run.banner()
	run.get_token()
elif inpo == "2" or inpo == "02":
	run.banner()
	run.__emails__()
elif inpo == "3" or inpo == "03":
	run.banner()
	run.info()
elif inpo == "0" or inpo == "00":
	print("\n \t ok \n ")
	sys.exit()
else:
	print("\n \t try aging \n")
	enter=str(input("[ Enter ] "))
	os.system("python3 Acat.py")



__end__ = '''

This is end a tool ^_^
Here her story ends and I will go back to sleep *-*
And I love authenticating girls xD
If you change something from the tool, fuck yourself bro XD
'''
