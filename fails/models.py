from django.db import models

class Vendor(models.Model):
    vendor_name = models.CharField(max_length = 128)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.vendor_name

class Submission(models.Model):
    title = models.CharField(max_length = 128)
    description = models.CharField(max_length = 1024)
    name = models.CharField(max_length = 64)
    location = models.CharField(max_length = 64)
    vendor_id = models.ForeignKey(Vendor)
    software = models.CharField(max_length = 128)
    upvotes = models.IntegerField(default = 0)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Image(models.Model):
    image_path = models.CharField(max_length = 1024)
    submission_id = models.ForeignKey(Submission)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return("Submission {} - {}".format(str(self.submission_id), self.image_path)

class Tag(models.Model):
    tag_text = models.CharField(max_length = 32)
    submissions = models.ManyToManyField(Submission)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return(self.tag_text)
