from compass.config import add_config
from compass.testcase import add_step, set_testcase_subdir, run_steps
from compass.examples.tests.example_expanded.res2km.test1 import step1, step2


# This function is used to define the test case by adding to or modifying the
# information in the "testcase" dictionary.  Typically, this involves adding
# steps to the test case and then potentially adding additional namelist and/or
# streams files to the step.  It must also include setting the "descriptions"
# of the test case.
def collect(testcase):
    """
    Update the dictionary of test case properties and add steps

    Parameters
    ----------
    testcase : dict
        A dictionary of properties of this test case, which can be updated
    """
    # You can set information about the test case, the resolution in this case
    resolution = '2km'
    testcase['resolution'] = resolution

    # you must add a description
    testcase['description'] = 'Template 2km test1'

    # You can change the subdirectory from the default, the name of the test
    # case.  In this case, we add a directory for the resolution.
    subdir = '{}/{}'.format(resolution, testcase['name'])
    set_testcase_subdir(testcase, subdir)

    # we can pass keyword argument to the step so they get added to the "step"
    # dictionary and can be used throughout the step
    add_step(testcase, step1)
    add_step(testcase, step2)


# this function can be used to add the contents of a config file as in the
# example below or to add or override specific config options, as also shown
# here.  The function must take only the "testcase" and "config" arguments, so
# any information you need should be added to "testcase" if it is not available
# in one of the config files used to build "config"
def configure(testcase, config):
    """
    Modify the configuration options for this test case.

    Parameters
    ----------
    testcase : dict
        A dictionary of properties of this test case

    config : configparser.ConfigParser
        Configuration options for this test case
    """
    # add (or override) some configuration options that will be used during any
    # or all of the steps in this testcase
    add_config(config, 'compass.examples.tests.example_expanded.res2km.test1',
               'test1.cfg')

    # add a config option to the config file
    config.set('example_expanded', 'resolution', testcase['resolution'])


# The function must take only the "testcase" and "config" arguments, so
# any information you need in order to run the testcase should be added to
# "testcase" if it is not available in "config"
def run(testcase, test_suite, config, logger):
    """
    Run each step of the testcase

    Parameters
    ----------
    testcase : dict
        A dictionary of properties of this test case

    test_suite : dict
        A dictionary of properties of the test suite

    config : configparser.ConfigParser
        Configuration options for this test case

    logger : logging.Logger
        A logger for output from the test case
    """
    # typically, this involves running all the steps in the testcase in the
    # desired sequence.  However, it may involve only running a subset of steps
    # if some are optional and not performed by default.
    run_steps(testcase, test_suite, config, logger)
