from rest_framework import serializers
from .models import Story
from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer

class StorySerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(required=False)

    class Meta:
        model = Story
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        user_profile = UserProfile.objects.get(user=user)
        story, created = Story.objects.update_or_create(
            author = user_profile,
            title = validated_data['title'],
            content = validated_data['content'],
        )
        if hasattr(validated_data, 'genre'):
            story.genre = validated_data['genre']
            story.save()
        return story
