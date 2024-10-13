from flask import Flask
from config import Config
from firebase_admin import credentials, initialize_app, firestore
import os

app = Flask(__name__)
app.config.from_object(Config)

# Firebase configuration with a raw string
cred = credentials.Certificate(r'D:\Downloads\27 sep mand a\27 sep mand a\heaxaware M&A\skill-navi-a0aad-firebase-adminsdk-c7hbt-9cc99e875f.json')  # Use a raw string
firebase_app = initialize_app(cred)  # Initialize Firebase
db = firestore.client()  # Firestore client instance

# Move this import to the bottom to avoid circular imports
from app import routes
