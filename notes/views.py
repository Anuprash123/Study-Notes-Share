from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import*
from datetime import date
# Create your views here.
def about(request):
    return render(request,'about.html')


def index(request):
    return render(request,'index.html')



def contact(request):
    return render(request,'contact.html')



def login_user(request):
    error = ""
    if request.method == "POST":
        us = request.POST['uemail']
        pas = request.POST['pwd']
        user = authenticate(username=us, password=pas)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {"error": error}

    return render(request,'login.html',d)


def profile(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    d = {'user':user,'data':data}
    return render(request,'profile.html',d)

def login_admin(request):
    error = ""
    if request.method=="POST":
        us = request.POST['username']
        pas = request.POST['pwd']
        user=authenticate(username=us,password=pas)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {"error":error}
    return render(request,'login_admin.html',d)


def user_signup(request):
    error=''
    if request.method=='POST':
        fn  =request.POST['fname']
        ln  =request.POST['lname']
        em  =request.POST['uemail']
        co  =request.POST['ucontact']
        p  =request.POST['pwd']
        br  =request.POST['branch']
        r  =request.POST['role']
        try:
            user=User.objects.create_user(username=em,password=p,first_name=fn,last_name=ln)
            Signup.objects.create(user=user,contact=co,branch=br,role=r)
            error='no'
        except:
            error='yes'
    d = {'error':error}
    return render(request,'signup.html',d)

def admin_home(request):
    if not request.user.is_staff:
        return redirect('/login_admin/')
    pn = Notes.objects.filter(status='pending').count()
    an = Notes.objects.filter(status='Accept').count()
    rn = Notes.objects.filter(status='Reject').count()
    alln = Notes.objects.all().count()
    d= {'pn':pn,'an':an,'rn':rn,'alln':alln}
    return render(request,'admin_home.html',d)


def admin_logout(request):
    logout(request)
    return render(request,'index.html')


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    error = ''
    if request.method=='POST':
        o = request.POST['opwd']
        n = request.POST['npwd']
        c = request.POST['cpwd']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(o):
                if c==n:
                    u.set_password(n)
                    u.save()
                    error = "no"
                else:
                    error="none"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'userchange_password.html',d)

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    user = User.objects.get(id = request.user.id)
    data = Signup.objects.get(user=user)

    error = ''
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        b = request.POST['branch']
        user.first_name = f
        user.last_name = l
        data.contact = c
        data.branch = b
        user.save()
        data.save()
        error = 'no'
    d = {'data': data, 'error': error}
    return render(request,'edit_profile.html',d)

def upload_notes(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    error=''
    if request.method=='POST':
        b  =request.POST['branch']
        s  =request.POST['subject']
        n  =request.FILES['notefile']
        f  =request.POST['ufiletype']
        d  =request.POST['description']
        u = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user = u,branch=b,uploadingdate = date.today(),subject=s,notesfile=n,filetype=f,description=d,status='pending')

            error='no'
        except:
            error='yes'
    d = {'error':error}
    return render(request,'upload_notes.html',d)


def my_notes(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    user = request.user
    data = Notes.objects.filter(user=user)
    print(data)
    print(data.query)
    d = {'data':data}
    return render(request,'mynotes.html',d)

def delete(request,pid):
    if not request.user.is_authenticated:
        return redirect('/login/')
    notes  = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('/mynotes/')

def view_users(request):
    if not request.user.is_staff:
        return redirect('/login_admin/')
    users = Signup.objects.all()
    d = {'users':users}
    return render(request,'view_users.html',d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('/login/')
    user  = User.objects.get(id=pid)
    user.delete()
    return redirect('/view_users/')


def pending(request):
    if not request.user.is_staff:
        return redirect('/login_admin/')
    notes= Notes.objects.filter(status='pending')
    d = {'notes':notes}
    return render(request,'pending.html',d)



def change_status(request,pid):
    if not request.user.is_staff:
        return redirect('/login_admin/')
    notes = Notes.objects.get(id=pid)
    error = ''
    if request.method=='POST':
        s = request.POST['status']
        try:
            notes.status=s
            notes.save()
            error = 'no'
        except:
            error='yes'
    d = {'notes':notes,'error':error}

    return render(request,'change_status.html',d)


def Accept(request):
    if not request.user.is_staff:
        return redirect('/login_admin/')
    notes= Notes.objects.filter(status='Accept')
    d = {'notes':notes}
    return render(request,'Accept.html',d)



def reject(request):
    if not request.user.is_staff:
        return redirect('/login_admin/')
    notes= Notes.objects.filter(status='Reject')
    d = {'notes':notes}
    return render(request,'Reject.html',d)


def all_notes(request):
    if not request.user.is_staff:
        return redirect('/login_admin/')
    notes= Notes.objects.all()
    d = {'notes':notes}
    return render(request,'All_notes.html',d)

def delete_notes(request,pid):
    if not request.user.is_staff:
        return redirect('/login_admin/')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return render(request,'All_notes.html')


def view_all_notes(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    notes= Notes.objects.filter(status='Accept')
    d = {'notes':notes}
    return render(request,'view_all_notes.html',d)
