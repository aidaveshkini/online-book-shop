from urllib import response
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import UserRegistrationForm


class RegisterUser(View):
    form_class = UserRegistrationForm
    template_name = 'books/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            

        return render(request, self.template_name, {'form':form})


