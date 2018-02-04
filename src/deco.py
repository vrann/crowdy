"""
Stores lambda function decorator for wrapping lambda functions,
minimizing duplicated code
"""
import json


codes = {
    KeyError: 404,
    ValueError: 400
}


def aws_lambda(f):
    """
    Wraps passed function, catching common exceptions to reduce code
    duplication.
    Also provides a default success response code for when return value
    is None.

    status codes for common exceptions:
        ValueError: 400
        KeyError: 404

    :param f: callable
    :return: callable wrapper
    """
    def wrapper(event, context):
        try:
            # if no return value is given by wrapped func,
            # return default status code 200 response.
            r = f(event, context)
            if r is None:
                r = {
                    'statusCode': 200,
                    'body': json.dumps({'input': event})
                }
            return r
        except Exception as e:
            # if exception is thrown, return exception text,
            # and return status code associated with passed
            # exception type
            exc_type = type(e)
            if exc_type is type:
                exc_type = e
                msg = e.__name__
            else:
                msg = str(e)
            # get default exception code for raised Exception.
            # default to code 500 if exception is not in codes dict.
            code = codes.get(exc_type, 500)
            return {
                'statusCode': code,
                'body': json.dumps({'input': event, 'message': msg})
            }

    wrapper.__name__ = f.__name__ + '_wrapper'
    return wrapper
