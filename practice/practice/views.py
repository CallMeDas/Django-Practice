from django.shortcuts import render
from django.http import HttpResponse

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
            total = (s1+s2+s3+s4+s5)/5
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