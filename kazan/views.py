from django.http import HttpResponse
from django.shortcuts import render

from kazan.models import Ad

def index(request):

    latest_ad_list = Ad.objects.order_by('price')[:5]
    context = {'latest_ad_list': latest_ad_list}
    return render(request, 'kazan/index.html', context)

def user_detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)

def ad_detail(request, ad_id):
    return HttpResponse("You're looking at ad %s." % ad_id)