from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        ID = request.POST['ID']
        PW1 = request.POST['PW1']
        PW2 = request.POST['PW2']
        if PW1 == PW2:
            user = User.objects.create_user(username=ID, password=PW1)
            # home.html을 띄워라!! - 127.0.0.1:8000/signup/
            # return render(request, 'home.html')
            #127.0.0.1:8000/
            # path 이름이 home url을 실행시켜라!!!
            return redirect('home')
        else:
            context = {'error':'password와 password확인이 일치하지 않습니다.'}
            return render(request, 'signup.html', context)
    elif request.method == 'GET':
        return render(request, 'signup.html')