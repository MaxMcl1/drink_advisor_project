from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from drinkadvisor.forms import UserForm, UserProfileForm, DrinkForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from drinkadvisor.models import DrinkProfile


# Create your views here.

def index(request):
    

    response = render(request, 'drinkadvisor/index.html')

    
    return response

def about(request):
    

    response = render(request, 'drinkadvisor/about.html')

    
    return response

def show_drink(request, drink_name_slug):

    context_dict = {}

    try:
        drink = DrinkProfile.objects.get(slug=drink_name_slug)
        context_dict['drink'] = drink

    except DrinkProfile.DoesNotExist:
        context_dict['drink'] = None

    return render(request, 'drinkadvisor/drink.html', context_dict)
        

def drinks(request):

    drink_list = DrinkProfile.objects.order_by('name')
    context_dict = {'drinks': drink_list}
    

    response = render(request, 'drinkadvisor/drinks.html', context_dict)

    
    return response

def energy_drinks(request):
    drink_list = DrinkProfile.objects.order_by('name')
    context_dict = {'drinks': drink_list}

    response = render(request, 'drinkadvisor/energy_drinks.html', context_dict)

    return response

def sugar_free(request):

    drink_list = DrinkProfile.objects.order_by('name')
    context_dict = {'drinks': drink_list}


    response = render(request, 'drinkadvisor/sugar_free.html', context_dict)

    return response

def profile(request):
    

    response = render(request, 'drinkadvisor/profile.html')

    
    return response

def register(request):
    registered = False


    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)


            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True


        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


    return render(request,
                  'drinkadvisor/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)


        if user:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Your Drink Advisor account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'drinkadvisor/login.html', {})

        
            
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
                
                
            
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def add_drink(request):

    form = DrinkForm()

    if request.method == 'POST':
        form = DrinkForm(request.POST)


        if form.is_valid():
            form.save(commit=True)

            return index(request)

        else:
            print(form.errors)
    return render(request, 'drinkadvisor/add_drink.html', {'form': form})
        
def edit_profile(request):

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/drinkadvisor/login')
        else:
            return HttpResponseRedirect('/drinkadvisor/edit_profile')
        
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request, 'drinkadvisor/edit_profile.html',args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('/drinkadvisor/profile')
        else:
            return HttpResponseRedirect('/drinkadvisor/change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request, 'drinkadvisor/change_password.html',args)
        
