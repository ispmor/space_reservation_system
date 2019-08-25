from django.views.generic import TemplateView
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('reservations/list')
        else:
            return render(request, self.template_name)


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'