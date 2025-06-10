import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("library-system-9735d-firebase-adminsdk-fbsvc-3e3ee532ca.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://library-system-9735d-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
