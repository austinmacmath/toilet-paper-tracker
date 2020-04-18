# from django.contrib.gis.geos import *
# from django.contrib.gis.measure import D
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Q
from geopy.distance import geodesic
from uszipcode import SearchEngine
from .models import Donor, Recipient

search = SearchEngine(simple_zipcode=True)

class IndexView(generic.TemplateView): 
    template_name = 'notp/index.html'

class SearchResultView(generic.ListView):
    model = Donor
    template_name = 'notp/searchresult.html'

    def get_queryset(self):
        query = self.request.GET.get('q')

        recipient = Recipient()
        recipient.zipcode = query
        bound_north = search.by_zipcode(recipient.zipcode).to_dict()["bounds_north"] 
        if bound_north == None:
            return None
        bound_south = search.by_zipcode(recipient.zipcode).to_dict()["bounds_south"] 
        bound_west = search.by_zipcode(recipient.zipcode).to_dict()["bounds_west"]
        bound_east = search.by_zipcode(recipient.zipcode).to_dict()["bounds_east"]
         
        recipient.latitude = (bound_north + bound_south)/2
        recipient.longitude = (bound_west + bound_east)/2
        recipient.save()

        object_list = Donor.objects.filter(
            Q(zipcode__icontains=query)
        )
        return object_list

class AboutView(generic.TemplateView):
    template_name = 'notp/about.html'

class MoreItemsView(generic.TemplateView):
    template_name = 'notp/moreitems.html'

def form(request):
    if request.method == 'POST':
        donor = Donor()
        donor.name = request.POST.get('name')
        donor.email = request.POST.get('email')
        donor.zipcode = request.POST.get('zipcode')
        bound_north = search.by_zipcode(donor.zipcode).to_dict()["bounds_north"] 
        bound_south = search.by_zipcode(donor.zipcode).to_dict()["bounds_south"] 
        bound_west = search.by_zipcode(donor.zipcode).to_dict()["bounds_west"]
        bound_east = search.by_zipcode(donor.zipcode).to_dict()["bounds_east"]
        donor.latitude = (bound_north + bound_south)/2
        donor.longitude = (bound_west + bound_east)/2
        donor.save()
        return render(request, 'notp/form.html')
    else:
        return render(request, 'notp/form.html')



 
