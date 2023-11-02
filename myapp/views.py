from django.shortcuts import render
from myapp.models import *
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, "register.html")
def login(request):
    return render(request, "login.html")

def register_result(request):
    idid = request.POST["id"]
    pwd = request.POST["pwd"]
    if len(idid) < 5:
        return render(request,"result.html",{"alert_string":"아이디가 5글자보다 작습니다","href":"/register"})
    if len(pwd) < 8:
        return render(request,"result.html",{"alert_string":"비밀번호가 8글자보다 작습니다","href":"/register"})

    
    try:
        if Member.objects.filter(memid=idid).exists():
            return render(request, "result.html",{"alert_string":"이미있는 id입니다.","href":"/register"})
        mem = Member(memid=idid,pwd=pwd)
        mem.save()
    except:
        return render(request, "result.html",{"alert_string":"회원가입에 실패했습니다.","href":"/register"})
    return render(request, "result.html",{"alert_string":"회원가입이 완료되었습니다.","href":"/"})
    # try:
    #     cursor = connection.cursor()
    #     strsql = "INSERT INTO member (userid,password) VALUES (%s ,%s)"
    #     result = cursor.execute(strsql,[idid,pwd])
    #     connection.commit()
    #     connection.close()
    # except Exception as e:
    #     print(e)
    #     connection.rollback()
    # return render(request, "result.html",{"alert_string":"회원가입이 완료되었습니다.","href":"/"})
def login_result(request):
    idid = request.POST["id"]
    pwd = request.POST["pwd"]
    mem = Member.objects.filter(memid = idid)
    if not mem.exists():
        return render(request, "result.html",{"alert_string":"회원의 가입되지 않았습니다","href":"/"})
    elif mem[0].pwd !=pwd:
        return render(request, "result.html",{"alert_string":"비밀버호가 틀렸습니다.","href":"/"})
    else:
        request.session['login_id'] = idid
        return render(request, "result.html",{"alert_string":"로그인이 완료되었습니다.","href":"/"})