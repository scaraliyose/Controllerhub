# storefront/views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Product, Review, Customer
from .forms import ReviewForm


# storefront/views.py
def home(request):
    products = Product.objects.all().order_by('pk')   # was 'id'
    return render(request, 'index.html', {'products': products})



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.select_related('customer').all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review: Review = form.save(commit=False)
            review.product = product



            review.save()
            messages.success(request, "Thanks for your review!")
            return redirect('product_detail', pk=product.pk)
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ReviewForm()

    ctx = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'product_detail.html', ctx)
