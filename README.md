# BruteF0rcePyth0n
Using Python for brute-forcing the username and password on the site's login page.

This is a Python script used for brute forcing into the site's login page. 
Assumptions:

    -> Example site: http://example.com
    -> login page: http://example.com/login
  These assumptions are modifiable.

Running the script:
  Open the terminal/ cmd
  Clone the repository: "git clone https://github.com/prasad-1808/BruteF0rcePyth0n/"
  Move to the folder: cd BruteF0rcePyth0n
  Run: python brute.py -t <http://example.com> -u username.txt -p password.txt

The username.txt and password.txt can be modified but make sure the files are in the same directory or declare the address of the files properly.


I have attached some of the username and password list that contains a huge amount of data.
These files can be cloned and modified with the runnable script

        Common Username: https://github.com/danielmiessler/SecLists/tree/master/Usernames/Names
        Common Password: https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials

Using huge amounts of data on a local device can cause lag in the system. 
Use with Cause.
