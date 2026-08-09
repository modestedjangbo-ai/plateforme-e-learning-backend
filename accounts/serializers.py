from rest_framework import serializers

from .models import User



# ==========================
# SERIALIZER INSCRIPTION
# ==========================

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password',
            'role'
        ]

        extra_kwargs = {

            'password': {
                'write_only': True
            }

        }



    def create(self, validated_data):

        user = User.objects.create_user(

            username=validated_data['username'],

            email=validated_data.get('email'),

            password=validated_data['password'],

            role=validated_data.get('role', 'student')

        )


        return user





# ==========================
# SERIALIZER LISTE UTILISATEURS
# ==========================

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = [

            'id',

            'username',

            'email',

            'role'

        ]