test = {   'name': 'q3_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> assert boston_pre_supply_binned.num_columns == 3\n'
                                               '>>> assert all([l in boston_pre_supply_binned.labels for l in ["price", "quantity", "quantity_supplied"]])\n'
                                               '>>> assert boston_pre_supply_binned.num_rows == 51\n'
                                               '>>> assert max(boston_pre_supply_binned.column("quantity_supplied")) == 19914\n'
                                               '>>> assert min(boston_pre_supply_binned.column("quantity_supplied")) == 0\n'
                                               '>>> assert len(np.unique(boston_pre_supply_binned.column("quantity_supplied"))) == 48\n'
                                               '>>> assert (np.diff(boston_pre_supply_binned.column("quantity_supplied")) >= 0).all()\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
