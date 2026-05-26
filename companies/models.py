from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RawRecord(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    csv_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company.name


class ESGResult(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    total_fuel = models.FloatField(default=0)
    total_kwh = models.FloatField(default=0)
    flight_km = models.FloatField(default=0)

    co2_emissions = models.FloatField(default=0)
    esg_score = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} - ESG {self.esg_score}"