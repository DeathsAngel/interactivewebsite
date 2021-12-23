from django.shortcuts import render
from django.views.generic.base import View
from lists.models import user, recipe, List

userName = user('', 'Placeholder', 'passPlace')

class HomePage(View):
    def get(self, request):
        return render(request, 'index.html')

class LoginPage(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        global userName 
        userName = user('', request.POST.get('user'), request.POST.get('pass'))
        userName.save

        return render(request, 'loginAccepted.html', {"userName" : userName})

class recipeHome(View):
    def get(self, request):
        #list_ = List.objects.get(id=list_id)
        return render(request, 'recipeHome.html', {"userName" : userName})

    def post(self, request):
        list_ = List.objects.create()
        recipe.objects.create(text=request.POST['item_text'], list=list_)
        return render(request)