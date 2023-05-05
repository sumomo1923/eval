from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from common.forms import UserForm
from eval.models import Score

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def my_logout(request):
    # Django의 로그아웃 함수를 호출하여 로그아웃을 처리합니다.
    auth_logout(request)

    # 로그아웃 후에는 home 페이지로 리디렉션합니다.
    return redirect('home')