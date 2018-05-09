from src.app import app

__author__ = 'stoxxe'

app.run(debug=app.config['DEBUG'], port=4990)
