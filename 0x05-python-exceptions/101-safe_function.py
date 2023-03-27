#!/usr/bin/python3


def safe_function(fct, *args):
    """Execute a function safely.

    Args:
        fct (function): The function to execute.
        args (tuple): The arguments to pass to the function.

    Returns:
        The return value of the function, or None if an exception occurs.
    """
    try:
        return (fct(*args))
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
    