import math; import random
def ADD(x, y):
    a = x + y
    return a
def SUB(x, y):
    a = x - y
    return a
def MUL(x, y):
    a = x * y
    return a
def DIV(x, y):
    a = x / y
    return a
def FLR(x):
    a = math.floor(x)
    return a
def CEIL(x):
    a = math.ceil(x)
    return a
def SIN(x):
    a = math.sin(x)
    return a
def COS(x):
    a = math.cos(x)
    return a
def TAN(x):
    a = math.tan(x)
    return a
def PI(x):
    a = math.pi(x)
    return a
def PI2():
    a = math.pi()
    return a
def ASIN(x):
    a = math.asin(x)
    return a
def ASINH(x):
    a = math.asinh(x)
    return a
def ACOS(x):
    a = math.acos(x)
    return a
def ACOSH(x):
    a = math.acosh(x)
    return a
def ATAN(x):
    a = math.atan(x)
    return a
def ATAN2(x, y):
    a = math.atan2(x, y)
    return a
def TANH(x):
    a = math.tanh(x)
    return a
def COMB(x, y):
    a = math.comb(x, y)
    return a
def POW(x):
    a = math.pow(x)
    return a
def LOG(x):
    a = math.log(x)
    return a
def LOG10(x):
    a = math.log10(x)
    return a
def LOG1P(x):
    a = math.log10ps(x)
    return a
def COPY(x, y):
    a = math.copysign(x, y)
    return a
def DEG(x):
    a = math.degrees(x)
    return a
def E(x):
    a = math.e(x)
    return a
def E2():
    a = math.e()
    return a
def EXP(x):
    a = math.exp(x)
    return a
def EXPM1(x):
    a = math.expm1(x)
    return a
def FABS(x):
    a = math.fabs(x)
    return a
def FAC(x):
    a = math.factorial(x)
    return a
def FMOD(x, y):
    a = math.fmod(x, y)
    return a
def RAND():
    a = random.random()
    return a
def RINT32():
    a = random.randint(0x0, 0x7FFFFFFF)
    return a
def RINT64():
    #0x7FFFFFFFFFFFFFFF_MAX
    a = random.randint(0x0, 0x7FFFFFFFFFFFFFFF)
    return a
def RINTN64():
    #0x8000000000000000_MIN
    a = random.randint(0x0, 0x8000000000000000)
    return a
def RINTMX():
    #0x25E453D73E354D9E6B0CEC68ADE1E25CA42AD4CBC1CACD6D88...
    #idk maybe use it for a pass, but I don't think you'll remember it.
    #min version doesn't work tho :/
    import RINTMX
    a = random.randint(0x0, RINTMX.max)
    return a
def RINTN32():
    a = random.randint(0x0, 0xFFFFFFFF80000000)
    return a
def HEX(x):
    a = hex(x)
    return a



