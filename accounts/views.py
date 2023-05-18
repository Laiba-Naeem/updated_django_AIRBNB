
# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer, RegisterSerializer, GoogleSignSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
# Register API


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        print("Debugging....")
        serializer = self.get_serializer(data=request.data)
        print("request.data", request.data)
        if serializer.is_valid():
            print("Serializer is Valid")
            user = serializer.save()
            print("Checking.....")

            return Response(
                {
                    "user": UserSerializer(
                        user, context=self.get_serializer_context()
                    ).data
                }
            )
        else:
            print(serializer.errors)
            return Response({"error": serializer.errors})


class RegisterGoogleSign(generics.GenericAPIView):
    serializer_class = GoogleSignSerializer

    def post(self, request, *args, **kwargs):
        print("Debugging....")
        serializer = self.get_serializer(data=request.data)
        print("request.data", request.data)
        if serializer.is_valid():
            print("Serializer is Valid")
            user1 = serializer.save()
            print("Checking.....")
            token = get_tokens_for_user(user1)
            return Response({"token": token})
        else:
            print(serializer.errors)
            return Response({"Error while registering user"})


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                data={"msg": "successful"}, status=status.HTTP_205_RESET_CONTENT
            )
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SpecificUserView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # below line is getting user id from access token
            request.data["id"] = request.user.id
            instance = User.objects.filter(id=request.data["id"])
            serializer = UserSerializer(instance, many=True)
            print("Success Ful")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
