# STDLIB
import os
import pathlib
import sys
from typing import Any, Union  # noqa

"""
set the syspath accordingly, if pytest or doctest is running
this is needed for local tests
this should be the first module which is loaded by __init__.py
to avoid frozen or partially initialized modules for pytest,
and just before the project imports (for doctest)
no other module should import or use this module,
again to avoid frozen or partially initialized modules.

"""

PathLikeOrString = Union[str, "os.PathLike[Any]"]


# is_doctest_running{{{
def is_doctest_running() -> bool:
    """
    returns True if test environment is detected (pytest, doctest, docrunner)


    Result
    ----------
    True if Test environment is detected


    Exceptions
    ----------
    none


    Examples
    ----------

    >>> if not is_setup_test_running(): assert is_doctest_running() == True
    """
    # is_doctest_running}}}
    # this is used in our tests when we test cli-commands
    if os.getenv("PYTEST_IS_RUNNING"):
        return True

    for argv in sys.argv:
        if is_doctest_in_arg_string(argv):
            return True
    return False


def is_setup_test_running() -> bool:
    """if 'setup.py test' was launched"""
    for arg_string in sys.argv:
        if "setup.py" in arg_string:
            return True
    return False


def is_doctest_in_arg_string(arg_string: str) -> bool:
    """
    >>> assert is_doctest_in_arg_string('test') == False
    >>> assert is_doctest_in_arg_string('test/docrunner.py::::test')
    >>> assert is_doctest_in_arg_string('test/pytest.py::::test')
    """
    arg_string = arg_string.replace("\\", "/")
    if ("docrunner.py" in arg_string) or ("pytest.py" in arg_string) or ("/pytest/__main__.py" in arg_string):
        return True
    else:
        return False


# add_path_to_syspath{{{
def add_path_to_syspath(path_to_append: PathLikeOrString) -> None:
    """
    adds a path to the syspath

    Parameter
    ----------
    path_to_append
        the path to append - will be resolved by this function and added to syspath
        if path_to_append is a file, its parent directory will be added.


    Result
    ----------
    none


    Exceptions
    ----------
    none


    Examples
    ----------

    >>> add_path_to_syspath(pathlib.Path(__file__).parent)
    >>> path1 = str(sys.path)
    >>> add_path_to_syspath(pathlib.Path(__file__))
    >>> path2 = str(sys.path)
    >>> assert path1 == path2
    """
    # add_path_to_syspath}}}
    path_to_append = pathlib.Path(path_to_append).resolve()
    if path_to_append.is_file():
        path_to_append = path_to_append.parent
    sys_paths_resolved = [pathlib.Path(path).resolve() for path in sys.path]
    if path_to_append not in sys_paths_resolved:
        sys.path.append(str(path_to_append))


if __name__ == "__main__":
    print(b'this is a library only, the executable is named "lib_detect_testenv_cli.py"', file=sys.stderr)
