from django.shortcuts import render


def the_view(request):
    return render(request, 'homepage.html',)
