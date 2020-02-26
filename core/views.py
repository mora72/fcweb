from django.shortcuts import render


def main_dash(request):
    return render(request, 'core/maindash.html')
