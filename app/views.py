from django.shortcuts import render

def app(request):
    # This is a simple view that renders a template
    return render(request, 'index.html')

# Create your views here.
