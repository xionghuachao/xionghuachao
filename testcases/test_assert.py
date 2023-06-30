import pytest
from pytest_assume.plugin import assume
class TestAssert:
    def test_assert(self):
        with assume:assert "i" in "wwww"
        pytest.assume(1+1==3)
        assert 1+1==2
        print("over")