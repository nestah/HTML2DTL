import re

def convert_html_to_dtl(content):
    # Add {% load static %} at the beginning of the content
    dtl_content = "{% load static %}\n" + content
    
    # Convert static file references to Django's static template tag
    dtl_content = re.sub(r'href="assets/(.*?)"', r'href="{% static \'assets/\1\' %}"', dtl_content)
    dtl_content = re.sub(r'src="assets/(.*?)"', r'src="{% static \'assets/\1\' %}"', dtl_content)
    
    # Remove backslashes before single quotes in {% static %} tags
    dtl_content = re.sub(r'{% static \\\'(.*?)\\\' %}', r"{% static '\1' %}", dtl_content)
    
    return dtl_content



