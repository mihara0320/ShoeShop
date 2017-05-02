from django.shortcuts import render
from showcase.models import Item

def content_view(request):
    model = Item
    template_name = 'cart/content.html'
    queryset = model.objects.all()
    items_in_cart = []
    total_price = 0
    message = None


    try:
        cart = request.session.get('cart')
        if (len(cart) == 0):
            message = 'Your cart is empty'
        else:
            for key in cart:
                query = model.objects.get(pk = key)
                total_price += query.price
                print(total_price)
                items_in_cart.append(query)
    except:
        print("Cart does not exist")
        message = 'Please log in'


    if request.method == 'GET':
        print('get')

    elif request.method == 'POST':
        print('post')
        message = 'Thank you for shopping for us'
        cart = ()
        request.session.modified = True
        items_in_cart = []

    context = {
        'Item':model,
        'items_in_cart': items_in_cart,
        'total_price': total_price,
        'message':message,
    }

    print(context['total_price'])
    return render(request, template_name, context)
