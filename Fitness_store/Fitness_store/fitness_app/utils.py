from .models import Cart, Order


def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart, created = Cart.objects.get_or_create(id=cart_id)
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id

    if not cart.session_key:
        cart.session_key = request.session.session_key
        cart.save()

    return cart


def get_or_create_order(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user)
    else:
        order_id = request.session.get('cart_id')
        if order_id:
            order, created = Order.objects.get_or_create(id=order_id)
        else:
            order = Order.objects.create()
            request.session['order_id'] = order.id

    return order
