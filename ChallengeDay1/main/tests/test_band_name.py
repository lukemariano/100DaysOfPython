from ChallengeDay1.main import band


def test_generate_band(monkeypatch):
    inputs = iter(['Island', 'Marry'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = band.generate_band_name()
    assert result == 'Your band name could be Island Marry'
