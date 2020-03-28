from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
# from django.template import loader
from django.db.models import Q
from .models import Donor, Recipient

# Create your views here.
class IndexView(generic.TemplateView): 
    template_name = 'welcome/index.html'
    

class DetailView(generic.DetailView):
    model = Donor
    template_name = 'welcome/detail.html'

# def detail(request, donor_id):
#     # try:
#     #     donor = Donor.objects.get(pk=donor_id)
#     # except Donor.DoesNotExist:
#     #     raise Http404("Donor does not exist")
#     donor = get_object_or_404(Donor, pk=donor_id)
#     return render(request, 'welcome/detail.html', {'donor': donor})

class NameView(generic.DetailView):
    # model = Donor
    template_name = 'welcome/results.html'
    context_object_name = 'latest_donor_list'

    def get_queryset(self):
        return Donor.objects.order_by('-join_date')[:5]

# def name(request, donor_id):
#     name = "You're looking at the name of donor %s."
#     # return HttpResponse(name  % donor_id)
#     donor = get_object_or_404(Donor, pk=donor_id)
#     return render(request, 'welcome/results.html', {'donor': donor})

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

# def search(request):
#     return render(request, 'welcome/search.html')

class SearchResultView(generic.ListView):
    model = Donor
    template_name = 'welcome/searchresult.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Donor.objects.filter(
            Q(name__icontains=query) | Q(points__icontains=query)
        )
        return object_list

    # queryset = Donor.objects.filter(name__icontains='Austin')
    # context_object_name = 'latest_donor_list'

    # def get_queryset(self):
    #     return Donor.objects.order_by('-join_date')[:5]

# def searchresult(request, donor_id):
#     donor = get_object_or_404(Donor, pk=donor_id)
#     return render(request, 'welcome/searchresult.html', {'donor': donor,})

# def recipients(request, donor_id):
#     donor = get_object_or_404(Donor, pk=donor_id)
#     try:
#         selected_recipient = donor.recipient_set.get(pk=request.POST['recipient'])
#     except (KeyError, Recipient.DoesNotExist):
#         return render(request, 'welcome/detail.html', {
#             'donor': donor,
#             'error_message': "No recipient selected.",
#         })
#     else:
#         selected_recipient.request -= 1
#         selected_recipient.save()
#         return HttpResponseRedirect(reverse('welcome:results', args=(donor.id,)))

# def results(request, donor_id):
#     donor = get_object_or_404(Donor, pk=donor_id)
#     return render(request, 'welcome/results.html', {'donor': donor})