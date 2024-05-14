try:
    # code that may raise an exception
except Exception as e:
    # log the exception
    print(f"An error occurred: {e}")
    # optionally, re-raise the exception if you want it to propagate
    raise
