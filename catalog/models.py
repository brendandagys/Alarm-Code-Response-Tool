from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime

# Create your models here.
class Cafeteria(models.Model):

    c_date = models.DateField(null=True, blank=False, verbose_name='Date', default=timezone.now().date())
    c_time = models.CharField(max_length=100, null=True, blank=False, verbose_name='Time (24 hr.)', default=str(datetime.datetime.now().time())[0:5])
    c_coordinator = models.CharField(max_length=100, null=True, blank=True, verbose_name='Staff Pool Coordinator')
    c_main_doors = models.CharField(max_length=100, null=True, blank=True, verbose_name='Main Doors')
    c_south_patio_doors = models.CharField(max_length=100, null=True, blank=True, verbose_name='South Patio Doors')
    c_north_patio_doors_1 = models.CharField(max_length=100, null=True, blank=True, verbose_name='North Patio Doors 1')
    c_north_patio_doors_2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='North Patio Doors 2')
    c_monitor = models.CharField(max_length=100, null=True, blank=True, verbose_name='Telephone Monitor')
    c_directors = models.CharField(max_length=100, null=True, blank=True, verbose_name='Patient/Visitor Director(s)')
    c_runners = models.CharField(max_length=100, null=True, blank=True, verbose_name='Command Centre Runner(s)')
    c_num_staff = models.CharField(max_length=100, null=True, blank=True, verbose_name='Number of Staff Present')
    c_explain = models.NullBooleanField(verbose_name='Explained to Participants')

    class Meta:
        verbose_name_plural = 'Cafeteria'
        verbose_name = 'Cafeteria'

    def __str__(self):
        if ((self.c_coordinator is None) or (self.c_coordinator == '') or (self.c_coordinator == 'None')): # Last two unnecessary?
            str_value = 'Undeclared Coordinator'
        else:
            str_value = self.c_coordinator

        return ', '.join([str(self.c_date), str_value])

    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this location."""
    #     return reverse('cafeteria_detail', args=[str(self.id)])

class East_Lobby(models.Model):
    e_date = models.DateField(null=True, blank=True, verbose_name='Date', default=timezone.now().date())
    e_time = models.CharField(max_length=100, null=True, blank=False, verbose_name='Time (24 hr.)', default=str(datetime.datetime.now().time())[0:5])
    e_coordinator = models.CharField(max_length=100, null=True, blank=True, verbose_name='Staff Pool Coordinator')
    e_main_doors = models.CharField(max_length=100, null=True, blank=True, verbose_name='Main Doors')
    e_lab_entrance = models.CharField(max_length=100, null=True, blank=True, verbose_name='Lab Entrance')
    e_ed_entrance = models.CharField(max_length=100, null=True, blank=True, verbose_name='ED Entrance')
    e_monitor = models.CharField(max_length=100, null=True, blank=True, verbose_name='Telephone Monitor')
    e_directors = models.CharField(max_length=100, null=True, blank=True, verbose_name='Patient/Visitor Director(s)')
    e_runners = models.CharField(max_length=100, null=True, blank=True, verbose_name='Command Centre Runner(s)')
    e_num_staff = models.CharField(max_length=100, null=True, blank=True, verbose_name='Number of Staff Present')
    e_explain = models.NullBooleanField(verbose_name='Explained to Participants')

    class Meta:
        verbose_name_plural = 'East Lobby'
        verbose_name = 'East Lobby'

    def __str__(self):
        if self.e_coordinator == '':
            str_value = 'Undeclared Coordinator'
        else:
            str_value = self.e_coordinator

        return ', '.join([str(self.e_date), str_value])

    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this location."""
    #     return reverse('east_lobby_detail', args=[str(self.id)])

class Town_Centre(models.Model):
    t_date = models.DateField(null=True, blank=True, verbose_name='Date', default=timezone.now().date())
    t_time = models.CharField(max_length=100, null=True, blank=False, verbose_name='Time (24 hr.)', default=str(datetime.datetime.now().time())[0:5])
    t_coordinator = models.CharField(max_length=100, null=True, blank=True, verbose_name='Staff Pool Coordinator')
    t_horticultural = models.CharField(max_length=100, null=True, blank=True, verbose_name='Horticultural Entrance')
    t_town_centre_main_street = models.CharField(max_length=100, null=True, blank=True, verbose_name='Town Centre/Main Street')
    t_monitor = models.CharField(max_length=100, null=True, blank=True, verbose_name='Telephone Monitor')
    t_directors = models.CharField(max_length=100, null=True, blank=True, verbose_name='Patient/Visitor Director(s)')
    t_runners = models.CharField(max_length=100, null=True, blank=True, verbose_name='Command Centre Runner(s)')
    t_num_staff = models.CharField(max_length=100, null=True, blank=True, verbose_name='Number of Staff Present')
    t_explain = models.NullBooleanField(verbose_name='Explained to Participants')

    class Meta:
        verbose_name_plural = 'Town Centre'
        verbose_name = 'Town Centre'

    def __str__(self):
        if self.t_coordinator == '':
            str_value = 'Undeclared Coordinator'
        else:
            str_value = self.t_coordinator

        return ', '.join([str(self.t_date), str_value])

    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this location."""
    #     return reverse('town_centre_detail', args=[str(self.id)])


class CodeStatuses(models.Model):
    code_red_status = models.CharField(max_length=100, null=True, blank=True, verbose_name='Code Red Status', default='Normal')
    status_setter = models.CharField(max_length=100, null=True, blank=True, verbose_name='Status Setter')
    from_location = models.CharField(max_length=100, null=True, blank=True, verbose_name='From')
    to_location = models.CharField(max_length=100, null=True, blank=True, verbose_name='To')

    class Meta:
        verbose_name_plural = 'Code Red Status'
        verbose_name = 'Code Red Status'

    def __str__(self):
        # return self.code_red_status
        return ', '.join([self.code_red_status, self.status_setter, self.from_location, self.to_location])
