from .forms import ProductSearchForm
from .models import Cart, GymEquipment, Supplements, FitnessUser


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

    elif 'cart_id' in request.session:
        cart_data = Cart.objects.get(id=request.session.get('cart_id')).cartitem_set.all()
        cart_items = cart_data
        cart_total = sum(item.price * item.quantity for item in cart_items)

    search_form = ProductSearchForm

    return {'cart_items': cart_items, 'cart_total': cart_total, 'search_form': search_form}
