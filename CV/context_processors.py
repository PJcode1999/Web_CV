from .models import SocialLink,PersonalDetailsModel,Language

def const_data(request):
    social = SocialLink.objects.all()
    for link in social:
        if link.id == 1:
            github=link
        if link.id == 2:
            linkedin=link
        if link.id == 3:
            insta=link
        if link.id == 4:
            whatsapp=link
    return {
        'github':github,
        'linkedin':linkedin,
        'insta':insta,
        'whatsapp':whatsapp,

        'user_object' : PersonalDetailsModel.objects.all(),
        'lang' : Language.objects.all(),
    }
  
