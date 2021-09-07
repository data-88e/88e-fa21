test = {   'name': 'q2_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> assert boston_pre_demand_binned.num_columns == 3\n'
                                               '>>> assert all([l in boston_pre_demand_binned.labels for l in ["price", "quantity", "quantity_demanded"]])\n'
                                               '>>> assert boston_pre_demand_binned.num_rows == 51\n'
                                               '>>> assert max(boston_pre_demand_binned.column("quantity_demanded")) == 9912\n'
                                               '>>> assert min(boston_pre_demand_binned.column("quantity_demanded")) == 0\n'
                                               '>>> assert len(np.unique(boston_pre_demand_binned.column("quantity_demanded"))) == 48\n'
                                               '>>> assert (np.diff(boston_pre_demand_binned.column("quantity_demanded")) <= 0).all()\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
