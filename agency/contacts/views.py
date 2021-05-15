from django.shortcuts import redirect
from django.contrib import messages
from .models import Contact


def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    realtor_email = request.POST['realtor_email']
    realtor_id = request.POST['realtor_id']

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message)

    contact.save()

    messages.success(request, 'Ваша заявка успешно отправлена, '
                              'дожидайтесь обратной связи по телефону и электронной почте!')
    return redirect('/listings/'+listing_id)
