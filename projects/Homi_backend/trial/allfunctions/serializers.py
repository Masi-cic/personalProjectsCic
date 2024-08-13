from tokenize import Comment
from rest_framework import serializers
from .models import Complaint, Landlord, Apartment, Room, RoomImage, Tenant, User
from django.contrib.auth import authenticate

class LandlordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Landlord
        fields = '__all__'
class TenantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tenant
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Apartment
        fields = '__all__'


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ('id', 'image')


class RoomSerializer(serializers.ModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True)  # Nested serializer for room images
    
    class Meta:
        model = Room
        fields = '__all__'
    
    
    def validate(self, data):
        apartment = data.get('apartment', None)

        if apartment:
            excisting_room_count = Room.objects.filter(apartment=apartment).count()

            if excisting_room_count >= apartment.no_of_rooms:
                raise serializers.ValidationError("Cannot add more rooms. Maximum units reached for this apartment.")
        
        return data


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'phone', 'type_of_user']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(email=data.get('email'), password=data.get('password'))
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Invalid credentials')