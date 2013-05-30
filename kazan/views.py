from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from kazan.models import Ad, User


def index(request):

    latest_ad_list = Ad.objects.order_by('price')[:5]
    context = {'latest_ad_list': latest_ad_list}
    return render(request, 'kazan/index.html', context)

def user_detail(request, user_id):

    user = get_object_or_404(User, id=user_id)
    return render(request, 'kazan/user_detail.html', {'user': user})

def ad_detail(request, ad_id):

    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'kazan/ad_detail.html', {'ad': ad})

def login(request):

    