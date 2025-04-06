from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 CXION Bot is Live – Welcome to CX Universe!"

@app.route('/ask', methods=['POST'])
def ask_bot():
    user_input = request.json.get('message', '')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = f"Hello! You said: {user_input}. I'm CXION, your AI bot."
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
