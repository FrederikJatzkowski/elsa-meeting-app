from django.http import HttpResponse

from django.conf import settings

# Create your views here.
def index(request):

    path = request.path.split('/')

    #Leere Elemente entfernen
    while "" in path:
        path.remove("")

    #Letztes Element
    if len(path) > 0:
        last = path[len(path)-1]
    else:
        last = "false"

    try:

        f = open(str(settings.BASE_DIR / str("static/angular-present/" + last)))

        if last[-2:] == 'js':
            return HttpResponse(f,'text/javascript')

        elif last[-3:] == 'css':
            return HttpResponse(f,'text/css')

        elif last[-3:] == 'ico':
            return HttpResponse(f,'image/x-icon')

        else:
            return HttpResponse(f,'text/html')
    
    except:

        f = open(settings.BASE_DIR / "static/angular-present/index.html")

        return HttpResponse(f)



    