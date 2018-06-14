from django.db.models import F, Q
from django.shortcuts import render, HttpResponse, redirect
from django.utils.decorators import method_decorator
from django import views
from app01.models import TelCode, UserInfo
from app01.toolClass.getcode import generate_verification_code
from django.utils.timezone import now, timedelta
from io import BytesIO
from app01.toolClass.getpilcode import create_validate_code
from app01.toolClass.modeltool import ModelSelect
# import datetime, time

def outer(func):
    def inner(request, *args, **kwargs):
        sess = request.session.get('username', None)
        if sess:
            return func(request, *args, **kwargs)
        else:
            return redirect('/test')
    return inner

# Create your views here.
def test(request):
    if request.method == 'GET':
        return render(request, 'base.html')
    else:
        return HttpResponse('ok!')

def getcode(request):#获取手机号验证码
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

def next_page(request):#在进入注册页面的下一页前，对第一页进行校验
    if request.method == 'POST':
        data =request.POST
        very = TelCode.objects.filter(telephone=data.get('rgmobile'), code=data.get('rgcode'))
        if very.exists():
            return HttpResponse('true')
        else:
            return HttpResponse('false')

def accomplish(request):#注册完成并登陆
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

def logout(request):#登出系统
    request.session.clear()
    return redirect('/test/')

def login(request):#登录系统
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        keeplogin = request.POST.get('keeplogin')
        pilcode = request.POST.get('pilcode')
        verpilcode = request.session.get('CheckCode')
        user = UserInfo.objects.filter((Q(telephone=username)|Q(username=username))&Q(pwd=pwd)).first()
        if pilcode.upper() != verpilcode.upper():
            return HttpResponse('验证码不正确')
        elif not user:
            return HttpResponse('手机号或密码不正确')
        else:
            request.session['username'] = user.username
            if keeplogin == '1':
                # request.session.set_expiry(0)
                request.session.set_expiry(timedelta(days=30))
            else:
                request.session.set_expiry(0)
            return HttpResponse('')

def check_code(request):#生成图片验证码
    stream = BytesIO()  # 开辟一块内存空间，不用写在外存，减少读写操作
    img, code = create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())

# @method_decorator(outer, name='dispatch')
class AllHot(views.View):
    def dispatch(self, request, *args, **kwargs):
        ret = super(AllHot, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):
        datalist = list(ModelSelect.hot_select(1))
        return render(request, 'index.html', {'datalist': datalist})
