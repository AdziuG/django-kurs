from django.contrib import admin
from .models import Film, DodatkoweInfo, Ocena, Aktor


#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ['tytul', 'opis', 'rok']
    exclude = ['opis']
    list_display = ['tytul', 'imbd_rating', 'rok']
    list_filter = ('imbd_rating', 'rok')
    search_fields = ['tytul', 'opis']

admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Aktor)