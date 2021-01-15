from django.shortcuts import render
import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyCdN5oARybbw6EfrNajWd1s4M6ZrD5tFvE",
  "authDomain": "fir-e40d9.firebaseapp.com",
  "databaseURL": "https://fir-e40d9.firebaseio.com",
  "projectId": "fir-e40d9",
  "storageBucket": "fir-e40d9.appspot.com",
  "messagingSenderId": "488597332661",
  "appId": "1:488597332661:web:3a4c2811f70133cc6d94fc",
  "measurementId": "G-5G4XLLSS2B"
}  
firebase = pyrebase.initialize_app(firebaseConfig)
authe=firebase.auth()
# Create your views here.
def home(request):
    # uname=authe.get_account_info("email")
    # print(uname)
    # {"e":uname}
    return render(request,'home.html')

    