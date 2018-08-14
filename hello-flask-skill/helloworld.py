import logging
import os

from flask import Flask
from flask_ask import Ask, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    speech_text = 'Welcome to Hello World, you can say hello'
    return question(speech_text)


@ask.intent('HelloWorldIntent', default={'name': 'World'})
def hello_world(name):
    speech_text = f'Hello, {name}'
    return question(speech_text)


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me, or ask me to say hello to someone!'
    return question(speech_text)


@ask.intent('AMAZON.StopIntent')
def stop():
    stop_text = 'Goodbye world!'
    return statement(stop_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    app.run(debug=True)
