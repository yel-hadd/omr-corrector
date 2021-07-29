import pyrebase
import re
import captcha

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

firebaseConfig = {
  'apiKey': "AIzaSyAA-fr7u1EH-ANAsEIMg1gzCWaARqm5evg",
  'authDomain': "maxi-auth.firebaseapp.com",
  'projectId': "maxi-auth",
  'storageBucket': "maxi-auth.appspot.com",
  'messagingSenderId': "407745641410",
  'appId': "1:407745641410:web:8cc65210075eb233c2b45b",
  'measurementId': "G-W7S2MKXSXD",
  'databaseURL': None
}


firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()


def login(email, password):
    if not(re.match(regex, email)):
        return 0
    # "Invalid Email Address"
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        return 1
            #"Successfully logged in!"
    except:
        return 2
            #"Invalid email or password"

#Signup Function

def signup(email, password):
    if not(re.match(regex, email)):
        return 0
        #"Invalid Email Address"
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return 1
        #'You have signed up successfully'
    except:
        return 2
        #"Email already exists"