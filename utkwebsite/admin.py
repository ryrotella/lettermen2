from django.contrib import admin
from .models import ServiceAward, LetterAward, BoardAward

# Register your models here.
@admin.register(ServiceAward)
class ServiceAwardAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'sport', 'year', 'statement', 'nominator')
    list_filter = ('sport', 'year')

@admin.register(LetterAward)
class LetterAwardAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'relation', 'statement', 'nominator')

@admin.register(BoardAward)
class BoardAwardAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'sport', 'year', 'statement', 'address_one', 'address_two', 'city', 'state', 'zip_code', 'phone', 'nominator')
    list_filter = ('sport', 'year')