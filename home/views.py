from django.shortcuts import render,HttpResponse
import pyrebase
from django.contrib import auth
from django.contrib import  messages
# from template.forms import CreateUserForm, UserCreationForm

# Create your views here.
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
database=firebase.database()
storage = firebase.storage()

def login(request):
    return render(request,'login.html')

def postLogin(request):
    email=request.POST.get('email')
    passw=request.POST.get('password')
    name=email.split('@')
    name1=name[0]
    try:
        user=authe.sign_in_with_email_and_password(email,passw)
        print(user)
        s_id=user['idToken']
        # uname=user['idToken']
        request.session['uid']=str(s_id)
    except:
        # messages.error(request, f"Invalid username or password")
        message="invalid credentials"
        return render(request,'login.html',{'m':message})    
    return render(request,'home.html',{"e":name1})

def register(request):
    return render(request,'register.html')
def Signup(request):
    email=request.POST.get('email')
    username=request.POST.get('username')
    passw=request.POST.get('password')
    passw2=request.POST.get('password2')
    if passw==passw2:
        try:
            user1=authe.create_user_with_email_and_password(email,passw)
            uid=user1['localId']
            data={'name':username, 'status':'1'}
            database.child("users").child(uid).child('detailsa').set(data)
            

        except:
            message="unable to create account try again"
            return render(request,'register.html',{'m':message})
    else:
        message3="Passwords donot Match"
        return render(request,'register.html',{'m':message3})  
    # message1='successffull'          
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')
    
def study(request):
    idtoken=request.session['uid']
    a=authe.get_account_info(idtoken)
    a=a['users']
    a=a[0]
    # print(a)
    a=a['localId']
    url_list=[]
    for i in range(1,5):
        url=storage.child("Java/{}.pdf".format(i)).get_url(a)
        url_list.append(url)
    print(url_list) 
    uname=storage.child("Java/2.pdf").get_name(a)
    print(uname)       
    return render(request,'blog.html',{'u':url_list})

def career(request):
    return render(request,'course.html')    