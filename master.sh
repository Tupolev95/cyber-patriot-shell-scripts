chmod 700 /CPscript/master.sh

sudo apt-get install libpam-pwquality
sudo apt-get install auditd 

##copies the common-password file from CPscript to the actual file location and replaces it
sudo cp -f /CPscript/common-password /etc/pam.d/common-password

sudo cp -f /CPscript/common-auth /etc/pam.d/common-auth

sudo cp -f /CPscript/login.defs /etc/login.defs

sudo cp -f /CPscript/audit.rules /etc/audit/audit.rules

sudo auditctl -e 1

sudo auditctl -l

sudo ufw enable
sudo ufw logging on
sudo ufw status
sudo find /home -iname *.mp3
