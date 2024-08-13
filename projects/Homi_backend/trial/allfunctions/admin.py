from django.contrib import admin
from .models import Apartment, Complaint, Room, Landlord, RoomImage, Tenant, User

# Register your models here.\
admin.site.register(Apartment)
admin.site.register(Room)
admin.site.register(Landlord)
admin.site.register(Tenant)
admin.site.register(User)
admin.site.register(Complaint)
admin.site.register(RoomImage)
