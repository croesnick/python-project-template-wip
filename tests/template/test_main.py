from template.main import greeting


def test_greeting():
    assert greeting() == 'Hello!'
