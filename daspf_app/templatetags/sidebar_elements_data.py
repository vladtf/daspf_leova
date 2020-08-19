from django import template

register = template.Library()


@register.simple_tag
def get_elements():
    elements = [
        {'url': 'http://www.leova.md/', 'title': 'Consiliul <br>Raional <br>Leova', 'image': '/images/leova-logo.png'},
        {'url': 'http://parlament.md', 'title': 'Parlamentul <br>Republicii <br>Moldova', 'image': '/images/moldova-stema.svg'},
        {'url': 'http://gov.md/', 'title': 'Guvernul <br>Republicii <br>Moldova', 'image': '/images/moldova-stema.svg'},
        {'url': 'http://www.presedinte.md/', 'title': 'Președintele <br>Republicii <br>Moldova', 'image': '/images/moldova-stema.svg'},
        {'url': 'http://cancelaria.gov.md/', 'title': 'Cancelaria <br>de Stat', 'image': '/images/moldova-stema.svg'},
        {'url': 'http://servicii.gov.md/', 'title': 'Portalul <br>Serviciilor <br>Publice', 'image': '/images/moldova-stema.svg'},
    ]

    return elements
