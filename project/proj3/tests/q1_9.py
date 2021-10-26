test = {   'name': 'q1_9',
    'points': [0, 0, 0.5, 0.5],
    'suites': [   {   'cases': [   {'code': '>>> tournament_results.num_rows == 45\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> tournament_results.num_columns == 4\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> players = make_array(Alternator(), Backstabber(), Bully(), Desperate(), FoolMeOnce(), Forgiver(), \n'
                                               '...                      OnceBitten(), TitForTat(), Grudger(), ForgivingTitForTat())\n'
                                               '>>> for player in players:\n'
                                               '...     assert player in tournament_results.column("p1") or player in tournament_results.column("p2")\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> t = tournament_results.where("p1", Alternator()).where("p2", Bully())\n'
                                               '>>> assert np.isclose(t["p1_mean"][0], 3.015)\n'
                                               '>>> assert np.isclose(t["p2_mean"][0], 2.99)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
