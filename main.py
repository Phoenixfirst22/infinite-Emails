import requests

from bs4 import BeautifulSoup


def error(k):
    print(f"Error response.status_code = {k}\n could not access url")

emails = []

def minutemail():
    global emails


    try:
        response = requests.get("https://10minutemail.net")

        if response.status_code in [200, 201]:

            soup = BeautifulSoup(response.text, "html.parser")

            email = soup.find("button", {"id": "copy-button"})

            if email is not None:
                print(email["data-clipboard-text"])

                emails.append(email["data-clipboard-text"])



            else:
                print("Could not find email element")

        else:
            error(response.status_code)

    except:
        error(response.status_code)



def addToTxt(list_):

    for item in list_:

        with open("emails.txt", "a") as f:

            f.write("".join(item) + "\n")




def inspect_userInput():

    while True:

        try:
            userOption = int(input("Number of emails: "))

            break

        except:

            print("please enter a valid number like 10")
    return userOption

userOption = inspect_userInput()


for k in range(userOption):

    minutemail()


addToTxt(emails)

