import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:\Users\Dorian\Downloads\hackathon-98900-firebase-adminsdk-w4mr8-eb9576c9de.json")
firebase_admin.initialize_app(cred)

db = firestore.client()