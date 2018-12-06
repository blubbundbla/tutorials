To be able to use pytest and it's powerful methods, do:

1. every test needs to be written in a function and end with an assert statement. When the test falls, it prints out where something was not running as expected.
2. mark tests as slow or with other markers to be able to skip them
3. write a seetings file to customize what is being run
4. you can use coverage tests and stuff to understand which lines of code are not tested


add following to travis if you want:

   - pip install pytest-cov pytest-xdist
   - python setup.py install

  - sh tests/run_tests.sh
  
  after_success:
    - curl -s https://codecov.io/bash | bash
