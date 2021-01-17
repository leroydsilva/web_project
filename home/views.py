from django.shortcuts import render,redirect,HttpResponse
import pyrebase
from django.contrib import auth
from django.contrib import  messages
import firebase_admin
from firebase_admin import credentials,firestore
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
cred=credentials.Certificate("static/fir-e40d9-firebase-adminsdk-qqywy-907f53f70d.json")
firebase_admin.initialize_app(cred)
firebase_db=firestore.client()

def home(request):
    return render(request,'home.html')

def postLogin(request):
    if request.method=='POST':
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
            return redirect('home:home')


        except:
            # messages.error(request, f"Invalid username or password")
            message="invalid credentials"
            return render(request,'login.html',{'m':message})    
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
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
    return render(request,'register.html')

    


def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass    
    return render(request,'login.html')
    
def study(request):
    idtoken=request.session['uid']
    a=authe.get_account_info(idtoken)
    a=a['users']
    a=a[0]
    # print(a)
    a=a['localId']
    url_list=[]
    url_list1=[]
    for i in range(1,5):
        url=storage.child("Java/{}.pdf".format(i)).get_url(a)
        url_list.append(url)
    for i in range(1,6):
        url=storage.child("python/{}.pdf".format(i)).get_url(a)
        url_list1.append(url)    
    # print(url_list)
    snapshots=list(firebase_db.collection(u'python').get())
    l=[]
    for s in snapshots:
        l.append(s.to_dict())
    # print(l) 
    pnames=[]
    for a in l:
        pnames.append(a.get('name'))   
    # print(pnames)   
    # print(l)    
    # for key,val in dic:
    #     dic
    
          
    return render(request,'blog.html',{'u':url_list,'p_list':url_list1,'v':pnames})

def course(request):
    return render(request,'course.html')    

def contact(request):
    return render(request,'contact.html')    