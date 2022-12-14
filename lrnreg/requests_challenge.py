#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

# Define our "base" API
API = "https://opentdb.com/api.php?amount=5&category=18&difficulty=medium&type=boolean"

def main():
    """Run time code"""

    # create resp, which is our request object
    data = requests.get(API).json()

    #print("data: ", data)
    #print("")

    for questions_dict in data.get("results"):
        #print(questions_dict)
        print("")
        print(questions_dict["question"])
        print("")
        print(questions_dict["incorrect_answers"])
        print("")
        print(questions_dict["correct_answer"])



if __name__ == "__main__":
    main()

