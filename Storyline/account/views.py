from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.core.exceptions import SuspiciousOperation
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.tokens import default_token_generator
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from django.template import loader
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import SignupForm, LoginForm
from .models import CustomUser

# Create your views here.
@require_http_methods(['GET', 'POST'])
def base(request):
	if request.user.is_authenticated():
		return redirect('home')
	if request.method == 'GET':
		f = LoginForm();
	else:
		f = LoginForm(request.POST)
		if f.is_valid():
			user = f.get_user();
			auth_login(request, user)
			return redirect('home')
	return render(request, 'authentication/login.html', {'form' : f})	

@require_http_methods(['GET', 'POST'])
def signup(request):
	if request.user.is_authenticated():
		return redirect('home')
	if request.method == 'GET':
		f = SignupForm();
	else:
		f = SignupForm(request.POST)
		if f.is_valid():
			user = f.save();
			email_body_context = {
				'username' : user.username,
				'token' : urlsafe_base64_encode(force_bytes(user.username)),
				'uid' : user.id,
				'protocol' : 'https' if settings.USE_HTTPS else 'http',
				'domain' : get_current_site(request).domain
			}
			body = loader.render_to_string('authentication/signup_email_body_text.html', email_body_context)
			email_message = EmailMultiAlternatives('Welcome To Story',body, settings.DEFAULT_FROM_EMAIL, [user.email])
			email_message.send()
			return render(request, 'authentication/signup_email_sent.html', { 'email' : user.email })
	return render(request, 'authentication/signup.html', {'form' : f}) 

@require_GET
def home(request):
	return render(request, 'authentication/home.html')

@require_GET
def logout(request):
	auth_logout(request)
	return redirect('base');

@require_GET
def activate(request, uid = None, token = None):
    if request.user.is_authenticated():
        return redirect('home')
    '''
    try:
        user = CustomUser.objects.get(id = uid)
    except CustomUser.DoesNotExist:
        raise Http404('Invalid User')
    '''
    user = get_object_or_404(CustomUser, id = uid)
    username_from_token = force_text(urlsafe_base64_decode(token))
    if user.is_active:
        return redirect('base')

    if user.username == username_from_token:
        user.is_active = True
        user.save()
        return render(request, 'authentication/activation_success.html')
    else:
        return render(request, 'authentication/activation_failure.html')
