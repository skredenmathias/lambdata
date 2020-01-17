import string
import numpy as numpy

def increment(x):
    """increments x by 1"""
    return(x + 1)

def strip_punctuation(text):
    """strips punctuation"""
    exclude = string.punctuation
    return ''.join(s for s in text if s not in exclude)

