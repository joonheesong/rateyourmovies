from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from webapp.forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
import tmdbsimple as tmdb
from webapp.models import Movie

# Set up API key for tmdb
tmdb.API_KEY = settings.MY_API_KEY

def index(request):
	""" Main page """
	if request.user.is_authenticated():
		return render(request, 'pages/home.html', {})
	else:
		return render(request, 'pages/index.html', {})
	
def signup(request):
	""" Registration of a user """

	if request.method == "POST":
		userform = RegistrationForm(request.POST)
		if userform.is_valid():
			user = userform.save()
			return HttpResponseRedirect(
				reverse('signup_ok')
			)

	elif request.method == "GET":
		userform = RegistrationForm()

	return render(request,
				  'registration/signup.html',
				  {"userform": userform}
				  )

def login_view(request):
	""" Login """
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/home/')
			else:
				return HttpResponse("Inactive user")
		else:
			return HttpResponseRedirect('/login/')
			
	return render(request, "registration/login.html", {'redirect_to': '/home/'})


def logout_view(request):
	""" Logout """
	logout(request)
	return HttpResponseRedirect('/home/')


def search_movie(request):
	# Get query value
	query = request.GET['query']
	if query != "":
		search_result = {}
		i = 0
		# Search movie with given query
		search = tmdb.Search()
		response = search.movie(query=query)
		# For each result, find the movies that are already released
		for result in response['results']:
			m_id = result['id']
			title = result['original_title']
			poster_path = result['poster_path']
			release_date = result['release_date']
			if release_date != "" and release_date <= settings.TODAY:
				# add to movies if it is a new moive
				found = Movie.objects.all().filter(m_id=result['id'])
				if found is None:
					found = Model(m_id=m_id,
								  title=title,
								  poster_path=poster_path,
								  release_date=release_date)
					found.save()
				search_result[i] = {"id": m_id,
									"title": title,
									"poster_path": settings.IMG_SRC + poster_path,
									"release_date": release_date}
				print(title)
				i += 1
		return render(request, 'pages/search.html', {'search_result': search_result})

	return render(request, 'pages/search.html', {'search_result': {}})





































