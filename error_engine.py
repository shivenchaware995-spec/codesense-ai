import traceback


def explain_error(error):
    """
    Takes a Python error and returns a beginner-friendly explanation.
    """

    error_type = type(error).__name__
    error_message = str(error)

    explanations = {
        "NameError": {
            "meaning": "Python cannot find the variable or function you used.",
            "fix": "Check the spelling or define the variable before using it.",
            "example": "x = 10\nprint(x)"
        },

        "SyntaxError": {
            "meaning": "Python found invalid Python syntax.",
            "fix": "Check brackets, colons, quotes and indentation.",
            "example": "if x > 5:\n    print(x)"
        },

        "TypeError": {
            "meaning": "You are using an operation with an incompatible data type.",
            "fix": "Check the types of the values you are using.",
            "example": 'age = 20\nprint("Age:", age)'
        },

        "IndexError": {
            "meaning": "You tried to access a list position that does not exist.",
            "fix": "Check the list length and make sure the index is valid.",
            "example": "numbers = [10, 20, 30]\nprint(numbers[2])"
        },

        "KeyError": {
            "meaning": "The dictionary key you requested does not exist.",
            "fix": "Check the key name or use .get() safely.",
            "example": 'student = {"name": "Rahul"}\nprint(student.get("age"))'
        },

        "ModuleNotFoundError": {
            "meaning": "Python cannot find the module/library you are trying to import.",
            "fix": "Install the package using pip or check the package name.",
            "example": "pip install pandas"
        },

        "FileNotFoundError": {
            "meaning": "Python cannot find the file at the specified location.",
            "fix": "Check the filename and file path.",
            "example": 'open("data.txt", "r")'
        },

        "ZeroDivisionError": {
            "meaning": "You tried to divide a number by zero.",
            "fix": "Make sure the denominator is not zero.",
            "example": "a = 10\nb = 2\nprint(a / b)"
        },

        "IndentationError": {
            "meaning": "Python found incorrect indentation.",
            "fix": "Use consistent spaces or tabs. Prefer 4 spaces.",
            "example": 'if True:\n    print("Hello")'
        }
    }

    if error_type in explanations:
        info = explanations[error_type]

        return {
            "type": error_type,
            "message": error_message,
            "meaning": info["meaning"],
            "fix": info["fix"],
            "example": info["example"]
        }

    return {
        "type": error_type,
        "message": error_message,
        "meaning": "This error is not currently in the beginner error database.",
        "fix": "Check the error message and traceback for more information.",
        "example": "Search for the exact error message."
    }


def run_code(code):
    """
    Runs Python code and captures errors.
    """

    try:
        exec(code)

        return {
            "success": True,
            "error": None
        }

    except Exception as error:
        return {
            "success": False,
            "error": error
        }