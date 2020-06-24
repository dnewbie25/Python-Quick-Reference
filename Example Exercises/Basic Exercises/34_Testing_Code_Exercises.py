import unittest
#City, Country

def get_city_country(city, country):
  area_string = f"{city}, {country}"
  return area_string.title()

def get_city_country_population(city, country, population=''):
  if population:
    area_string = f"{city}, {country} - {population}"
  else:
    area_string = f"{city}, {country}"
  return area_string.title()


class CityTestCase(unittest.TestCase):
  def test_city_country(self):
    test_string = get_city_country('medellin', 'COLOMBIA')
    self.assertEqual(test_string, 'Medellin, Colombia')

  def test_city_country_population(self):
    test_string = get_city_country_population('santiago', 'chile', '2000000')
    self.assertEqual(test_string, 'Santiago, Chile - 2000000')

if __name__ == '__main__':
  unittest.main()