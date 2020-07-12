from rest_framework import serializers
from .models import Contact, User

User._meta.get_field('email')._unique = True

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Contact
        fields = ['url', 'id', 'name', 'email', 'phone1', 'phone2', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    contacts = serializers.HyperlinkedRelatedField(many=True, view_name='contact-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'contacts']