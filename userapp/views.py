from django.shortcuts import render

# Create your views here.
def getUser(request):
    datas = []
    msg = 'hello1'
    print(msg)
    return render(request, 'user/index.html', locals())