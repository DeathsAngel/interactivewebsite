from django.shortcuts import render
from django.views.generic.base import View
from lists.models import Name

userName = Name('', 'Placeholder')

class HomePage(View):
    def get(self, request):
        return render(request, 'index.html')

class LoginPage(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        global userName 
        userName = Name('', request.POST.get('user'))
        userName.save

        return render(request, 'loginAccepted.html', {"userName" : userName})

class recipeHome(View):
    def get(self, request):
        return render(request, 'recipeHome.html', {"userName" : userName})