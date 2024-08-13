from django.urls import path
from allfunctions import views

urlpatterns = [
    path('apartments/', views.ApartmentViewSet.as_view()),
    path('landlords/', views.LandlordViewSet.as_view()),
    path('rooms/', views.RoomViewSet.as_view()),
    path('tenants/', views.TenantViewSet.as_view()),
    path('complaints/', views.ComplaintViewSet.as_view()),
    path('users/', views.CustomUserViewSet.as_view()),
    

]