from django.shortcuts import render

# Create your views here.
def home(request):

    import json
    import  requests
    zipcode = '89129'

    if request.method == 'POST':
        if request.POST['zipcode']:
            zipcode = request.POST['zipcode']




    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipcode +"&distance=25&API_KEY=EA1E5ECD-D846-4F39-B81A-7DA379B888A7")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=~zipCode~&distance=25&API_KEY=EA1E5ECD-D846-4F39-B81A-7DA379B888A7
    return render(request,'home.html', {'api': api})

def about(request):
    return render(request,'about.html')
