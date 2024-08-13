from django.utils import timezone
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    type_of_user_choices = [
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
        ('admin', 'Administrator'),
    ]
    type_of_user = models.CharField(
        max_length=20,
        choices=type_of_user_choices,
        default='tenant'  # Default value can be set here
    )
    phone = models.TextField()

    def __str__(self):
        return f" User {self.first_name}"
    

class Landlord(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='landlord_profile'
    )
    landlord_id_scan = models.ImageField(upload_to='landlord_id_scans/', default="LandlordIdScan")
    # auth_token = models.OneToOneField(Token, related_name='landlord_token', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.user.first_name}"

@receiver(post_save, sender=User)
def create_landlord(sender, instance, created, **kwargs):
    if created and instance.type_of_user == 'landlord':
        Landlord.objects.create(user=instance)


class Apartment(models.Model):
    name = models.TextField()
    landlord = models.ForeignKey(Landlord, related_name='apartment', on_delete=models.CASCADE, limit_choices_to={'user__type_of_user': 'landlord'})
    address = models.CharField(max_length=255)
    no_of_rooms = models.IntegerField()
    amenities = models.TextField()
    apartment_main_img = models.ImageField(upload_to='apartment_images/', default="Homi")
    # rent_date = models.PositiveSmallIntegerField(default=1, help_text="Day of the month when rent is due (e.g., 1 for 1st)")
    
    
    def __str__(self):
        return f"{self.name}"


class Tenant(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='tenant_profile'
    )
    tenant_id_scan = models.ImageField(upload_to='tenant_id_scans/', default="TenantIdScan")
   
    # auth_token = models.OneToOneField(Token, related_name='landlord_token', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.user.first_name}"

@receiver(post_save, sender=User)
def create_tenant(sender, instance, created, **kwargs):
    if created and instance.type_of_user == 'tenant':
        Tenant.objects.create(user=instance)
    



    
class Room(models.Model):
    apartment = models.ForeignKey(Apartment, related_name='rooms', on_delete=models.CASCADE)
    # room_name ="{self.apartment.name} {self.id}"
    number_of_bedrooms = models.IntegerField()
    size_in_sq_meters = models.DecimalField(max_digits=6, decimal_places=2)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    occupied = models.BooleanField(default=False)
    tenant =  models.ForeignKey(User, related_name='tenant_occupying', on_delete=models.SET_NULL, null=True, blank=True)
    # entry_date = models.DateField(default=timezone.now())
    room_images = models.ImageField(upload_to='room_images/', default="Homi rooms")
    
    def assign_tenant(self, tenant):
        self.tenant = tenant
        self.occupied = True
        self.save()

    def remove_tenant(self, tenant):
        self.tenant = None
        self.occupied = False
        self.save()
    def __str__(self):
        # name = apartment + self.id
        return f"{self.apartment.name} {self.id}"
class RoomImage(models.Model):
    room =  models.ForeignKey(Room, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return  f""

class Complaint(models.Model):
    landlord =  models.ForeignKey(Landlord, related_name='landlord_complaint', on_delete=models.CASCADE)
    tenant =  models.ForeignKey(Tenant, related_name='tenant_complaint', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='room_complaint', on_delete=models.CASCADE)
    date_field = models.DateField(timezone.now())
    complaint_body = models.TextField()
    status = models.BooleanField()
    tag_choice  = [
        ('noise', 'Noise'),
        ('repair', 'Repair'),
        ('service', 'Service'),
    ]
    tag = models.CharField(
        max_length=20,
        choices=tag_choice,
        default='No issue'  # Default value can be set here
    )

    def __str__(self):
        return self.tag
    

