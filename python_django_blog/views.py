from django.shortcuts import render


def home(request):
    return render(request, 'python_django_blog/home.html', {'user': request.user})
