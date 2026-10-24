# Here are my calculator's functions

def add(num1, num2) :
    return num1 + num2

def subtract(num1, num2) :
    return num1 - num2

def multiply(num1, num2) :
    return num1 * num2

def divide(num1, num2) :
    if num2 == 0:
        raise ValueError("تقسیم بر صفر مجاز نیست.")
    return num1 / num2

def power(num1, num2):
    # 0 to a negative power means dividing by zero
    if num1 == 0 and num2 < 0:
        raise ValueError("صفر به توان منفی تعریف نشده است")

    # A negative base with a non-integer power gives a complex number
    if num1 < 0 and not float(num2).is_integer():
        raise ValueError("پایه‌ی منفی با توان غیرصحیح پشتیبانی نمی‌شود")

    return num1 ** num2

def C_to_K(value) :
    return value + 273.15

def K_to_C(value) :
    return value - 273.15

def C_to_F(value) :
    return value * 1.8 + 32

def F_to_C(value) :
    return (value-32) / 1.8

def K_to_F(value) :
    c = K_to_C(value)
    return C_to_F(c)

def F_to_K(value) :
    c = F_to_C(value)
    return C_to_K(c)