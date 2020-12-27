from django.shortcuts import render,redirect
from .forms import ProducerForm,ShipperForm,DetailerForm,WholesalerForm
from .models import ProducerModel,ShipperModel,DetailerModel,WholesalerModel
from django.contrib import messages
from rest_framework import generics,mixins
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.views import APIView
from django.db import models

from .services import TransactionService
from django.contrib.auth.decorators import login_required


tx_service = TransactionService()
tx_service.setup_blockchain_connection()


def home(request):
    tx_service.setup_contract("user")
    setup_forms_fields(request)
    return render(request,'blockchain/home.html')

def setup_forms_fields(request):
    producer_fields = list(ProducerForm.base_fields)
    shipper_fields = list(ShipperForm.base_fields)
    wholesaler_fields = list(WholesalerForm.base_fields)
    detailer_fields = list(DetailerForm.base_fields)

    request.session['producer_fields'] = producer_fields
    request.session['shipper_fields'] = shipper_fields
    request.session['wholesaler_fields'] = wholesaler_fields
    request.session['detailer_fields'] = detailer_fields

@login_required
def add_product(request):
    current_link = request.user.widget.lower()
    tx_service.setup_contract(current_link)

    if request.method == 'POST':
        if current_link == "producer":
            form_for_link = ProducerForm(request.POST)
        elif current_link == "shipper":
            form_for_link = ShipperForm(request.POST)
        elif current_link == "wholesaler":
            form_for_link = WholesalerForm(request.POST)
        elif current_link == "detailer":
            form_for_link = DetailerForm(request.POST)
        #form_class = LinksMultiForm(request.POST)
        #form_for_link= form_class[current_link]
        
        if form_for_link.is_valid():
            tx_service.add_link(form_for_link)
            form_for_link.save(commit=False)
            print("Form posted correctly!")
            print("Index: ",form_for_link.cleaned_data.get("product_id"))
            print("Common name: ", form_for_link.cleaned_data.get("common_name"))
            messages.success(request, 'You posted a form successfully')
            return redirect('blockchain-home')
    else:
        if current_link == "producer":
            form_for_link = ProducerForm()
        elif current_link == "shipper":
            form_for_link = ShipperForm()
        elif current_link == "wholesaler":
            form_for_link = WholesalerForm()
        elif current_link == "detailer":
            form_for_link = DetailerForm()
        #form_class = LinksMultiForm()
        #form_for_link= form_class[current_link]

    return render(request,'blockchain/add_product.html',{'form': form_for_link})

def about(request):
    return render(request,'blockchain/about.html',{'title':'About'})

def enter_prod_id(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        received_info = tx_service.get_all_links(product_id)

        print("Received product id: {}".format(received_info))
        request.session['tracked_product_id'] = received_info

        return redirect('/tracking')
    
    return render(request, 'blockchain/enter_prod_id.html')
    
def tracking(request):
    received_info = request.session['tracked_product_id']

    producer_fields= dict(zip(request.session['producer_fields'],received_info['producer']))
    shipper_fields= dict(zip(request.session['shipper_fields'],received_info['shipper']))
    wholesaler_fields = dict(zip(request.session['wholesaler_fields'],received_info['wholesaler']))
    detailer_fields = dict(zip(request.session['detailer_fields'],received_info['detailer']))
    
    tracked_product = {
        'producer_fields': producer_fields,
        'shipper_fields': shipper_fields,
        'wholesaler_fields': wholesaler_fields,
        'detailer_fields': detailer_fields,
    }
    return render(request, 'blockchain/tracking.html', context = tracked_product)
  
