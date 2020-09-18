#!/usr/bin/env python3.6
# coding: utf-8

import subprocess
import sys
import os
from subprocess import check_call, CalledProcessError

try:
   check_call(['apt-get', 'install', '-y', 'mariadb-server', 'python3-pip', 'cmake', 'curl', 'libssl-dev'], stdout=open(os.devnull,'wb'))

except CalledProcessError as e:
  print(e.output)



import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS testrt")
mycursor.execute("CREATE DATABASE IF NOT EXISTS  testrt")
mycursor.execute("CREATE USER IF NOT EXISTS  'test'@'localhost' IDENTIFIED BY 'test'")
mycursor.execute("GRANT INSERT,SELECT,UPDATE ON testrt.* to 'test'@'localhost'")
mycursor.execute("CREATE TABLE `testrt`.`customers` (`customer_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, `customer_name` VARCHAR(30) NOT NULL)")
mycursor.execute("CREATE TABLE `testrt`.`orders` (`order_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY Key, `order_name` VARCHAR(50) NOT NULL, `customer_id` INT UNSIGNED NOT NULL, FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON UPDATE CASCADE ON DELETE RESTRICT)")

sql = "INSERT INTO testrt.customers (customer_name) VALUES (%s),(%s)"
val= ("joe"),("smith")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO testrt.orders (order_name,customer_id) VALUES (%s,%s)"
val= ("cookie", 1)
mycursor.execute(sql, val)
print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO testrt.orders (order_name,customer_id) VALUES (%s,%s)"
val= ("water", 2)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
