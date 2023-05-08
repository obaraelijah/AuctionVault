from django.contrib import admin
from .models import Category, Seller, Lot, WishList, Contact, Auction, Message, Subscribe

class LotAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'seller', 'category', 'base_price', 'current_price', 'is_live', 'year_published')
    list_display_links = ('id', 'product_name')
    list_filter = ('category', 'seller')
    list_editable = ('base_price', 'is_live')
    search_fields = ('product_name', 'seller__name')
    list_per_page = 25

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_no')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'contact_no')

class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lot_id', 'Wishlisted_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'lot__product_name')
    list_per_page = 25

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'lot_id', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'lot__product_name')
    list_per_page = 25

class AuctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'start', 'curr_time')
    list_display_links = ('id', 'item')
    search_fields = ('item__product_name',)
    list_per_page = 25

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'auction', 'timecap', 'price')
    list_display_links = ('id', 'author')
    search_fields = ('author__username', 'auction__item__product_name')

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('id', 'email')
    search_fields = ('email',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Lot, LotAdmin)
admin.site.register(WishList, WishListAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Auction, AuctionAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
