from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
# from user.models import User
from .forms import RegisterForm, LoginForm

class RegisterFormView(View):
    form_class = RegisterForm
    template = 'user/form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                    return redirect('home:index')

        return render(request, self.template, {'form':form})

class LoginFormView(View):
    form_class = LoginForm
    template = 'user/form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print(request.session.get('cart'))
                    cart = ()
                    request.session['cart'] = cart
                    print(request.session.get('cart'))
                    return redirect('home:index')
            else:
                redirect(self.template)

        return render(request, self.template, {'form':form})

class LogoutView(View):
    def get(self, request):

        print(request.session.get('cart'))
        print(request.session['cart'])
        if request.session['cart'] :
            print ('if')
        else:
           print('else')


        request.session['cart'] = ()
        request.session.modified = True
        
        logout(request)
        return redirect('home:index')
