from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from webapp.forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout

def index(request):
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
			user.set_password(user.password)
			user.save()

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
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
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
	logout(request)
	return HttpResponseRedirect('/home/')