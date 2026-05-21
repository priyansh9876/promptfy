from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = SignupForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()

            login(
                request,
                user,
                backend='django.contrib.auth.backends.ModelBackend'
            )

            return redirect('/')

    return render(request, 'accounts/signup.html', {
        'form': form
    })