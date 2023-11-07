from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

# Create the server
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jxaeaeqq:uLwG0gBcBoytEOnJHP2PEZGSK0EyUMP4@trumpet.db.elephantsql.com/jxaeaeqq"
# os.environ['DATABASE_URL']
db = SQLAlchemy(app)

from application import routes