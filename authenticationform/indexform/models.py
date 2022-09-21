from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Posts(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    liked=models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    updated=models.DateField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')

    def __str__(self):
        return str(self.title)

    @property
    def num_likes(self):
        return self.liked.all().count()

Like_Choies=[
    ('Like','Like'),
    ('Unlike','Unlike')
]
class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    value=models.CharField(choices=Like_Choies,default='Like',max_length=10)

    def __str__(self):
        return str(self.post)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField()
    friends=models.ManyToManyField(User,related_name='friends',blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def get_friends(self):
        return str(self.friends.all())

    def get_friends_no(self):
        return str(self.friends.all().count())

    def __str__(self):
        return str(self.user)

status_choices=[
    ('send','send'),
    ('accepted','accepted'),
]

class RelationShip(models.Model):
    sender=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name='sender')
    receiver=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name='receiver')
    status=models.CharField(max_length=10,choices=status_choices)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"

class FriendList(models.Model):
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    age=models.PositiveIntegerField()
    password=models.IntegerField()

    def __str__(self):
        return self.first_name

class Car(models.Model):
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100,null=True,blank=True)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.name

class  Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=200)

    class Meta:
        ordering=['-name']

    def __str__(self):
        return self.name

class Blog(models.Model):
    name=models.CharField(max_length=100)
    tagline=models.TextField()

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog',null=True,blank=True)
    headline=models.CharField(max_length=100,null=True)
    body_text=models.TextField()
    pub_date=models.DateField()
    mod_date=models.DateField(default=date.today)
    authors=models.ManyToManyField(Author,related_name='authors')
    number_of_comment=models.IntegerField(default=0)
    rating=models.IntegerField(default=5)

    def __str__(self):
        return self.headline


