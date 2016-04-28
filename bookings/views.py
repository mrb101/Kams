from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from forms import BookingForm
from models import Booking


def index(request):
    template = 'booking/index.html'
    form = BookingForm(request.POST or None)
    if form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        booking.save()
        messages.success(request, "Your booking was completed successfully!")
        return redirect('/bookings/')
    context = {'form': form}
    return render(request, template, context)


def bookings(request):
    template = 'booking/list.html'
    bookings = Booking.objects.all().filter(user=request.user)
    context = {'bookings': bookings}
    return render(request, template, context)


def booking(request, pk):
    template = 'booking/detail.html'
    queryset = Booking.objects.filter(user=request.user)
    booking = get_object_or_404(queryset, pk=pk)
    context = {'booking': booking}
    return render(request, template, context)


def delete_booking(request, pk):
    queryset = Booking.objects.filter(user=request.user)
    booking = get_object_or_404(queryset, pk=pk)
    booking.delete()
    messages.warning(request, "Your booking was deleted!")
    return redirect('/bookings/')
