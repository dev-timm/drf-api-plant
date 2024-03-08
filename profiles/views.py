from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileList(APIView):
    def get(seld, request):
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)

        return Response(serializer.data)
