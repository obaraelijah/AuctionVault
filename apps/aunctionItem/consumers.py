import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone
from .models import Message,Auction,Lot
from django.contrib.auth import get_user_model
from django.shortcuts import render,get_object_or_404
from datetime import timedelta

User = get_user_model()


