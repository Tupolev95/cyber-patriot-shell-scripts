chmod 700 /home/test/Documents/myscript.sh
sudo ufw enable
sudo ufw logging on
sudo apt update 
sudo apt upgrade
sudo apt-get install libpam-cracklib
sudo apt-get install auditd
sudo auditctl -e 1 #enables auditing, 0 disables
sudo /usr/lib/lightdm/lightdm-set-defaults -l false #disables guest account
sudo auditctl -w /etc/shadow -p wa
sudo auditctl -w /etc/passwd -p wa
sudo auditctl -w /etc/group -p wa
sudo auditctl -w /etc/sudoers -p wa
sudo auditctl -e 1
sudo gedit /etc/pam.d/common-password #at the end of line 25 add remember=5 minlen=10 difok=3 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
sudo gedit /etc/pam.d/common-auth #make a new line at the end and write auth required pam_tally2.so deny=5 onerr=fail unlock_time=1800
sudo gedit /etc/login.defs #starting at line 160, change values to 90, 10 and 7
sudo gedit /etc/ssh/sshd_config #PermitRootLogin no
