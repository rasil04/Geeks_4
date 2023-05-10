from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import DetailView, ListView
from products.forms import ShowForm
from django.views import generic
from products.models import Order


class ProductListView(ListView):
    # queryset = models.Product.objects.filter().order_by('-id')
    queryset = models.Product.objects.filter()
    template_name = 'product/product_list.html'

    def get_queryset(self):
        # return models.Product.objects.filter().order_by('-id')
        return models.Product.objects.filter()


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Product, id=product_id)


class CreateOrderView(generic.CreateView):
    template_name = 'product/create_order.html'
    form_class = ShowForm
    queryset = Order.objects.all()
    success_url = '/product_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateOrderView, self).form_valid(form=form)


class ProductJacketView(ListView):
    queryset = models.Product.objects.filter(tag__name='jacket')
    template_name = 'product/product_jacket.html'

    def get_queryset(self):
        return models.Product.objects.filter(tag__name='jacket')


class ProductBootsView(ListView):
    queryset = models.Product.objects.filter(tag__name='boots')
    template_name = 'product/product_boots.html'

    def get_queryset(self):
        return models.Product.objects.filter(tag__name='boots')


class ProductShirtView(ListView):
    queryset = models.Product.objects.filter(tag__name='t-shirt')
    template_name = 'product/product_shirt.html'

    def get_queryset(self):
        return models.Product.objects.filter(tag__name='t-shirt')


class ProductCapView(ListView):
    queryset = models.Product.objects.filter(tag__name='cap')
    template_name = 'product/product_cap.html'

    def get_queryset(self):
        return models.Product.objects.filter(tag__name='cap')