from aplicacao import tip


def test_tip(monkeypatch):
    inputs = iter(['100', '50', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = tip.tip_calculator()
    assert result == 'Each person should pay: $150.0'

