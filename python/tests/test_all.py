import pytest
import migrate_uv_demo


def test_sum_as_string():
    assert migrate_uv_demo.sum_as_string(1, 1) == "2"
