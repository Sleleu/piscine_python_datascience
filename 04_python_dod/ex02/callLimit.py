def callLimit(limit: int):
    """
    Decorator factory that creates a decorator to
    limit the number of calls to a function.

    Args:
    - limit (int): The maximum number of times the decorated
                   function can be called.

    Returns:
    - callLimiter (function): A decorator that limits the number of
                              calls to the function it decorates.
    """
    count = 0

    def callLimiter(function):
        """
        Decorator that limits the number of calls to the decorated function.

        Args:
        - The function to be decorated and its call limited.
        """

        def limit_function(*args: any, **kwds: any):
            """
            Wrapper function that checks call counts.

            Args:
            - *args: Variable length argument list.
            - **kwds: Arbitrary keyword arguments.
            """
            nonlocal count
            count += 1
            if count <= limit:
                return function()
            else:
                f_name = function.__name__
                f_id = hex(id(function))
                print(f"Error: {f_name} at {f_id} call too many times")
        return limit_function
    return callLimiter
