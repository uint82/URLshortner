from django.shortcuts import render, redirect
from django.http import Http404
import random
import string
from .models import URLMapping

def generate_short_code(length=6):
    """Generate a random short code for the URL"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def home(request):
    context = {}
    
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        
        if not original_url:
            context['error'] = 'Please enter a valid URL'
            return render(request, 'url_shortner/index.html', context)
            
        # Check if URL already exists in database
        existing_mapping = URLMapping.objects.filter(original_url=original_url).first()
        
        if existing_mapping:
            context['short_url'] = existing_mapping.short_code
        else:
            # Generate a unique short code
            short_code = generate_short_code()
            while URLMapping.objects.filter(short_code=short_code).exists():
                short_code = generate_short_code()
                
            # Save the new mapping
            new_mapping = URLMapping(
                original_url=original_url,
                short_code=short_code
            )
            new_mapping.save()
            
            context['short_url'] = short_code
    
    return render(request, 'url_shortner/index.html', context)

def redirect_to_original(request, short_code):
    """Redirect short URL to original URL"""
    try:
        mapping = URLMapping.objects.get(short_code=short_code)
        # Increment the click count
        mapping.clicks += 1
        mapping.save()
        
        return redirect(mapping.original_url)
    except URLMapping.DoesNotExist:
        raise Http404("Short URL does not exist")
