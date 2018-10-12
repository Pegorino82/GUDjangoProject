from django.shortcuts import render


# Create your views here.

def contacts(request):
    context = {}
    print(request.POST)
    if request.method == "POST":
        usr_name = request.POST.get('username')
        email = request.POST.get('email')
        text = request.POST.get('text')

        context.update({
            'usr_name': usr_name,
            'email': email,
            'text': text
        })



    return render(request, 'contacts/contacts.html', context)
