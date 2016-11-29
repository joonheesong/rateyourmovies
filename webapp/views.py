from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from webapp.forms import RegistrationForm, ReviewForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
import tmdbsimple as tmdb
from webapp.models import Movie, Posting, Users
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from ast import literal_eval

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
			Users(username=user.username, password=user.password, email=user.email).save()
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
			release_date = result['release_date']

			if result['poster_path']:
				poster_path = settings.IMG_SRC + result['poster_path']
			else:
				poster_path = "none"

			if release_date != "" and release_date <= settings.TODAY:
				# add to movies if it is a new moive
				found = Movie.objects.all().filter(m_id=result['id'])
				if not found:
					found = Movie(m_id=m_id,
								  title=title,
								  poster_path=poster_path,
								  release_date=release_date)
					found.save()

				search_result[i] = {"id": m_id,
									"title": title,
									"poster_path": poster_path,
									"release_date": release_date}
				i += 1

		return render(request, 'pages/search.html', {'search_result': search_result})

	return render(request, 'pages/search.html', {'search_result': {}})


def review_movie(request):
	if request.method =="POST":
		reviewform = ReviewForm(request.POST)
		new_post = None
		rating = request.POST.get('rating')
		if reviewform.is_valid():
			m_id = Movie.objects.get(m_id=reviewform.cleaned_data['m_id'])
			user = Users.objects.get(username=request.user.username)
			review = reviewform.cleaned_data['review']

			try:
				new_post = Posting.objects.get(m_id=m_id, username=user)
				new_post.new_review(new_review=review)
				new_post.update_rating(new_rating=rating)
				new_post.save()
			except ObjectDoesNotExist:
				new_post = Posting(m_id=m_id, username=user, review=review, rating=rating)
				new_post.save()

		listing_url = '/listing?m_id=' + str(new_post.m_id.m_id)
		
		return HttpResponseRedirect(listing_url)

		''' else:
			will implement error later
		'''

	elif request.method == "GET":
		movie = request.GET['movie']
		movie = literal_eval(movie)

		reviewform = ReviewForm(initial={'m_id': movie['id']})

		return render(request, 'pages/review.html', {'title': movie['title'],
												 'poster_path': movie['poster_path'],
												 'release_date': movie['release_date'],
												 'm_id': movie['id'],
												 'reviewform': reviewform })

def listing(request):
	m_id = int(request.GET['m_id'])
	movie = None
	user = Users.objects.get(username=request.user.username)

	if m_id > 0:
		# Find current movie
		movie = Movie.objects.get(m_id=m_id)
	else:
		try:
			movie = Posting.objects.filter(username=user)[0].m_id
		except:
			return HttpResponseRedirect('/search?query=')
		
	# Find all movies that user rated.
	current_review = Posting.objects.get(m_id=movie, username=user)
	movie_list = {}
	for review in Posting.objects.filter(username=user):
		movie_list[review.m_id.title] = review.m_id.m_id
		
	return render(request, 'pages/personal_list.html', {'movie': movie,
														'movie_list': sorted(movie_list.items()),
														'current_review': current_review})






























