from django.contrib import admin

# Register your models here.

from .models import Prospects,Delegate

class ProspectsAdmin(admin.ModelAdmin):
    list_display=('email','nom','prenom','numero1','numero2','lieu','sexe','filiere','diplome','date')

class DelegateAdmin(admin.ModelAdmin):
    list_display=('delegue','date',)

admin.site.register(Prospects,ProspectsAdmin)
admin.site.register(Delegate,DelegateAdmin)