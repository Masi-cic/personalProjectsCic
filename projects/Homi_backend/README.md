# uploading images 
we can deal with images with the help of imageField 

## multiple images 
https://medium.com/ibisdev/upload-multiple-images-to-a-model-with-django-fd00d8551a1c


# authentication 
first we have to understand that there are different authentication methods 
REST framework provides several built in authentication classes such as 
- SessionAuthentication
- BasicAuthentication 
- TokenAuthentication 
- JSONWebTokenAuthentication 

we will use token based authentication for this case 
    TokenAuthentication: This authentication class uses a token-based system. Clients authenticate by including an API token in the Authorization header of HTTP requests.
    IsAuthenticated: This permission class ensures that only authenticated users (those with a valid token in this case) can access the view set.

