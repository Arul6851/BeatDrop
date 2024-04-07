from django.shortcuts import render, redirect
from beats.forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login
from beats.models import Song, WatchLater
from datetime import date

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print("Done")
            if user:
                login(request, user)
                return redirect('home') 
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home_view(request):
  songs = Song.objects.all()
  search_query = request.GET.get('query', '')
  if(request.user.is_anonymous == False):
    user = request.user
    watch_later_songs = WatchLater.objects.filter(user=user)
  else:
    watch_later_songs = []

  watch_later_list = []

  for watch_later in watch_later_songs:
      watch_later_list.append(watch_later.song)
  if search_query:
    songs = songs.filter(title__icontains=search_query)
  context = {'songs': songs, 'search_query': search_query, 'current_year': date.today().year, 'watch_later': watch_later_list}
  return render(request, 'home.html', context)