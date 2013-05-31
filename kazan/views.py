from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from registration.models import RegistrationProfile
from kazan.forms import CreateAdForm

from kazan.models import Ad, UserProfile, Sale

# def

def index(request):

    latest_ad_list = Ad.objects.order_by('price')[:5]
    form = CreateAdForm()
    context = {'latest_ad_list': latest_ad_list, 'form' : form}

    # if form.is_valid():
    #     return HttpResponseRedirect('kazan/index.html')
    return render(request, 'kazan/index.html', context)

def user_detail(request, user_id):

    user = get_object_or_404(RegistrationProfile, id=user_id)
    latest_ad_list = Ad.objects.filter(owner_id=user_id)
    return render(request, 'kazan/user_detail.html', {'user': user,'latest_ad_list': latest_ad_list})

def ad_detail(request, ad_id):

    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'kazan/ad_detail.html', {'ad': ad})

def sale_detail(request, sale_id):

    sale = get_object_or_404(Sale, id=sale_id)
    return render(request, 'kazan/sale_detail.html', {'sale': sale})