from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.db.models import Q

from .models import Product, Category, Order
from .forms import CheckoutForm
from .cart import Cart


def home(request):
    featured_products = Product.objects.filter(is_featured=True)[:6]
    if not featured_products:
        featured_products = Product.objects.all()[:6]
    categories = Category.objects.all()
    context = {
        "featured_products": featured_products,
        "categories": categories,
    }
    return render(request, "shop/home.html", context)


def product_list(request):
    products = Product.objects.all()
    query = request.GET.get("q")
    category_slug = request.GET.get("category")

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    if category_slug:
        products = products.filter(category__slug=category_slug)

    categories = Category.objects.all()
    context = {
        "products": products,
        "categories": categories,
        "query": query or "",
        "selected_category": category_slug or "",
    }
    return render(request, "shop/products.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "shop/product_detail.html", {"product": product})


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    quantity = int(request.POST.get("quantity", 1))
    cart.add(product=product, quantity=quantity)
    messages.success(request, f"Added \"{product.name}\" to your cart.")
    next_url = request.POST.get("next") or "shop:cart_detail"
    return redirect(next_url)


@require_POST
def cart_update(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    action = request.POST.get("action")
    current_qty = cart.cart.get(str(product.id), {}).get("quantity", 1)

    if action == "increase":
        cart.add(product=product, quantity=current_qty + 1, update_quantity=True)
    elif action == "decrease":
        new_qty = current_qty - 1
        if new_qty <= 0:
            cart.remove(product)
        else:
            cart.add(product=product, quantity=new_qty, update_quantity=True)
    return redirect("shop:cart_detail")


@require_POST
def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    cart.remove(product)
    messages.info(request, f"Removed \"{product.name}\" from your cart.")
    return redirect("shop:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "shop/cart.html", {"cart": cart})


def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, "Your cart is empty. Add some products first!")
        return redirect("shop:product_list")

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            customer = form.save()
            for item in cart:
                Order.objects.create(
                    customer=customer,
                    product=item["product"],
                    quantity=item["quantity"],
                    total_price=item["total_price"],
                )
                # Reduce stock
                product = item["product"]
                product.quantity = max(product.quantity - item["quantity"], 0)
                product.save()
            cart.clear()
            return redirect("shop:order_success")
    else:
        form = CheckoutForm()

    return render(request, "shop/checkout.html", {"form": form, "cart": cart})


def order_success(request):
    return render(request, "shop/order_success.html")
