from django.shortcuts import render
from django.http import request
from .models import Profile
# Create your views here.


def profile_index(request):
    context= {}
    uid = request.user.id
    context['prof'] = Profile.objects.get(user=uid)
    return render(request, "profile.html", context)

