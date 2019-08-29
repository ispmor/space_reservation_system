from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=200)
    equipement = models.TextField(max_length=1000, help_text='Enter a brief description of the room')
    capacity = models.IntegerField()
    ROOM_STATUS = (
        ('i', 'In Use'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=ROOM_STATUS,
        blank=True,
        default='a',
        help_text='Room availability',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this room."""
        return reverse('room-detail', args=[str(self.id)])

    