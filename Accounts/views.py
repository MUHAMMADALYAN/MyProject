from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

# when we click register button it always call get data method as we are  reuesting for Registeration page
# when user click on submit button it will be Posting that data
def register(request):
    # it happens only when we click submit button therefore always first else condition will be executed
    if request.method == 'POST':
        # fetching data from html form
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        username = request.POST['user']
        pn = request.POST['phone']
        em = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if (pass1 == pass2):
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('registeration')
                # events=Events.objects.all()
            elif User.objects.filter(email=em).exists():
                messages.info(request, 'Email already present')
                return redirect('registeration')
            else:
                user = User.objects.create_user(first_name=fn, username=username, password=pass1, last_name=ln,email=em)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password mismatch')
            return redirect('registeration')
        return redirect('/')

    else:

        return render(request, "registeration.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        passw = request.POST['password']
        user = auth.authenticate(username=username, password=passw)
        if user is not None:
            auth.login(request, user)
            # The redirect_to method tells your browser to send a request to another URL.
            # so no mistake in rediect as it contain parametre path
            return redirect('')
        else:
            messages.info(request, 'ivalid username or password')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('')
