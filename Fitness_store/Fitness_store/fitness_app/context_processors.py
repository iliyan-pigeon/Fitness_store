from .forms import ProductSearchForm
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
    cart_in_progress = False

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()

        if cart:
            cart_items = cart.cartitem_set.filter(in_progress=False)
            cart_total = sum(item.price * item.quantity for item in cart_items if item.in_progress is False)

    elif 'cart_id' in request.session:
        cart_data = Cart.objects.get(id=request.session.get('cart_id')).cartitem_set.filter(in_progress=False)
        cart_items = cart_data
        cart_total = sum(item.price * item.quantity for item in cart_items if item.in_progress is False)

    search_form = ProductSearchForm

    return {'cart_items': cart_items, 'cart_total': cart_total, 'search_form': search_form}
