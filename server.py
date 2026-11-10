import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import nest_asyncio
import g4f

# Activate the asynchronous bridge safely
nest_asyncio.apply()

app = Flask(__name__)
CORS(app)

print("\n🌐 Aligned to Live AI & Data Purge Engine Core... 🌐")
print("🚀 SUCCESS! Your server is live at: http://localhost:8000\n")

def read_ideas_from_file():
    try:
        file = open("web_ideas.txt", "r")
        lines = file.readlines()
        file.close()
        ideas = []
        for line in lines:
            if line.strip():
                ideas.append(json.loads(line.strip()))
        return ideas
    except:
        return []

def rewrite_ideas_to_file(ideas_list):
    file = open("web_ideas.txt", "w")
    for item in ideas_list:
        file.write(json.dumps(item) + "\n")
    file.close()

@app.route("/save", methods=["POST"])
def save_idea_api():
    data = request.json
    user_idea = data.get("idea", "")
    
    print(f"🧠 Contacting Live AI Cloud for concept: '{user_idea}'...")
    
    try:
        # Requesting a response from a live online cloud model
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": f"Give a brief 2-sentence software engineering advice blueprint for: {user_idea}"}],
        )
        # Verify we got a real message back, otherwise use fallback
        if response and len(str(response).strip()) > 5:
            ai_feedback = str(response)
        else:
            raise Exception("Empty response")
    except Exception as e:
        print("⚠️ Cloud network busy, deploying internal AI blueprint helper...")
        ai_feedback = f"💡 Local Engine: Great concept! To build '{user_idea}', you should design a frontend architecture with HTML/CSS and connect it to a structured backend data manager."

    data_record = {
        "user_input": user_idea,
        "ai_response": ai_feedback
    }
    
    file = open("web_ideas.txt", "a")
    file.write(json.dumps(data_record) + "\n")
    file.close()
    
    return jsonify({"status": "Success", "ai_feedback": ai_feedback})

@app.route("/history", methods=["GET"])
def get_history_api():
    return jsonify(read_ideas_from_file())

@app.route("/delete", methods=["POST"])
def delete_idea_api():
    data = request.json
    index_to_delete = data.get("index")
    
    current_ideas = read_ideas_from_file()
    
    if 0 <= index_to_delete < len(current_ideas):
        removed = current_ideas.pop(index_to_delete)
        print(f"🗑️ PURGE WARNING: Erased '{removed['user_input']}' from the repository log.")
        rewrite_ideas_to_file(current_ideas)
        return jsonify({"status": "Success", "message": "Item deleted!"})
    
    return jsonify({"status": "Error", "message": "Index not found"}), 400

if __name__ == "__main__":
    app.run(port=8000)
