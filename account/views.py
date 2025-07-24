from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.forms import CustomUserCreationForm, CustomUserChangeForm, ProfileChangeForm
from account.models import Profile


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'account/register.html', context=context)


def profile(request):
    return render(request, 'account/profile.html')


def change_profile(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if not hasattr(request.user, 'profile'):
            Profile.objects.create(user=request.user)

        profile_form = ProfileChangeForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            messages.warning(request, 'Account changed successfully')
            profile_form.save()
        return redirect('profile')

    else:
        user_form = CustomUserChangeForm(instance=request.user)
        if not hasattr(request.user, 'profile'):
            Profile.objects.create(user=request.user)
        profile_form = ProfileChangeForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'account/change_profile.html', context=context)


def test_send_mail(request):
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    email = request.POST.get('email')
    if request.method == 'POST':
        send_mail(
            subject,
            message,
            'soxadev@gmail.com',
            [email],
            fail_silently=True,
        )
        return render(request,'mail/send_mail_success.html')

    else:
        return render(request, 'mail/send_mail.html')
