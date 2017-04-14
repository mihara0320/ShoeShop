from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from showcase.models import Item

def new_arrivals_view(request):
    model = Item
    queryset = Item.objects.all().order_by("date")
    template_name = 'showcase/new_arrival.html'
    context = {'Item':model}

    print(request)

    if request.method == 'GET':
        new_arrivals = []

        if len(queryset) <= 5:
            for i in range(0, len(queryset)):
                new_arrivals.append(queryset[i])
        else:
            for i in range(0, 5):
                new_arrivals.append(queryset[i])

        context.update({'new_arrivals':new_arrivals})
        return render(request, template_name, context)

def brand_list_view(request):
    queryset = Item.objects.all().order_by("brand")
    template_name = 'showcase/brand_list.html'
    context = {'Item':Item}
    brand_list = []

    if request.method == 'GET':
        for item in queryset:
            if item.brand in brand_list:
                pass
            else:
                brand_list.append(item.brand.upper())

        ordered_list = sorted(brand_list)
        context.update({'brand_list':ordered_list})
        return render(request, template_name, context)

    if request.method == 'POST':
        template_name = 'showcase/index.html'
        filtered_list = []
        selected_brand = None

        for item in queryset:
            if item.brand in brand_list:
                pass
            else:
                brand_list.append(item.brand.upper())

        for brand in brand_list:
            if request.POST.get(brand) is not None:
                selected_brand = brand

        result = Item.objects.filter(brand=selected_brand)
        context.update({'item_list':result})

        return render(request, template_name, context)


class IndexView(ListView):
    queryset = Item.objects.all().order_by("price")
    template = 'showcase/index.html'
    context = {'item_list':queryset}

    def get(self, request):
        category = request.GET.get("category")
        result = None

        if category == "shoes":
            result = Item.objects.filter(category='1')

        elif category == "boots":
            result = Item.objects.filter(category='2')

        else:
            result = Item.objects.all().order_by('name')

        print(result)            
        self.context.update({'item_list':result})

        return render(request, self.template, self.context)


class ItempageView(DetailView):
    model = Item
    template_name = 'showcase/itempage.html'
    context = {'Item':model}

    def get(self, request, **kwargs):
        self.object = self.get_object()
        context = super(ItempageView, self).get_context_data(**kwargs)
        return self.render_to_response(context=context)

    def post(self, request, **kwargs):
        if "cart" in request.session:
            cart = request.session["cart"]
            pk = kwargs.get('pk')
            cart.append(pk)
            request.session.modified = True
            print(cart)

            self.context.update({'cart':cart})
            self.object = self.get_object()
            context = super(ItempageView, self).get_context_data(**kwargs)

            return self.render_to_response(context=context)
        else:
            print ('you need to login first ') # TODO
