from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include

from Fitness_store.fitness_app.views import HomePageView, AboutUsPageView, SupplementsPageView, GymEquipmentPageView, \
    ContactsPageView, LoginUserView, EquipmentProductPageView, SupplementProductPageView, \
    RegisterUserView, LogoutUserView, ProfileDetailView, ProfileEditView, ProfileDeleteView, add_to_cart, \
    remove_from_cart, PasswordChangeView, PasswordChangeDoneView, CustomPasswordResetView, \
    search_product, complete_order

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
    path('password_change/', PasswordChangeView.as_view(), name='password change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password change done'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password reset done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='password_reset_confirm_form.html'),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('complete_order/', complete_order, name='complete order'),
    path('search_product/', search_product, name='search product')
]
