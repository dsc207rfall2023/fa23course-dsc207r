OK_FORMAT = True

test = {   'name': 'q2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> for i in range(5):\n...     for j in range(3):\n...         assert aT[i, j] == a[j, i]\n', 'hidden': True, 'locked': False},
                                   {'code': '>>> answer = np.array([[0.25, -0.3], [-0.25, 0.5]])\n>>> np.testing.assert_allclose(B_inv, answer)\n', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
