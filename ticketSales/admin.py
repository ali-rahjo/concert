from django.contrib import admin
from ticketSales.models import ConcertModel, LocationModel,TimeModel, ProfileModel, ticketModel
# Register your models here.

admin.site.register(ConcertModel)
admin.site.register(LocationModel)
admin.site.register(TimeModel)
admin.site.register(ProfileModel)
admin.site.register(ticketModel)
