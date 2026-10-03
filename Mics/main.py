from flask import Flask
from flask import render_template, request, redirect, url_for, session, jsonify
import base64
import model
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')


@app.route('/check', methods=["POST"])
def check():
	data = request.get_data()

	starter = data.find(b',')

	image_data = data[starter + 1:]

	open("login.png", "wb").write(
		base64.b64decode(image_data)
	)

	score = model.check()

	if score > 0.8:

		return jsonify({
			'score': score * 100,
			'access': 'granted',
			'text': (
				"Welcome X! Here is your flag: "
				"gctf26{**REDACTED**}"
			)
		})

	else:

		return jsonify({
			'score': score * 100,
			'access': 'denied',
			'text': (
				"AI detect that you didn't match X's face!"
			)
		})


@app.errorhandler(404)
def page_not_found(e):
	return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
	return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == '__main__':
	app.run(
		debug=True,
		host='0.0.0.0',
		port=80
	)
