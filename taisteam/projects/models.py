from django.db import models

class Notice(models.Model):
    notification = models.CharField(max_length=11)
    about = models.CharField(max_length=255)
    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=True)
    date = models.DateField(auto_now_add=True)
    worker = models.CharField(max_length=30)
    in_archive = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-notification']


    def __str__(self):
        return self.notification


class LettersTais(models.Model):
    notification = models.CharField(max_length=10)
    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=True)
    content = models.CharField(max_length=255)
    to_whom = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    worker = models.CharField(max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-notification']


    def __str__(self):
        return self.notification


class LettersTeks(models.Model):
    notification = models.CharField(max_length=10)
    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=True)
    content = models.CharField(max_length=255)
    to_whom = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    worker = models.CharField(max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-notification']


    def __str__(self):
        return self.notification


class LettersTechBureau(models.Model):
    notification = models.CharField(max_length=10)
    project = models.ForeignKey('Project', on_delete=models.PROTECT, null=True)
    content = models.CharField(max_length=255)
    to_whom = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    worker = models.CharField(max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)



class IncomingLetters(models.Model):
    notification = models.CharField(max_length=50)
    project = models.ForeignKey('Project', on_delete=models.PROTECT)
    content = models.CharField(max_length=255)
    from_whom = models.CharField(max_length=30)
    date = models.DateField(null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)




class Team(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    job = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    mobile_number = models.CharField(max_length=11)


    class Meta:
        ordering = ['-surname']


    def __str__(self):
        return self.surname


    def mobile_str(self):
        return f'+7-({self.mobile_number[1:4]})-{self.mobile_number[4:7]}-{self.mobile_number[7:9]}-{self.mobile_number[9:11]}'


class Project(models.Model):
    title = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


class Stages(models.Model):
    title = models.CharField(max_length=255)
    document = models.CharField(max_length=255)
    date_start = models.DateField(null=True)
    date_finish = models.DateField(null=True)
    project = models.ForeignKey('Project', on_delete=models.PROTECT)
    is_completed = models.BooleanField(default=False)


class Status(models.Model):
    title = models.CharField(max_length=20)


class PKD(models.Model):
    number = models.IntegerField()
    notification = models.CharField(max_length=100)
    title = models.CharField(max_length=255)

    agreement = models.BooleanField(default=False)
    supplied = models.BooleanField(default=False)
    in_archive = models.BooleanField(default=False)

    status = models.ForeignKey('Status', on_delete=models.PROTECT, null=True)

    supplied_by = models.ForeignKey('LettersTais', on_delete=models.PROTECT, null=True)
    released_by = models.ForeignKey('Notice', on_delete=models.PROTECT, null=True)

    inventory_number = models.CharField(max_length=15)

    is_paper_copy_sent = models.BooleanField(default=False)
    is_pdf_copy_sent = models.BooleanField(default=False)

    letter_for_paper_sent = models.ForeignKey('LettersTechBureau', on_delete=models.PROTECT, null=True)

    note = models.CharField(max_length=255)