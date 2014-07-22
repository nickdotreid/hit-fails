from django.db import models

class Vendor(models.Model):
    vendor_name = models.CharField(max_length = 128)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.vendor_name

    class Meta:
        ordering = ['vendor_name']

class Submission(models.Model):
    title = models.CharField(max_length = 128)
    description = models.CharField(max_length = 1024)
    name = models.CharField(max_length = 64)
    location = models.CharField(max_length = 64, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, null=True, blank=True)
    software = models.CharField(max_length = 128, null=True, blank=True)
    upvotes = models.IntegerField(default = 0)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def has_description(self):
        if self.description:
            return True
        else:
            return False

    def tags(self):
        return self.tag_set.all()
    
class Image(models.Model):
    image_path = models.CharField(max_length = 1024)
    submission_id = models.ForeignKey(Submission)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Submission {} - {}".format(str(self.submission_id), self.image_path)

class Tag(models.Model):
    tag_text = models.CharField(max_length = 32)
    submissions = models.ManyToManyField(Submission)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return(self.tag_text)

    class Meta:
        ordering = ['tag_text']

    
