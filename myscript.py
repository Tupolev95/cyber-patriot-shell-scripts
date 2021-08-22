
##this section of the program is meant to remove unathorized users
## you must first input how many authorized users according to the readme you should have, then thier names, then it will promt you to delete users not on said list 
##NOTE!!! DO NOT TYPE Y FOR EVERY USER THAT IT PROMPTS YOU TO DELETE! some of them may be system accounts, if you wish, investigate further


import os


##amount of users

nusers = int(input())
print(nusers)

## input for valid users NOTE: also input valid admins


users = []

while len(users) < nusers:
	users.append(input())
	print(users)
	

##this prints all users and thier group
users2 = []

p = []
import pwd, grp


#this prints all JUST users in the system
for p in pwd.getpwall():
	users2.append(p[0])

print("users2=", users2)

##creates masterlist; a list of all users that should be on the vm

masterlist = ["root", "deamon", "bin", "sys", "sync", "games", "man", "lp", "mail", "news", "uucp", "proxy", "www-data", "backup", "list", "irc", "gnats", "nobody", "systemd-network", "systemd-resolve", "systemd-timesync", "messagebus", "syslog", "_apt", "tss", "uuidd", "tcpdump", "avahi-autoipd", "usbmux", "rtkit", "dnsmasq", "cups-pk-helper", "speech-dispatcher", "speed-dispatcher", "avahi", "kernoops", "saned", "nm-openvpn", "hplip", "whoopsie", "colord", "geoclue", "pulse", "gnome-initial-setup", "gdm", "systemd-coredump", "root"]

##adds all the users typed in at the beginning from the read me to the masterlist
masterlist.extend(users)

print(masterlist)


## this creates the list users3 which is the diffrence between users2 and the masterlist
users3 = set(users2) ^ set(masterlist)

print("users3 =", users3)



import subprocess
import sys
import getpass

for x in users3:
	yn = input("would you like to delete user" + x + "? ")
	if yn == "y":
		output = subprocess.run(['userdel', x ])
			
			







