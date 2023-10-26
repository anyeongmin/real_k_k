from django.shortcuts import render

from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'index.html')
def register(request):
    return render(request, "register.html")
def register_result(request):
    print(request.POST)
    idid = request.POST["id"]
    pwd = request.POST["pwd"]
    if len(idid) < 5:
        return render(request,"result.html",{"alert_string":"아이디가 5글자보다 작습니다","href":"/register"})
    if len(pwd) < 8:
        return render(request,"result.html",{"alert_string":"비밀번호가 8글자보다 작습니다","href":"/register"})
    
    try:
        cursor = connection.cursor()
        strsql = "INSERT INTO member (userid,password) VALUES (%s ,%s)"
        result = cursor.execute(strsql,[idid,pwd])
        connection.commit()
        connection.close()
    except Exception as e:
        print(e)
        connection.rollback()
    return render(request, "result.html",{"alert_string":"회언가입이 완료되었습니다.","href":"/"})
    