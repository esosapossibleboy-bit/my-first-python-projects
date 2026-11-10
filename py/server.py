from flask import Flask, request, jsonify
from flask_cors import CORS

# Turn on our Flask app server machine
app = Flask(__name__)
CORS(app) # This opens the window so the browser is allowed to talk to us!

@app.route("/save", methods=["POST"])
def save_idea_api():
    # 1. Grab the data sliding through the drive-thru window
    data = request.json
    received_idea = data.get("idea", "")
    
    print(f"📥 SERVER RECEIVED WORK ORDER: {received_idea}")
    
    # 2. Open our notebook file on the hard drive and write it down permanently!
    file = open("web_ideas.txt", "a") # 'a' means append/add to the end
    file.write(received_idea + "\n")
    file.close()
    
    # 3. Slide a success receipt back to the browser
    return jsonify({"status": "Success", "message": "Saved to computer hard drive!"})

# Start our server machine on channel port 5000
if __name__ == "__main__":
    app.run(port=5000)
