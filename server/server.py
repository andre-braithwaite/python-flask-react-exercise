from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

recent = [] # Keep a local list of the 5 most recently retrieved users
# Reduces calls to external site reqres.in

def getUser(id):
    url = requests.get( "https://reqres.in/api/users/" + str(id) )
    userDict = json.loads(url.text) # Convert String to Python Dictionary
    return userDict["data"] # Only keep data related to the user


def checkRecent(id):
    global recent

    if not any(_["id"] == id for _ in recent):
        if len(recent) > 5:
            recent.pop(0) # Remove the oldest item from the recent list to make room for a new item
            
        recent.append(getUser(id)) # Add retrieved user to the recent list if not present
    
    return next(_ for _ in recent if _["id"] == id) # Send the user json from the recent list


@app.route("/user/<int:id>/", methods=['GET'])
def displayUserDetails(id):
    return checkRecent(id)


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')