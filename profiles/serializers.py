from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'full_name', 'bio', 'profile_image', 'created_on', 'updated_on'
        ]