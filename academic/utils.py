# utils.py
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML

def render_to_pdf(template_src, context_dict):
    html_string = render_to_string(template_src, context_dict)
    html = HTML(string=html_string)
    result = html.write_pdf()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="output.pdf"'
    response.write(result)
    return response
