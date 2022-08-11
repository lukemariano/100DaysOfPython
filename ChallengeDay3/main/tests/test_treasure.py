from main import treasure


def test_treasure(monkeypatch):
    inputs = iter(['left', 'swim', 'yes'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = treasure.adventure()
    assert result == 'You have found the secret treasure of luquinhas adventure bank! Let is see what is inside.'
