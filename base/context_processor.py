from base.models import Categories

def get_categories(request):
    return {'categories':Categories.objects.all().order_by('created_at')}



