from flask import Flask, render_template, url_for, request, redirect, Blueprint, session
import requests

main = Blueprint('main',__name__)

@main.route("/")
def home():
    advice = get_advice()
    return render_template('home.html',advice=advice)


def get_advice():
    url = "https://api.adviceslip.com/advice"

    response = requests.get(url)
    response_json = response.json()
    print
    try:
        advice = response_json['slip']['advice']
    except KeyError:
        advice = "Who even are you?\nNo advice to strangers -_-"

    return advice