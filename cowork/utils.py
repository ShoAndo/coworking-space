from .models import Store

def get_defalt_store():
    return Store.objects.get(id=1)