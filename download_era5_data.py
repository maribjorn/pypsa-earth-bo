import cdsapi
c = cdsapi.Client()
c.retrieve("southamerica-2013-era5",
{
"variable": "temperature",
"pressure_level": "1000",
"product_type": "reanalysis",
"year": "2013",
"month": "01",
"day": "01",
"time": "12:00",
"format": "grib"
}, "download.grib")