from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from drinkadvisor.forms import UserForm, UserProfileForm

# Create your views here.

def index(request):
    

    response = render(request, 'drinkadvisor/index.html')

    
    return response

def about(request):
    

    response = render(request, 'drinkadvisor/about.html')

    
    return response

def drinks(request):
    

    response = render(request, 'drinkadvisor/drinks.html')

    
    return response

def sugar_free(request):
    

    response = render(request, 'drinkadvisor/sugar_free.html')

    
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

            
    
        
        
        
