from src.calculator.calculator import Calculator


def test_codex_demo_broken_assertion():
    result = Calculator().add(2, 2)
    assert result == 5
