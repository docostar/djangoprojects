from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    request.session.set_test_cookie()
    return HttpResponse('<h2>Jai Bharat</h2>')

def page2(request):
    if request.session.test_cookie_worked():
        print('Cookies are enabled')
    request.session.delete_test_cookie()
    return HttpResponse('<b>Page 2</b>')

def countview(request):
    if 'count' in request.COOKIES:
        count=int(request.COOKIES['count'])+1
    else:
        count = 1
    response = render(request, 'cookiesApp/count.html',{'count':count}) 
    response.set_cookie('count',count)
    return response

