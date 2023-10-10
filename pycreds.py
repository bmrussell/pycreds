import keyring
import glob
import os
from pathlib import Path

def main():
    """
    Demonstrates setting credentials in the windows credential store
    Reading the plain text from a file and deleting it after
    So an app without logon can set the credentials initially
    """
    
    credfiles = glob.glob("*.cred")
    for credfile in credfiles:
        with open(credfile, mode='r') as file:
            username = file.readline().strip()
            password = file.readline().strip()
        
        keyring.set_password(Path(credfile).stem, username, password)
        os.remove(credfile)

if __name__ == '__main__':      
    main()
    exit(0)
    