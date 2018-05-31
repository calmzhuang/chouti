from django.shortcuts import render, HttpResponse

# Create your views here.
def test(request):
    if request.method == 'GET':
        return render(request, 'base.html')
    else:
        return HttpResponse('ok!')
