from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import speech_recognition as sr
import json
import os
import signal


# class TimeoutException(Exception):   # Custom exception class
#     pass
# def timeout_handler(signum, frame):   # Custom signal handler
#     raise TimeoutException
# # Change the behavior of SIGALRM
# signal.signal(signal.SIGALRM, timeout_handler)


MY_PATH = "/home/p/Documents/Code/speechToText/sourceCode"
app = Flask(__name__)
api = Api(app)

@app.route('/audio/speechtotext', methods=['POST'])
def speech_to_text():

    response_data = dict()
    # signal.alarm(5) 
    try:
        form_data = json.loads(request.data)
        file_path = MY_PATH + "/" + form_data["filename"]
        if os.path.isfile(file_path):
            r = sr.Recognizer()
            text_of_file = ""
            # open the file
            with sr.AudioFile(file_path) as source:
                # listen for the data (load audio to memory)
                audio_data = r.record(source)
                # recognize (convert from speech to text)
                text = r.recognize_google(audio_data)

            response_data["success"] = True
            response_data["word"] = text
            response = jsonify(response_data)
            return response
        else:
            response_data["success"] = False
            response = jsonify(response_data)
            return response    
    except Exception:
        pass
    else:
        pass
        # signal.alarm(0)
    response_data["success"] = False
    response = jsonify(response_data)
    return response 




app.run()