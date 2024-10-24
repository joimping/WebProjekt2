import json
from django.shortcuts import render
import xml.etree.ElementTree as ET
from django.contrib.auth.decorators import login_required
from .models import ContactForm, Comment
from .forms import CommentForm as cf
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
@login_required
def index (request): 

    # XML-Datei parsen
    tree = ET.parse('xml/data.xml')
    root = tree.getroot()


    # Daten extrahieren
    blog_daten = []
    for auto in root:
        auto_daten = {}
        auto_daten['marke'] = auto.find('Automarke').text
        auto_daten['bezeichnung'] = auto.find('Autobezeichnung').text
        technische_details = auto.find('Technische_Details')
        auto_daten['leistung'] = technische_details.find('Leistung').text
        auto_daten['drehmoment'] = technische_details.find('max_Drehmomemt').text
        auto_daten['hubraum'] = technische_details.find('Hubraum').text
        auto_daten['zylinderzahl'] = technische_details.find('Zylinderzahl').text
        auto_daten['verbrauch'] = technische_details.find('Verbrauch').text
        auto_daten['getriebe'] = technische_details.find('Getriebe').text
        auto_daten['leergewicht'] = technische_details.find('Leergewicht').text
        auto_daten['hoechstgeschwindigkeit'] = technische_details.find('Hoechstgeschwindigkeit').text
        auto_daten['beschleunigung_0_100'] = technische_details.find('Beschleunigung_0_100').text
        auto_daten['erscheinungsjahr'] = technische_details.find('Erscheinungsjahr').text
        auto_daten['anzahl_tueren'] = technische_details.find('Anzahl_tueren').text
        auto_daten['farbe'] = technische_details.find('Farbe').text  # neues Attribut
        auto_daten['preis'] = technische_details.find('Preis').text    # neues Attribut
        auto_daten['baujahr'] = technische_details.find('Baujahr').text  # neues Attribut
        auto_daten['image_url'] = technische_details.find('image_url').text
        auto_daten['beschreibung'] = technische_details.find('beschreibung').text

        blog_daten.append(auto_daten)

    #Get the Intupt from Frotend contact Form
    if request.method == 'POST' and  request.content_type == 'application/json':  
        
        # JSON-Daten aus der Anfrage lesen
        daten = json.loads(request.body)
        email1 = daten.get('email')
        text = daten.get('text')


        contact_form = ContactForm(

            user =  request.user,
            email = email1,
            message =text
        )

        contact_form.save()


    comment_form = cf()
    if request.method == 'POST' and  'submit_comment' in request.POST and not request.content_type == 'application/json':
        comment_form = cf(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.save()


    comments = Comment.objects.all()


    return render(request, 'blog/index.html',  {'blog_daten': blog_daten, 'comments': comments, 'comment_form': comment_form})