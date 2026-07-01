from flask import session
from flask import flash
from flask import redirect
from flask import url_for

from functools import wraps

def login_required(func):
    @wraps(func)

    def wrapper(*args, **kwargs):

        if not session.get("username"):

            flash(
                "Please login first!"
            )

            return redirect(
                url_for("student.login")
            )
        return func(
            *args,
            **kwargs
        )
    
    return wrapper