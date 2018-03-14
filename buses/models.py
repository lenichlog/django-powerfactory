from django.db import models


class Bus(models.Model):
    bus_name = models.CharField(max_length=200)
    bus_voltage = models.IntegerField(default=0)

    def __str__(self):
        return self.bus_name

    def has_high_voltage(self):
        return self.bus_voltage >= 1


class Line(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    line_name = models.CharField(max_length=200)
    line_voltage = models.IntegerField(default=3)

    def __str__(self):
        return self.line_name
