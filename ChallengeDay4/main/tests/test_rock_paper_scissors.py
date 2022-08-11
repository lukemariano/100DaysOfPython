from imp import init_builtin
from mimetypes import init

from ChallengeDay4.main import rock_paper_scissors


def test_rock_paper_scissors(monkeypatch):
    inputs = iter(['10', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = rock_paper_scissors.rock_paper_scissors()
    assert result == 'draw'



