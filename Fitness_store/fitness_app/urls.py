from django.urls import path, include

from Fitness_store.fitness_app.views import HomePageView, AboutUsPageView, SupplementsPageView, GymEquipmentPageView, \
    ContactsPageView, LoginUserView, EquipmentProductPageView, SupplementProductPageView, \
    RegisterUserView, LogoutUserView, ProfileDetailView, ProfileEditView, ProfileDeleteView, add_to_cart, \
    remove_from_cart

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsPageView.as_view(), name='about us'),
    path('supplements/', SupplementsPageView.as_view(), name='supplements'),
    path('gym-equipment/', GymEquipmentPageView.as_view(), name='gym equipment'),
    path('contact/', ContactsPageView.as_view(), name='contacts'),
    path('equipment_product/<int:pk>/', EquipmentProductPageView.as_view(), name='equipment product'),
    path('supplement_product/<int:pk>/', SupplementProductPageView.as_view(), name='supplement product'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile_detail/<int:pk>/', ProfileDetailView.as_view(), name='profile detail'),
    path('edit/<int:pk>/', ProfileEditView.as_view(), name='profile edit'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete'),
    path('add-to-cart/<str:product_type>/<int:product_id>/', add_to_cart, name='add to cart'),
    path('remove-from-cart/<str:product_type>/<int:product_id>/', remove_from_cart, name='remove from cart'),
]