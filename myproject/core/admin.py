from django.contrib import admin
from myproject.core.models import Distributor, Category, Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ('movie', 'distributor__distributor')
    list_display = ('movie', 'distributor')


admin.site.register(Distributor)
admin.site.register(Category)
