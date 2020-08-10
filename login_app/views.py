from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['ID']
        password = request.POST['PW']
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        # 로그인 성공시
        if user is not None:
            auth.login(request, user)
            return redirect('home')
            # return render(request, 'home.html')
        # 로그인 실패시
        else:
            context = {'error':'존재하지 않는 회원입니다.'}
            return render(request, 'login.html', context)
    elif request.method == 'GET':
        return render(request, 'login.html')

# 로그인이 되어 있을 때만 실행
@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')