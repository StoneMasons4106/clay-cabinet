from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, UserForm
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(User, username=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        form_two = UserForm(request.POST, instance=user)
        if form.is_valid() and form_two.is_valid():
            try:
                user_email = get_object_or_404(EmailAddress, user_id=request.user)
                if str(request.POST.get('email')) != str(user_email):
                    new_email = request.POST.get('email')
                    profile.add_email_address(request, new_email)
                else:
                    pass
                form.save()
                form_two.save()
            except EmailAddress.MultipleObjectsReturned:
                pass
        else:
            pass
    else:
        form = UserProfileForm(instance=profile)
        form_two = UserForm(instance=user)
    
    orders = profile.orders.all() 
    
    template = 'profiles/profile.html'
    context = {
        'page': 'profile',
        'profile': profile,
        'user': user,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def edit_profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(User, username=request.user)

    form = UserProfileForm(instance=profile)
    form_two = UserForm(instance=user)

    template = 'profiles/edit-profile.html'
    
    context = {
        'page': 'profile',
        'form': form,
        'form_two': form_two,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def delete_profile(request):
    '''Delete user profile'''
    if request.method == "POST":
    
        user = get_object_or_404(User, username=request.user)
        user.delete()

        return redirect(reverse('home'))
    
    template = "profiles/delete_profile.html"

    context= {
        'page':'profile',
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def order_history(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    
    orders = profile.orders.all() 
    
    template = 'profiles/order-history.html'
    context = {
        'page': 'profile',
        'profile': profile,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)