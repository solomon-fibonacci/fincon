import json

import requests
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

from userplus.forms import SignUpForm, SignInForm


signup_subject = 'Welcome to fincon'
signup_message = ('follow link to activate account'
                  '{}')


class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'finconuser/signup.html', locals())

    #  TODO include captcha functionality
    def post(self, request):
        form = SignUpForm(request.POST)
        captcha_data = {
            'secret': '6Lfe8SETAAAAAPeAKS3zW09cgMTGlCKmuppoyPKk',
            'response': form.data['g-recaptcha-response'],

        }
        verification = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data=captcha_data
        )

        if json.loads(verification.content)['success']:
            if form.is_valid():
                user = form.save()
                location = reverse('userplus_confirm_registration', kwargs={
                                   'activation_key': user.activation_key})
                message = signup_message.format(
                    request.build_absolute_uri(location))
                user.email_user(signup_subject, message)
                return HttpResponseRedirect(reverse('signin'))

        return render(request, 'finconuser/signup.html', locals())


class SignInView(View):

    def get(self, request):
        form = SignInForm()
        return render(request, 'finconuser/signin.html', locals())

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

        form.add_error("username_or_email", "Invalid login details!")
        return render(request, 'finconuser/signin.html', locals())


class UserHomeView(View):

    def get(self, request):
        return render(request, 'finconuser/home.html', locals())


class SignOutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('signin'))
