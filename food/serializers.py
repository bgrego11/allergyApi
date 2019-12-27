from django.contrib.auth.models import User, Group
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import get_user_model
from .models import Food, Ingredient, LogEntry
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'groups']

        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'brand', 'categories']

        

class LogEntrySerializer(serializers.ModelSerializer):
    person = UserSerializer(read_only=False)
    item = FoodSerializer(read_only=False)

    class Meta:
        model = LogEntry
        fields = ['person','person_id', 'category', 'item','log_date']

    def create(self, validated_data):
        person_data = validated_data.pop('person')
        username = person_data.pop('username')
        person = get_user_model().objects.get_or_create(username=username)[0]
        item_data = validated_data.pop('item')
        name = item_data.pop('name')
        item = Food.objects.get_or_create(name=name)[0]
        task = LogEntry.objects.create(person=person, item=item, **validated_data)
        return task

    # def update(self, instance, validated_data):
    #     owner_data = validated_data.pop('owner')
    #     username = owner_data.pop('username')
    #     owner = get_user_model().objects.get_or_create(username=username)[0]
    #     instance.owner = owner
    #     instance.name = validated_data['name']
    #     return instance