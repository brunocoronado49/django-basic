from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Index Page</h1>')

def hello_world(request, username):
    print(username)
    return HttpResponse('<h1>Hello, World! from Django</h1>')

def about(request):
    return HttpResponse('<h1>About this site</h1>')
