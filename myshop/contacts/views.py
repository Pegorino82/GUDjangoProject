from django.shortcuts import render

# Create your views here.

def contacts(request):
    context = {
        'results': [
            'one',
            'two',
            'three',
        ]
    }

    return render(request, 'contacts/contacts.html', context)
