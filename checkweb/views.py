from django.shortcuts import render, redirect
from .parser import parsing

def index(request):
    return render(request, 'checkweb/index.html')

def about(request):
    return render(request, 'checkweb/about.html')

def contact(request):
    return render(request, 'checkweb/contact.html')

def check(request):
    if request.method == 'POST':
        domain = request.POST['domain']
        if(parsing(domain)):
            context = parsing(domain)
            context['domain'] = domain
        else:
            context = {
                'error': True,
                'domain': domain
            }
            return render(request, 'checkweb/index.html', context)
        return render(request, 'checkweb/check.html', context)

    return redirect('index')
