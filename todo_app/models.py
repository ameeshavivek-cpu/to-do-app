from django.db import models

class TodoModel(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField()

# foreignkey (many to one)

# one to one field

# user-profile

# many to many relation

# publication_books

# movies and actors


# on_delete=models.DO_NOTHING
# on_delete=models.CASCADE
# on_delete=models.SET_NULL