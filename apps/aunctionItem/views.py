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




