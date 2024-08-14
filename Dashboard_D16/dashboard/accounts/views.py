import random

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

from .forms import SignUpForm


class OneTimeCode:
    pass


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

    # def usual_login_view(request):
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         OneTimeCode.objects.create(code=random.choice('absd'), user=user)
    #         # Send one-time code to email.
    #         # Redirect to a success page.
    #     else:
    #         pass
    #         # Return an 'invalid login' error message.
    #
    # def login_with_code_view(request):
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     code = request.POST['code']
    #     user = authenticate(request, username=username, password=password)
    #     if OneTimeCode.filter(code=code, user__username=username).exist():
    #         login(request, user)
    #     else:
    #         pass
    #         # errore