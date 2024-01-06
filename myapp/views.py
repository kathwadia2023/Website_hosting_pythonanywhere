from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from FinalProject import settings
import requests
import random

# Create your views here.
status = False
def index(request):
    global status
    if request.method =='POST':
        if request.POST.get('signup')=='signup':
            newuser = signup_form(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Success")
            else:
                print(newuser.errors)
         
        elif request.POST.get('login')=='login':
            unm = request.POST['username']
            pswd = request.POST['password']

            user=signupmaster.objects.filter(username = unm, password=pswd)
            fnm_session = signupmaster.objects.get(username=unm)
            uid = signupmaster.objects.get(username=unm)
            print(uid.id)
            print("firstname:", fnm_session.firstname)
            if user:
               
                print("login Success")
                # msg = "login Success"
                status = True
                request.session['user']= fnm_session.firstname
                request.session['uid']=uid.id
                return redirect("notes")
            else:
                print("Login fail ,plz try again!!!")


    return render(request,'index.html')


def notes(request):
    # global status
    if request.method =='POST':
        # if request.POST.get('submit post')=='submit post':
        new_notes = Notes_form(request.POST, request.FILES)
        if new_notes.is_valid():
            new_notes.save()
            print("Success")
        else:
            print(new_notes.errors)
    user=request.session.get('user')
    return render(request,'notes.html', {'user':user})
# , {'new_notes':new_notes}) 

def profile(request):
    user=request.session.get('user')
    uid = request.session.get('uid')
    c_user = signupmaster.objects.get(id=uid)
    if request.method =='POST':
        newuser = update_form(request.POST, instance=c_user)
        if newuser.is_valid():
            newuser.save()
            print("Profile updated")
            return redirect('notes')
        else:
            print(newuser.errors)
    return render(request,'profile.html',{'user':user, 'c_user':c_user}) 

def about(request):
    return render(request,'about.html') 

def contact(request):
    if request.method == "POST":
        newfeedback = Feedback_form(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Feedback saved")
            ran_otp = random.randint(11111,99999)
        # send mail
            sub="Thank you"
            message = f"Hello {request.POST['name']}! \n\nWe have Received Your feedback.\nWe will contact you shortly...\nIf any Queries, plz feel free to contact us...\nRegards \nNotes Company PVT. LTD."
            frm_mail = settings.EMAIL_HOST_USER
            to_mail=['djangotestingpython@gmail.com', request.POST['email']]
            send_mail(subject=sub, message=message, from_email=frm_mail, recipient_list=to_mail)
        
        # OTP sending
            
            url = "https://www.fast2sms.com/dev/bulkV2"

            querystring = {"authorization":"8yBMwGHNWIShkxe1EZumYUa4pTR0oAKjqPOVn36il7g2zQdrFJh4tvYQJCN87IyUMlqTiEkPpgV90FOG","variables_values":f"ran_otp","route":"otp","numbers":request.POST['mobile']}

            headers = {
                        'cache-control': "no-cache"
                        }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)
        
        else:
            print(newfeedback.errors)
    return render(request,'contact.html') 

def user_logout(request):
    logout(request)
    return redirect('/')

