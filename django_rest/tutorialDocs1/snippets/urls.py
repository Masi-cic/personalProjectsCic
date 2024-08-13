from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns #this i should do research on
from .views import SnippetList, SnippetDetail, UserList, UserDetail, CustomAuthToken, api_root
from rest_framework.authtoken.views import obtain_auth_token

'''we used the below for function based views '''
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
'''we used the below for class based views'''
urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('snippets/', SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('', api_root, name='api-root'),
]

urlpatterns = format_suffix_patterns(urlpatterns)