from flask import Flask
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
app = Flask(__name__)

@app.route('/')
def start():
  return render_template('index.html', artist='rihanna')

@app.route('/artist', methods=['GET'])
def artistGet():
  artist = request.args.get('artist')
  return render_template('index.html', artist=artist)

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')


