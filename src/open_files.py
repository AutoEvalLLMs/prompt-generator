from contextlib import contextmanager

@contextmanager
def open_file(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

# Example usage:
#with open_file('file') as f:
    #contents = f.read()