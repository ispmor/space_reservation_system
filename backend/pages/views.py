from django.views.generic import TemplateView
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render


class HomePageView(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('reservations/list')
        else:
            return HttpResponseRedirect('about')


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'