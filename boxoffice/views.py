from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
from boxoffice.models import City, Theatre, Movie, Show
from boxoffice.serializers import CitySerilaizer, TheatreSerilaizer


def index(request):
    if request.method=="POST":
        print(request)
    else:
        try:
            city_data=CitySerilaizer(City.objects.filter(is_active=True),many=True)
            base=request.get_host()
            #movies=TheatreSerilaizer(Theatre.objects.filter(city__name="Pune"),many=True)
            shows =Show.objects.filter(theatre__city__name="Pune")
            movies_data=[]
            for show in shows:
                movies_data.append({
                    "id": show.id,
                    "name": show.name,
                    "url": "http://" + base + "/media/" + str(show.movie.url),
                    "theatre":show.theatre.name
                })
            context = {
                'mov': movies_data,
                'cities':city_data.data
            }
            return render(request,"index.html", context)
        except Exception as e:
            return render(request,"index.html", {"error":e})
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exist')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password1)
                user.save()
                messages.info(request, 'User created')
                return redirect('login')
        else:
            messages.info(request, 'Password not match')
        return redirect('register')
    else:
        return render(request, "register.html")


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Username/Password is incorrect')
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

