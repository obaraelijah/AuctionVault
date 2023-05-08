from django.shortcuts import render,get_object_or_404,redirect
from .models import Lot,Category,Auction,Seller,Contact,Wishlist,Subscribe
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
import redis
from django.conf import settings
from django.utils.safestring import mark_safe
import json
from django.core.mail import send_mail


def all_item(request,category_slug=None):
    products=Lot.objects.filter(is_trending=True)
    category=None
    categories=Category.objects.all()
    
    print(category_slug)
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    print(category)
    
    items_trending = Lot.objects.filter(is_trending=True)
    paginator =Paginator(items_trending, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    context={
        'items':page_obj,
        'products':products,
        'categories':categories,
        'category':category, 
        
    }
    return render(request,'all_item.html',context)
    

