import firebase_admin


cred_obj = firebase_admin.credentials.Certificate("countingpeople-f2000-firebase-adminsdk-qizfa-44872a8ce6.json")
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': "https://countingpeople-f2000-default-rtdb.europe-west1.firebasedatabase.app"
	})
from firebase_admin import db
ref=db.reference("/")
ref.set({
 "Square":
 {
     "times":-1}
})
 
 