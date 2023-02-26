from django.contrib import admin
from .models import Demande, Professeur, DemandeCED

# Register your models here.
admin.site.register(Demande)
admin.site.register(DemandeCED)
admin.site.register(Professeur)
# admin.site.register(Album)
# admin.site.register(Musician)
