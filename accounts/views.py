from django.shortcuts import render, redirect
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import userform
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
# Create your views here.
def registration(request):

	if request.method == 'POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']
		email=request.POST['email']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'username taken')
				return redirect('accounts:registration' )
			elif User.objects.filter(email=email).exists():
				messages.info(request,'email taken')
				return redirect('accounts:registration')
			else:
				user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
				user.save();
				return redirect('accounts:login')
				
		else:
			print('password not matching')
			return redirect('accounts:registration')	

		return redirect('../')
	else:

		return render(request, 'accounts/registration.html')
	#if request.method == 'POST':
		#form = UserCreationForm(request.POST)
		#if form.is_valid():
			#form.save()
		#return redirect('posts:list')
	#else:        
		#form = UserCreationForm()
#def registration(request):
	#if r) 
	#else:
		#form1=userform(request.post)
		#return render(request, 'accounts/singup.html',{'form1': form1})
def login(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('../')
		else:
			messages.info(request,'invalid credentials')
			return redirect('accounts:login')

	else:
		return render(request, 'accounts/login.html')
def logout(request):
	auth.logout(request)
	return redirect('../')

def password_reset(request):
	if request.method=='POST':
		email=request.POST['email']
		if User.objects.filter(email=email).exists():
			current_site = get_current_site(request)
			#message box 
			user=User.objects.filter(email=email).get()
			message = render_to_string('accounts/acc_password_reset_cnfrm.html', {
				'user':user, 
				'domain':current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})
			mail_subject = 'for password reset.'
			email = EmailMessage(mail_subject, message, to=[email])
			email.send()
			messages.info(request,'chack ur emailid')
			return HttpResponse('Please confirm your email address to complete the registration')
		else:
			messages.info(request,'email does not exists')
			return render(request,'accounts/password_reset.html')	
			
	else:
		return render(request,'accounts/password_reset.html')







def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):


        login(request, user)
        # return redirect('home')
        return redirect('../changepassword.html')
    else:
        return HttpResponse('Activation link is invalid!')