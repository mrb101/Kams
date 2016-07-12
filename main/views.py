from django.shortcuts import render
from models import Album, Gallery


def home(request):
    template = 'main/index.html'
    context = {}
    return render(request, template, context)


def about(request):
    template = 'main/about.html'
    context = {}
    return render(request, template, context)


def album(request):
    template = 'main/album.html'
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, template, context)


def gallery(request, pk):
    template = 'main/gallery.html'
    images = Gallery.objects.filter(album=pk)
    context = {'images': images}
    return render(request, template, context)


def contact(request):
    template = 'main/contact.html'
    context = {}
    return render(request, template, context)


def services(request):
    template = 'main/services.html'
    context = {}
    return render(request, template, context)
