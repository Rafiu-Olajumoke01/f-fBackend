from rest_framework import serializers
from .models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, data):
         user = User.objects.create_user(
             first_name = data['first_name'],
             last_name = data['last_name'],
             email = data['email'],
             password = data['password'],
         )
         return user