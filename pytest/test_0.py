
from pytest import mark
# you can actually do whatever
# ruftrum = mark.ruftrum will work and create a "ruftrum" test. 
slow = mark.slow


@slow
def test_0():

    workdir = "tests/output/test_blacklist"
    configfi = "tests/data/test.config"
    .... your TEST
    
