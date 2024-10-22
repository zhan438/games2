from django.shortcuts import render
import requests
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Game

def get_current_time(zone="UTC"):
    url = f"http://worldtimeapi.org/api/timezone/{zone}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        current_datetime = data['datetime']  # Extract the current datetime
        
        # Fix the malformed offset if necessary
        if current_datetime.endswith("+01:0"):
            current_datetime = current_datetime[:-3] + "00"  # Change "+01:0" to "+01:00"
        
        # Parse the datetime string into a datetime object
        dt_object = datetime.fromisoformat(current_datetime)  # No need to slice off 'Z' as it's now fixed
        
        # Extract the time in desired format (e.g., "HH:MM:SS")
        current_time = dt_object.strftime("%H:%M:%S")
        return current_time
    except requests.RequestException as e:
        print(f"Error fetching time: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing datetime: {e}")
        return None
    
def get_time(request):
    timezone = "Europe/Vienna"  # Change this to your desired timezone
    current_time = get_current_time(timezone)
    return JsonResponse({'current_time': current_time})

def index(request):
    timezone = "Europe/Vienna" 
    current_time = get_current_time(timezone)
    games = Game.objects.all().order_by('title')
    context = {"current_time" : current_time, "games" : games}
    return render(request, 'core\index.html', context=context)
    
def minecraft_view(request):
    return render(request, 'core\minecraft.html')
def polygon_view(request):
    return render(request, 'core/polygon.html')
def geometry_dash_view(request):
    return render(request, 'core/geometry_dash.html')
def game_detail(request, game_id):
    # Retrieve the game object based on the provided game_id
    game = get_object_or_404(Game, id=game_id)
    
    
    # Prepare the context for the template
    context = {
        'game': game,
        'current_year': datetime.now().year  # Get the current year for the footer
    }
    
    # Render the game detail template with the context
    return render(request, 'core\game_template.html', context)

def handler404(request, exception, template_name="404.html"):
    response = render(None, template_name)
    response.status_code = 404
    return response