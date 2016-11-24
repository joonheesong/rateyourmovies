from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm

def index(request):
	return render(request, 'pages/index.html', {})
	
def signup(request):
	""" Registration of a user """

	if request.method == "POST":
		userform = UserCreationForm(request.POST)
		if userform.is_valid():
			userform.save()

			return HttpResponseRedirect(
				reverse('signup_ok')
			)
	elif request.method == "GET":
		userform = UserCreationForm()

	return render(request,
				  'registration/signup.html',
				  {"userform": userform}
	)