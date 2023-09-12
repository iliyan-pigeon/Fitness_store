from .models import Cart


def get_or_create_cart(request):
    if request.user.is_authenticated:
        # If the user is authenticated, associate the cart with the user
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # If the user is a guest, use session-based cart
        cart_id = request.session.get('cart_id')
        if cart_id:
            # If a cart ID is found in the session, get the cart
            cart, created = Cart.objects.get_or_create(id=cart_id)
        else:
            # If no cart ID is found, create a new cart and store its ID in the session
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id

    return cart
