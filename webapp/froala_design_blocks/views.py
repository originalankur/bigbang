from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "frola_design_blocks/index.html")

def call_to_action(request):
    return render(request, "frola_design_blocks/call-to-action.html")

def contacts(request):
    return render(request, "frola_design_blocks/contacts.html")

def contents(request):
    return render(request, "frola_design_blocks/contents.html")

def features(request):
    return render(request, "frola_design_blocks/features.html")

def footers(request):
    return render(request, "frola_design_blocks/footers.html")

def forms(request):
    return render(request, "frola_design_blocks/forms.html")

def headers(request):
    return render(request, "frola_design_blocks/headers.html")

def pricings(request):
    return render(request, "frola_design_blocks/pricings.html")

def teams(request):
    return render(request, "frola_design_blocks/teams.html")

def testimonials(request):
    return render(request, "frola_design_blocks/testimonials.html")
