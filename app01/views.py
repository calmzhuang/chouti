from django.shortcuts import render, HttpResponse
from app01.models import TelCode
import datetime

# Create your views here.
def test(request):
    if request.method == 'GET':
        return render(request, 'base.html')
    else:
        return HttpResponse('ok!')

def getcode(request):
    if request.method == 'POST':
        today = datetime.date.today()
        telnum = request.POST.get('telephonenum')
        tel = TelCode.objects.filter(telephone=telnum).first()
        if tel:
            if tel.times >= 6:
                if tel.cTime < today:
                    TelCode.objects.filter(telephone=telnum).update(times=0)


