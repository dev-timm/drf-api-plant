from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user
        

    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'full_name', 'bio', 'profile_image', 'created_on', 'updated_on', 'is_owner'
        ]