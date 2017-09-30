import lexicon
import pytest

@pytest.fixture(scope="module")
def before():
    print('\n[Setup] before test')

    def fin():
        print('\n[Teardown], finnished')
    request.addfinalizer(fin)

@pytest.mark.parametrize("test_input, expected_output", 
                     [

                     ("north",[('direction', 'north')]),
                     ("south",[('direction', 'south')]),
                     ("east",[('direction', 'east')]),
                     ("eat",[('verb', 'eat')]),
                     ("kill",[('verb', 'kill')]),
                     ("the",[('stop', 'the')]),
                     ("in",[('stop', 'in')]),
                     ("bear",[('noun', 'bear')]),
                     ("princess",[('noun', 'princess')]),
                     ("ASDFAD",[('error', 'ASDFAD')]),
                     ("1234",[('number', 1234)]),
                     ("kronor",[('money', 'kronor')]),
                     ("meter",[('distance', 'meter')]),

                     ]
                    )

def test_all(test_input, expected_output):
    all = lexicon.scan(test_input)
    assert all == expected_output

def test_finnish(request):
    print("end of the test")
