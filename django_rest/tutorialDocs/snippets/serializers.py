from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User

STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices = STATUS_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STATUS_CHOICES, default='friendly')

    
#     def create(self, **validated_date):
#         """
#         Create and return a new 'snippet' instance, given the validated data
#         """

#         return Snippet.objects.create(**validated_date)
    
#     def update(self, instance, **validated_data):
#         """
#         update and return an excisting 'Snipper' instance, given the validated data
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


"""
the code below is replacement for the above commented code

ModelSerializer class is simply a shortcut fro creating serializer classes
"""
# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     class Meta:
#         model = Snippet
#         fields = ['id','title','code','linenos','language','style', 'owner']

# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets', 'owner']


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']