from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                   'image', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']





class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'



class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'



class CarSerializer(serializers.ModelSerializer):
        class Meta:
            model = Car
            fields = ['id', 'brand', 'model', 'year', 'type_status', 'transmission', 'mileage', 'price']



class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'



class BidSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%Y')
    class Meta:
        model = Bid
        fields = ['id', 'auction', 'buyer', 'amount', 'created_at']



class FeedbackSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%Y')

    class Meta:
        model = Feedback
        fields = ['id', 'seller', 'buyer', 'rating', 'comment', 'created_at']