from src.app import index
# from flask import Flask
# import pytest

# @pytest.fixture(scope="session")
def test_index():
    # app = Flask(__name__)
    assert index() == "hello, world"