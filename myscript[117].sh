chmod 700 /home/test/Documents/myscript.sh
sudo ufw enable
sudo ufw logging on
sudo apt update 
sudo apt upgrade
sudo apt-get install libpam-cracklib
sudo apt-get install auditd
sudo auditctl -e 1 #enables auditing, 0 disables #once enabling, auditct -l shows the current settings, but after changing it and reseting it there is nothing, do i have to start and stop to edit?
sudo /usr/lib/lightdm/lightdm-set-defaults -l false #this doesnt work
sudo gedit /etc/audit/audit.rules #at the bottom, add lines -w /etc/shadow -p wa, -w /etc/passwd -p wa, -w /etc/group -p wa, -w /etc/sudoers -p wa (line should 
sudo gedit /etc/pam.d/common-password #at the end of line 25 add remember=5 minlen=10 difok=3 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
sudo gedit /etc/pam.d/common-auth #make a new line at the end and write auth required pam_tally2.so deny=5 onerr=fail unlock_time=1800
sudo gedit /etc/login.defs #starting at line 160, change values to 90, 10 and 7
sudo gedit /etc/ssh/sshd_config #PermitRootLogin no
#for the last 5 lines, do i have to use nano or can i use gedit?
