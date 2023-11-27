from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include
from django.contrib.auth import views as auth_views

from Fitness_store.fitness_app.forms import CustomSetPasswordForm
from Fitness_store.fitness_app.views import HomePageView, AboutUsPageView, SupplementsPageView, GymEquipmentPageView, \
    ContactsPageView, LoginUserView, EquipmentProductPageView, SupplementProductPageView, \
    RegisterUserView, LogoutUserView, ProfileDetailView, ProfileEditView, ProfileDeleteView, add_to_cart, \
    remove_from_cart, PasswordChangeView, PasswordChangeDoneView, \
    search_product, complete_order, orders_for_delivery, order_details, clear_session, CustomPasswordResetConfirmView, \
    CreateCheckoutSessionView, PaymentView

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
    path('complete_order/', complete_order, name='complete order'),
    path('search_product/', search_product, name='search product'),
    path('orders_for_delivery/', orders_for_delivery, name='orders for delivery'),
    path('order_datails/<int:pk>/', order_details, name='order details'),
    path('clear/', clear_session, name='clear'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('create-checkout-session', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('payment', PaymentView.as_view(), name='payment'),

]
