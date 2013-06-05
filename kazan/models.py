from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.encoding import smart_str
from hashlib import md5, sha256
from mysite import settings


def get_hexdigest(algorithm, salt, raw_password):
    """
    Returns a string of the hexdigest of the given plaintext password and salt
    using the given algorithm ('md5', 'sha1' or 'crypt').
    """
    raw_password, salt = smart_str(raw_password), smart_str(salt)
    if algorithm == 'crypt':
        try:
            import crypt
        except ImportError:
            raise ValueError('"crypt" password algorithm not supported in this environment')
        return crypt.crypt(raw_password, salt)

    if algorithm == 'md5':
        return md5(salt + raw_password).hexdigest()
    elif algorithm == 'sha1':
        return sha256(salt + raw_password).hexdigest()
    raise ValueError("Got unknown password algorithm type in password.")


class Owner(models.Model):

    user = models.OneToOneField(User)
    image = models.ImageField(upload_to='users', null=True)

    def __unicode__(self):
        return self.name

#create our user object to attach to our user_profile object
def create_owner_user_callback(sender, instance, **kwargs):
    owner, new = Owner.objects.get_or_create(user=instance)
# post_save.connect(create_owner_user_callback, User)


class Ad(models.Model):

    owner = models.ForeignKey(Owner)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='ads', null=True)
    price = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.text

class Sale(models.Model):

    ad_id = models.ForeignKey(Ad)
    buyer_id = models.ForeignKey(Owner)