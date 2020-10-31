from sw_utils import settings as utils_settings 

def context(request):
    show_admin      = utils_settings.SHOW_ADMIN 
    image_not_found = utils_settings.IMAGE_NOT_FOUND
    return locals()

