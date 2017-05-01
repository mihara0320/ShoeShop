from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ContactForm

def index(request):
    return render(request, 'home/index.html')

class HomeView(View):
    form_class = ContactForm
    template = 'home/index.html'

    def get(self, request):
        form = self.form_class(None)
        context = {'form':form}

        return render(request, self.template, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form = None
            print(email)
            print(message)

            subject='Contact Form'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, email]
            contact_message = "%s: %s via %s"%(name, message, email)

            send_mail(
                subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=True
            )
            # redirect to contact part


        return render(request, self.template, {'form': form})
