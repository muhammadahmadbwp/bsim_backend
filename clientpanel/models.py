from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"brands/{base}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

class ClientsDetail(models.Model):

    GENDER = (
        ("1", "Male"),
        ("2", "Female"),
        ("3", "Other")
    )

    user = models.ForeignKey('core.User', blank=True, null=True, on_delete=models.CASCADE, related_name='client_user')
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_username = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=30, choices=GENDER, null=True, blank=True)
    avatar = models.ImageField(_("Avatar"), upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)