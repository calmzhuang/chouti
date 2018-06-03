from django.db.models import F, Q
from django.shortcuts import render, HttpResponse, redirect
from app01.models import TelCode, UserInfo
from app01.toolClass.getcode import generate_verification_code
from django.utils.timezone import now, timedelta
# import datetime, time

# Create your views here.
def test(request):
    if request.method == 'GET':
        return render(request, 'base.html')
    else:
        return HttpResponse('ok!')

def getcode(request):
    if request.method == 'POST':
        telnum = request.POST.get('telephonenum')
        code = generate_verification_code()
        tel = TelCode.objects.filter(telephone=telnum).first()
        # now = datetime.datetime.now()
        date = now() + timedelta(days=-1)#昨天的此时
        # date = now() #今天
        tctime = TelCode.objects.filter(cTime__lt=date)
        userIn = UserInfo.objects.filter(telephone=telnum)
        if userIn.exists():
            return HttpResponse('该手机号已被注册')
        else:
            if tel:
                if tel.times >= 6:
                    if tctime.exists():
                        TelCode.objects.filter(telephone=telnum).update(times=0, code=code)
                        print(code)
                    else:
                        return HttpResponse('注册次数超过最大限制，请明天再试')
                else:
                    TelCode.objects.filter(telephone=telnum).update(times=F('times') + 1, code=code)
                    print(code)
            else:
                TelCode.objects.create(
                    telephone=telnum,
                    code=code,
                    times=0,
                )
                print(code)
            return HttpResponse('')

def next_page(request):
    if request.method == 'POST':
        data =request.POST
        very = TelCode.objects.filter(telephone=data.get('rgmobile'), code=data.get('rgcode'))
        if very.exists():
            return HttpResponse('true')
        else:
            return HttpResponse('false')

def accomplish(request):
    if request.method == 'POST':
        data = request.POST
        UserInfo.objects.create(
            username=data.get('nick'),
            telephone=data.get('user_info[rgmobile]'),
            pwd=data.get('user_info[rgpwd]'),
            sex=data.get('sex'),
            sign=data.get('sign'),
        )
        request.session['username'] = data.get('nick')
        request.session.set_expiry(0)
        return HttpResponse('""')

def logout(request):
    request.session.clear()
    return redirect('/test/')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        keeplogin = request.POST.get('keeplogin')
        user = UserInfo.objects.filter((Q(telephone=username)|Q(username=username))&Q(pwd=pwd)).first()
        if not user:
            return HttpResponse('手机号或密码不正确')
        else:
            request.session['username'] = user.username
            if keeplogin == '1':
                # request.session.set_expiry(0)
                request.session.set_expiry(timedelta(days=30))
            else:
                request.session.set_expiry(0)
            return HttpResponse('')