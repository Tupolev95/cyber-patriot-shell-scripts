import os
cmd = 'ls -l'
os.system(cmd)



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
for p in pwd.getpwall():
	print(p[0], grp.getgrgid(p[3])[0])

#this prints all JUST users in the system
for p in pwd.getpwall():
	users2.append(p[0])

print("users2=", users2)

##creates masterlist; a list of all users that should be on the vm

masterlist = ["root", "deamon", "bin", "sys", "sync", "games", "man", "lp", "mail", "news", "uucp", "proxy", "www-data", "backup", "list", "irc", "gnats", "nobody", "systemd-network", "systemd-resolve", "systemd-timesync", "messagebus", "syslog", "_apt", "tss", "uuidd", "tcpdump", "avahi-autoipd", "usbmux", "rtkit", "dnsmasq", "cups-pk-helper", "speech-dispatcher", "speed-dispatcher", "avahi", "kernoops", "saned", "nm-openvpn", "hplip", "whoopsie", "colord", "geoclue", "pulse", "gnome-initial-setup", "gdm", "systemd-coredump", "root"]

masterlist.extend(users)

print(masterlist)



users3 = set(users2) ^ set(masterlist)

print("users3 =", users3)

##import getent
##this was an attempt to use getent but it didnt work :(
##print(dict(getent.passwd('root')))


import subprocess



##process = subprocess.run(['getent','passwd', '{1000..60000}'], stdout=subprocess.PIPE)
	
##print(process.stdout.decode())

print(os.popen("getent passwd {1000..60000}").read())


