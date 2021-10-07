import nltk
nltk.download('all')
from src.services.chat.chat_processor import get_best_context
from flask import Flask, request
import os


app = Flask(__name__)

@app.route('/chat', methods=['GET'])
def login():
	__message = request.get_json()["message"].lower()
	__contexts_array = request.get_json()["contexts"]
	
	return { "results":get_best_context(__contexts_array, __message) }


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(port=port, debug=True)