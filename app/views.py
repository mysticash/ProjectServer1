from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def _404(request):
    return render(request, '404.html')
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def FAQ(request):
    return render(request, 'FAQ.html')
def feature(request):
    return render(request, 'feature.html')
def offer(request):
    return render(request, 'offer.html')
def service(request):
    return render(request, 'service.html')
def team(request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')