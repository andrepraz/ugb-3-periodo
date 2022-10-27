from multiprocessing import context
from django.shortcuts import render, HttpResponse

def index(request):

    template_name = 'index.html'
    context = {
        'nome' : 'UGB'
    }
    return render(request, template_name, context)

def nome(request):
    name = 'André Ricardo Prazeres Rodrigues'
    html = f'''
    <html>
    <head>
    <title>Aula 3</title>
    </head>
    <body>
    <h1>{name}</h1>
    </body>
    </html>
    '''
    return HttpResponse(html)