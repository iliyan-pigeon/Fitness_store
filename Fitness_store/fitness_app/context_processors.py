from .models import Cart, GymEquipment, Supplements


def get_product_price(product_type, product_id):
    try:
        if product_type == 'gym_equipment':
            product = GymEquipment.objects.get(pk=product_id)
        elif product_type == 'supplements':
            product = Supplements.objects.get(pk=product_id)
        else:
            raise ValueError("Invalid product type")

        return product.price
    except (GymEquipment.DoesNotExist, Supplements.DoesNotExist):
        return 0


def cart_context(request):
    cart_items = []
    cart_total = 0

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()

        if cart:
            cart_items = cart.cartitem_set.all()
            cart_total = sum(item.price * item.quantity for item in cart_items)

    elif 'cart' in request.session:
        cart_data = request.session['cart']

        for item_data in cart_data:
            product_type = item_data['product_type']
            product_id = item_data['product_id']
            quantity = item_data['quantity']

            price = get_product_price(product_type, product_id)

            cart_items.append({'name': 'Product Name', 'price': price, 'quantity': quantity})
            cart_total += price * quantity

    return {'cart_items': cart_items, 'cart_total': cart_total}
