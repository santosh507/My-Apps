#from django.db import models
from mongoengine import Document, EmbeddedDocument, fields
# Create your models here.
class CustomerAddress(EmbeddedDocument):
    street_address = fields.StringField(required=True, name="Street Address")
    country = fields.StringField(required=True,name="Country")
    city = fields.StringField(required=True,name="City")
    state = fields.StringField(name="State")
    zip_code = fields.IntField(name='Zip Code')

class CustomerDetails(Document):
    id = fields.IntField(db_field='id',primary_key=True,name='Customer ID')
    first_name = fields.StringField(required=True,name="First Name")
    last_name = fields.StringField(required=True,name="Last Name")
    full_name = fields.StringField(name="Customer Name")
    dob = fields.DateField(name="Date Of Birth", blank=False)
    phone_no = fields.IntField(name='Phone Number')
    pan_no = fields.DynamicField(name='PAN No')
    adhaar_no = fields.IntField(name='Adhaar No')
    # Seperate entity Address
    address = fields.ListField(fields.EmbeddedDocumentField(CustomerAddress))

    def save(self, *args, **kw):
        if self.full_name == '':
            self.full_name = '{0} {1}'.format(self.first_name, self.last_name)
        id_count = CustomerDetails.objects.count() + 1
        self.id = id_count
        super(CustomerDetails, self).save(*args, **kw)



