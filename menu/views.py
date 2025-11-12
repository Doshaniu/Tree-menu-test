from django.shortcuts import get_object_or_404, render

from .models import MenuItem


def menu_page(request):
    return render(request, 'base.html')


def category_page(request, slug):
    item = get_object_or_404(
        MenuItem.objects.prefetch_related('children'),
        slug=slug
    )
    return render(request, 'category.html', {'item': item})
