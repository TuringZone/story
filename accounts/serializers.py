from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    profile_pic = serializers.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['user', 'email', 'profile_pic']

    def create(self, validated_data):
        user_data = validated_data['user']
        print(validated_data)
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.set_password(validated_data['user']['password'])
        user.save()
        user_profile, created = UserProfile.objects.update_or_create(
            user = user,
            email = validated_data['email'],
        )
        try:
            user_profile.profile_pic = validated_data['profile_pic']
            user_profile.save()
            return user_profile
        except:
            return user_profile
