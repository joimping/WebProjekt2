from django.shortcuts import render
import xml.etree.ElementTree as ET

# Create your views here.

def index (request): 

    # XML-Datei parsen
    tree = ET.parse('xml/data_copy.xml')
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
        auto_daten['image_url'] = technische_details.find('image_url').text
        blog_daten.append(auto_daten)

    for a in blog_daten:
        print(a ['marke']) 
        print(a ['bezeichnung'])
        print(a ['leistung'])
        print(a ['drehmoment'])  
        print('')

    #Get the Intupt from Frotend contact Form
    if request.method == 'POST':
        print('Empfangen', 'Name: ', request.POST['name'], ' Email: ', request.POST['email'], ' Text: ' , request.POST['text']) 


    return render(request, 'blog/index.html',  {'blog_daten': blog_daten})