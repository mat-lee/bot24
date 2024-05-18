
import pytest
from act.crux import Crux


@pytest.mark.skip
def test_b2_crux_exe(dot_env_obj):

    Crux.exe(dot_env_obj)