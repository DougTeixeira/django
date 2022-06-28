from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *

def home(request):
    recipes = Recipe.objects.filter(
        is_published = True
    ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def category(request, category_id):
    """recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published = True,
    ).order_by('-id')

    if not recipes:
        #return HttpResponse(content='Not found', status=404)
        raise Http404('Not found🤡')"""
    
    #desse jeito não vai ordenar por ordem de criação
    #recipes = get_list_or_404(Recipe, category__id=category_id, is_published = True) 

    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id,
        is_published = True,
    ).order_by('-id')) 

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title_category': f'{recipes.first[0].category.name} Category |'
    })


def recipe(request, id):
    #recipe = Recipe.objects.filter(id=id, is_published=True).first()

    recipe = get_object_or_404(Recipe, id=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })

