from .models import Cart, GymEquipment, Supplements  # Import your Cart model


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
        # Handle the case where the product with the given ID doesn't exist
        return 0  # or raise an exception, return a default value, etc.


def cart_context(request):
    cart_items = []
    cart_total = 0

    if request.user.is_authenticated:
        # For authenticated users, fetch the user's cart from the database
        cart = Cart.objects.filter(user=request.user).first()

        if cart:
            cart_items = cart.cartitem_set.all()
            cart_total = sum(item.price * item.quantity for item in cart_items)

    elif 'cart' in request.session:
        # For guest users, retrieve the cart data from the session
        cart_data = request.session['cart']

        for item_data in cart_data:
            product_type = item_data['product_type']
            product_id = item_data['product_id']
            quantity = item_data['quantity']

            # Fetch the product price directly from the database based on the product type
            price = get_product_price(product_type, product_id)

            cart_items.append({'name': 'Product Name', 'price': price, 'quantity': quantity})
            cart_total += price * quantity

    return {'cart_items': cart_items, 'cart_total': cart_total}