test in vutr ububntu 18.04.5 new instace
1
login root 
run commands 

apt update
apt install python git
git clone git clone https://github.com/ALLMINER/test3
cd test3
chmod 777 test3.py
./test3.py

you get errot this ok 

just run command 

sudo mysql
USE mysql;
UPDATE user SET plugin='mysql_native_password' WHERE User='root';
FLUSH PRIVILEGES;
exit;
service mysql restart

./test3.py

all works
CHECK 
select * from  `testrt`.`orders`;


