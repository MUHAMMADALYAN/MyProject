from django.shortcuts import render

# Create your views here.
from .models import  Events


def index(request):
    events=Events.objects.all()
    return render(request, 'index.html', {'events': events})

"""
    dest1=Events()
    dest1.title="2 June 2018 Mehndi"
    dest1.description="Mehndi Dolki Dance Haleem Chawal Dol Bajey "
    dest1.button_text="See Venue"

    dest2 = Events()
    dest2.title = "3 June 2018 Barat"
    dest2.description = "Barat Dolki Dance Haleem Chawal Dol Bajey "
    dest2.button_text = "See Venue"

    dest3 = Events()
    dest3.title = "4 June 2018 Walima"
    dest3.description = "Walima Dolki Dance Haleem Chawal Dol Bajey "
    dest3.button_text = "See Venue"

    events=[dest1,dest2,dest3]"""

