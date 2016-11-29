from django import forms            
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from webapp.models import Posting

class RegistrationForm(UserCreationForm):
	username = forms.CharField(
							max_length=50,
							widget=forms.TextInput(attrs={'class': "input__field input__field--chisato"}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "input__field input__field--chisato"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "input__field input__field--chisato"}))
	email = forms.EmailField(required=True,
							widget=forms.TextInput(attrs={'class': "input__field input__field--chisato"}))

	class Meta:
		model = User
		fields = {'username', 'email', 'password1', 'password2'}

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class ReviewForm(forms.Form):
	review = forms.CharField(widget=forms.Textarea(attrs={'class': 'input__field'}))
	m_id = forms.IntegerField(widget=forms.HiddenInput())