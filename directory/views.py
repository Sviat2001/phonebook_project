from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Subscriber
from .forms import SubscriberForm
from django.db.models import CharField
from django.db.models.functions import Lower

CharField.register_lookup(Lower, 'lower')

@login_required
def subscriber_list(request):
    subscribers = Subscriber.objects.filter(user=request.user).order_by('last_name__lower')
    grouped_subscribers = {}
    for subscriber in subscribers:
        first_letter = subscriber.last_name[0].upper()
        if first_letter not in grouped_subscribers:
            grouped_subscribers[first_letter] = []
        grouped_subscribers[first_letter].append(subscriber)
    return render(request, 'subscriber_list.html', {'grouped_subscribers': grouped_subscribers})

@login_required
def subscriber_detail(request, pk):
    subscriber = get_object_or_404(Subscriber, pk=pk, user=request.user)
    return render(request, 'subscriber_detail.html', {'subscriber': subscriber})

@login_required
def subscriber_new(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save(commit=False)
            subscriber.user = request.user
            subscriber.save()
            return redirect('subscriber_list')
    else:
        form = SubscriberForm()
    return render(request, 'subscriber_edit.html', {'form': form})

@login_required
def subscriber_edit(request, pk):
    subscriber = get_object_or_404(Subscriber, pk=pk, user=request.user)
    if request.method == "POST":
        form = SubscriberForm(request.POST, instance=subscriber)
        if form.is_valid():
            form.save()
            return redirect('subscriber_list')
    else:
        form = SubscriberForm(instance=subscriber)
    return render(request, 'subscriber_edit.html', {'form': form})

@login_required
def subscriber_delete(request, pk):
    subscriber = get_object_or_404(Subscriber, pk=pk, user=request.user)
    if request.method == "POST":
        subscriber.delete()
        return redirect('subscriber_list')
    return render(request, 'subscriber_confirm_delete.html', {'subscriber': subscriber})