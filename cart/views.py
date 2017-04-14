from django.shortcuts import render
# from django.views.generic import View, ListView, DetailView
from showcase.models import Item

# class contentView(ListView):
#     model = Item
#     context = {'Item':model}
#     queryset = model.objects.all()
#     template_name = 'cart/content.html'
#
#     def get(self, request):
#
#         cart = request.session.get('cart')
#         self.context.update({'cart':cart})
#         print(cart)
#
#         return render(request, self.template_name, self.context)

def content_view(request):
    model = Item
    template_name = 'cart/content.html'
    queryset = model.objects.all()
    items_in_cart = []
    total_price = 0
    message = None

    try:
        cart = request.session.get('cart')
        for key in cart:
            query = model.objects.get(pk = key)
            total_price += query.price
            items_in_cart.append(query)
    except:
        message = 'Please log in'


    if request.method == 'GET':
        print('get')

    elif request.method == 'POST':
        print('post')
        message = 'Thank you for shopping for us'

    context = {
        'Item':model,
        'items_in_cart': items_in_cart,
        'total_price': total_price,
        'message':message,
        }
    print(context['total_price'])
    return render(request, template_name, context)
