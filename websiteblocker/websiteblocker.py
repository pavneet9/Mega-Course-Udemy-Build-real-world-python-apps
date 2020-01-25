# Website Blocker File

### Import Libraries
import time
from datetime import datetime as dt
import os

### Constants
host_path = r'hosts'
redirect = "127.0.0.1"
website_lists = ["www.facebook.com" , "facebook.com", "www.youtube.com/"]

### Functions

# String, String, ListofWebsites > Boolean
# Check if the ListofWebsites are already their in the host file. Return 1 if they exist else return 0.
def check_if_exits(host_path, website_lists):
    x = 0
    with open("hosts","r+") as file:
        content = file.read()
        for website in website_lists:
            if website in content:
                return 1
                x=1
        if x == 0:
           return 0


# String, String, ListofWebsites, String, Boolean -> No return values
# This function adds or removes the ListofWebsites into the host File
# Actions-> 1 add website_lists , 0 remove website_lists
def change_host_file(host_path, website_lists, redirect, action):
    check = check_if_exits(host_path, website_lists)
    print action
    print check
    if(action != check):
        if action ==1:
            #file.seek(0,2)
            print ("check")
            with open("hosts","a") as file:
                for website in website_lists:
                    file.write(redirect + "    " + website + "\n")
        else:
            with open("hosts","a") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_lists):
                        file.write(line)
                file.truncate()

# Time of day -> Boolean
# Based on the time of the day, the
def time_to_change_host(host_path, website_lists, redirect):
    if dt.now() > dt( dt.now().year, dt.now().month, dt.now().day, 9) and dt.now() < dt( dt.now().year, dt.now().month, dt.now().day, 20):
       print("Gets here")
       change_host_file(host_path, website_lists, redirect, 1)
    else:
       change_host_file(host_path, website_lists, redirect, 0)

# As we want out program to run continously, we can put the logic to fire it in a while loop
# Sleep function is used to reduce memory consumption
while True:
    time_to_change_host(host_path, website_lists, redirect)
    time.sleep(3000)
