from django.db.models import F
from django.shortcuts import render, HttpResponse
from app01.models import TelCode
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
        print(date)
        tctime = TelCode.objects.filter(cTime__lt=date)
        print(tctime)
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
