test = {   'name': 'q2_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> len(country_array) == 4\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> "United States" in country_array\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> "China" in country_array\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.count_nonzero(np.isin(country_array, all_countries.column("Country"))) == 4\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all_countries.where("Country", country_array.item(2)).column("Earliest Year") <= 1990\narray([ True])', 'hidden': False, 'locked': False},
                                   {'code': '>>> all_countries.where("Country", country_array.item(3)).column("Earliest Year") <= 1990\narray([ True])', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(comparison_data.group("country").column("country")) == 4\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(comparison_data.labels) == 5\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure country_array is in alphabetical order!\n'
                                               '>>> country_array.item(0) < country_array.item(1) < country_array.item(2) < country_array.item(3)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
