from django.db import models


class Team(models.Model):
    name = models.CharField(verbose_name='チーム名', max_length=50)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(verbose_name='選手名', max_length=50)
    team = models.ForeignKey(to=Team,
                             verbose_name='所属チーム',
                             on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['name', 'team'],
                                               name='unique_player')]

    def __str__(self):
        return f'{self.team} : {self.name}'