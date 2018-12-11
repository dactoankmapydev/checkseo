from django.shortcuts import render, redirect
from .parser import parsing, reCaptcha

def index(request):
    return render(request, 'checkweb/index.html')

def about(request):
    return render(request, 'checkweb/about.html')

def contact(request):
    return render(request, 'checkweb/contact.html')

def check(request):
    if request.method == 'POST':
        domain = request.POST['domain']
        # reCaptcha
        if reCaptcha(request):
            # Parsing
            if(parsing(domain)):
                context = parsing(domain)
                context['domain'] = domain
            else:
                return render(request, 'checkweb/index.html', {'errURL': True, 'domain': domain})
            return render(request, 'checkweb/check.html', context)
        else:
            return render(request, 'checkweb/index.html', {'errCC': True, 'domain': domain})
    return redirect('index')
