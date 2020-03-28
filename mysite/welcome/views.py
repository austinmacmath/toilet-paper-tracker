from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Q
from .models import Donor, Recipient

class IndexView(generic.TemplateView): 
    template_name = 'welcome/index.html'
    
class DetailView(generic.DetailView):
    model = Donor
    template_name = 'welcome/detail.html'

class NameView(generic.DetailView):
    template_name = 'welcome/results.html'
    context_object_name = 'latest_donor_list'

    def get_queryset(self):
        return Donor.objects.order_by('-join_date')[:5]

def points(request, donor_id):
    donor = get_object_or_404(Donor, pk=donor_id)
    try:
        selected_recipient = donor.recipient_set.get(pk=request.POST['recipient'])
    except (KeyError, Recipient.DoesNotExist):
        return render(request, 'welcome/detail.html', {
            'donor': donor,
            'error_message': "No recipient selected.",
        })
    else:
        selected_recipient.request -= 1
        selected_recipient.save()
        return HttpResponseRedirect(reverse('welcome:name', args=(donor.id,)))

class SearchResultView(generic.ListView):
    model = Donor
    template_name = 'welcome/searchresult.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Donor.objects.filter(
            Q(name__icontains=query) | Q(points__icontains=query)
        )
        return object_list