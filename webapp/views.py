from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from webapp.forms import RegistrationForm

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
