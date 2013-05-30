from django.db import models
from django.utils.encoding import smart_str
from hashlib import md5, sha256


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


class User(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(('password'), max_length=128, help_text=("Use '[algo]$[salt]$[hexdigest]' or use the <a href=\"password/\">change password form</a>."))
    image = models.ImageField(upload_to='users', null=True)

    def __unicode__(self):
        return self.name

    def set_password(self, raw_password):
        import random
        algo = 'sha1'
        salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
        hsh = get_hexdigest(algo, salt, raw_password)
        self.password = '%s$%s$%s' % (algo, salt, hsh)

class Ad(models.Model):

    owner = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='ads', null=True)
    price = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.text

class Sale(models.Model):

    ad_id = models.ForeignKey(Ad)
    buyer_id = models.ForeignKey(User)