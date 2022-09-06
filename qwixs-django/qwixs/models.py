from django.db import models

STATES = [
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District Of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
]


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Business(models.Model):
    name = models.CharField(max_length=150)
    image_url = models.CharField(max_length=255, default='Cover Image')
    about = models.CharField(max_length=400, default='Max 400 characters')
    about_image = models.CharField(max_length=255, default='About Image')
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50, default=' ')
    state = models.CharField(max_length=2, choices=STATES, default='State')
    zipcode = models.CharField(max_length=6, default=' ')
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=255)
    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, related_name='businesses')

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.name
