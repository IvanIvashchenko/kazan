from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import password_reset
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from kazan.forms import CreateAdForm, RegistrationForm, LoginForm

from kazan.models import Ad, Owner, Sale
from mysite import settings


def index(request):

    latest_ad_list = Ad.objects.order_by('price')[:15]
    form = CreateAdForm()
    # else:
    #     return render_to_response('registration/register.html', {'form': form}, context_instance=RequestContext(request))
    context = {'latest_ad_list': latest_ad_list, 'form': form}

    # if form.is_valid():
    #     return HttpResponseRedirect('kazan/index.html')
    return render(request, 'kazan/index.html', context)

def create_ad(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/kazan/registration/register/')
    if request.method == 'POST':
        form = CreateAdForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Ad.objects.create(title=form.cleaned_data['title'],
                                              text=form.cleaned_data['text'],
                                              price=form.cleaned_data['price'],
                                              owner=Owner.objects.get(user_id=request.session._session.get('_auth_user_id')),
                                              image=request.FILES['image']
            )
            advertisement.save()
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

    else:
        form = CreateAdForm()
        context = {'form': form}
        return render(request, 'kazan/index.html', context)

def user_detail(request, user_id):

    user = get_object_or_404(Owner, id=user_id)
    latest_ad_list = Ad.objects.filter(owner_id=user_id)
    return render(request, 'kazan/user_detail.html', {'owner': user, 'latest_ad_list': latest_ad_list})

def ad_detail(request, ad_id):

    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'kazan/ad_detail.html', {'ad': ad})

def sale_detail(request, sale_id):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/kazan/registration/register/')
    sale = get_object_or_404(Sale, id=sale_id)
    return render(request, 'kazan/sale_detail.html', {'sale': sale})

def buy_ad(request, ad_id):

    if not request.user.is_authenticated():
        return HttpResponseRedirect('/kazan/registration/register/')
    if request.method == 'POST':
        advertisement = Ad.objects.get(id=ad_id)
        owner = Owner.objects.get(user_id=request.user.id)
        sale = Sale(ad=advertisement, buyer=owner)
        sale.save()
        return render(request, 'kazan/sale_detail.html', {'sale': sale})
    else:
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)


def owner_registration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['passwd'],
            )
            user.save()
            if 'image' in request.FILES:
                owner = Owner(user=user, image=request.FILES['image'])
            else:
                owner = Owner(user=user)
            owner.save()
            send_mail('Hello!', 'You are welcome on kazan size!', settings.DEFAULT_FROM_EMAIL, [form.cleaned_data['email']])
            return HttpResponseRedirect('/kazan/registration/login')
        else:
            return render_to_response('registration/register.html', {'form': form}, context_instance=RequestContext(request))
    else:
        '''user is not submitting the form, show them a blank registration form'''
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('registration/register.html', context, context_instance=RequestContext(request))

def login_request(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            owner = authenticate(username=username, password=password)
            if owner is not None:
                login(request, owner)
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
            else:
                return render_to_response('registration/login.html', {'form': form}, context_instance=RequestContext(request))
        else:
            return render_to_response('registration/login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        ''' user is not submitting the form, show the login form '''
        form = LoginForm()
        context = {'form': form}
        return render_to_response('registration/login.html', context, context_instance=RequestContext(request))

def logout_request(request):
        logout(request)
        return HttpResponseRedirect('/kazan/registration/login')

def password_reset_custom(request):
    return password_reset(request, template_name='registration/pass_reset.html',
                          subject_template_name = 'registration/password_reset_subj.txt',
                          post_reset_redirect = '/kazan/registration/user/password/reset/done/',
                          email_template_name = 'registration/pass_reset_email.html'
     )
