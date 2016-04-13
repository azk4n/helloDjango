from django.shortcuts import render, get_object_or_404
from helloDjango.subscriptions.forms import SubscriptionForm
from django.http import HttpResponseRedirect
from helloDjango.subscriptions.models import Subscription

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    return render(request, 'subscriptions/subscription_form.html',  {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',  {'form': form})

    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d/' % obj.pk)

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})
