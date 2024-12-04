from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import creatuserform

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'index.html')
def calculator(request):
    c =''
    data = {}
    try:
        if request.method == 'POST':
            a = eval(request.POST.get('num1'))
            b = eval(request.POST.get('num2'))
            opr = request.POST.get('opt')
            if opr == '+':
                c = a+b
            elif opr == '-':
                c = a-b
            elif opr == '*':
                c = a*b
            elif opr == '/':
                c = a/b

        data ={
            'a':a,
            'b':b,
            'c' : c
        }
    except:
        data ={'c': 'invalid'}

    return render(request, "calc.html", data)


def marksheet(request):
    res ={}
    total =''
    try:
        if request.method == 'POST':
            s1 = eval(request.POST.get("sub1"))
            s2 = eval(request.POST.get("sub2"))
            s3 = eval(request.POST.get("sub3"))
            s4 = eval(request.POST.get("sub4"))
            s5 = eval(request.POST.get("sub5"))
            total = (s1+s2+s3+s4+s5)
            per = (total/500)*100
        res= {
            's1':s1,
            's2': s2,
            's3': s3,
            's4': s4,
            's5': s5,
            'total': total,
            'per': per

            }
    
    except:
        res = {'total': 'invalid'}
        
    return render(request, 'mark.html',res)



def sign(request):
    
    form = creatuserform()

    if request.method == 'POST':
        form = creatuserform(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request,'sign.html',context)

def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password = password)
        print(user)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'email or Password is incorrect')
    
    return render(request,'login.html')