from django.shortcuts import render
from showcase.models import Item

def content_view(request):
    model = Item
    template_name = 'cart/content.html'
    items_in_cart = []
    total_price = 0
    checkout_price = 0
    message = None
    context = { 'Item':model }

    try:
        cart = request.session.get('cart')
    except:
        print("Cart does not exist")

    if request.method == 'GET':
        print('get')
        if (len(cart) == 0):
            message = 'Your cart is empty'
            context.update({
                'total_price': total_price,
                'message':message, 
            })
        else:
            for key in cart:
                query = model.objects.get(pk = key)
                total_price += query.price
                items_in_cart.append(query)

            context.update({
                'total_price': total_price,
                'message':message,
                'items_in_cart': items_in_cart 
            })

    elif request.method == 'POST':
        print('post')
        message = 'Thank you for shopping for us'
        
        for key in cart:
            query = model.objects.get(pk = key)
            checkout_price += query.price
            items_in_cart.append(query)
        
        items_in_cart = []
        request.session['cart'] = ()
        request.session.modified = True
    
        context.update({
            'checkout_price': checkout_price,
            'message':message,
            'items_in_cart': items_in_cart 
        })

    return render(request, template_name, context)
