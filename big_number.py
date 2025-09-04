class BigNumber:
    
    
    #########################################################
    #                                                       #
    # Class capable of handling vaues up to 1x10^10^MAX_INT #
    #                                                       #
    #########################################################
    
    
    def __init__(self, mantissa: float = 0, exponent: int = 0):
        if mantissa == 0:
            self.mantissa = 0
            self.exponent = 0
            return

        while abs(mantissa) >= 10:
            mantissa /= 10
            exponent += 1
        while 0 < abs(mantissa) < 1:
            mantissa *= 10
            exponent -= 1

        self.mantissa = mantissa
        self.exponent = exponent

    def __repr__(self):
        return f"BigNumber({self.mantissa} x 10^{self.exponent})"

    # Safe float conversion (may overflow)
    def __float__(self):
        try:
            return float(self.mantissa * (10 ** self.exponent))
        except OverflowError:
            return float('inf') if self.mantissa > 0 else float('-inf')

    # Safe int conversion (may overflow)
    def __int__(self):
        try:
            return int(self.mantissa * (10 ** self.exponent))
        except OverflowError:
            raise OverflowError("BigNumber too large for int() conversion")

    # Formatted string representation
    def getNumber(self) -> str:
        if self.exponent < 6:
            ret = int(self.mantissa * (10 ** self.exponent))
            return f'{ret:,}'
        return f"{self.mantissa:.2f}e{self.exponent:,}"

    # Addition
    def __add__(self, other):
        if not isinstance(other, BigNumber):
            other = BigNumber(other)
        m1, e1 = self.mantissa, self.exponent
        m2, e2 = other.mantissa, other.exponent

        # Align exponents safely
        if abs(e1 - e2) > 20:
            # Small number negligible compared to huge exponent
            new_mantissa = m1 if e1 > e2 else m2
            result_exp = max(e1, e2)
        else:
            if e1 > e2:
                m2 /= 10 ** (e1 - e2)
                result_exp = e1
            else:
                m1 /= 10 ** (e2 - e1)
                result_exp = e2
            new_mantissa = m1 + m2

        return BigNumber(new_mantissa, result_exp)

    def __radd__(self, other):
        return self.__add__(other)

    # Subtraction
    def __sub__(self, other):
        if not isinstance(other, BigNumber):
            other = BigNumber(other)
        return self + BigNumber(-other.mantissa, other.exponent)

    def __rsub__(self, other):
        if not isinstance(other, BigNumber):
            other = BigNumber(other)
        return other - self

    # Multiplication
    def __mul__(self, other):
        if not isinstance(other, BigNumber):
            other = BigNumber(other)
        return BigNumber(self.mantissa * other.mantissa,
                         self.exponent + other.exponent)

    def __rmul__(self, other):
        return self.__mul__(other)

    # Division
    def __truediv__(self, other):
        if not isinstance(other, BigNumber):
            other = BigNumber(other)
        return BigNumber(self.mantissa / other.mantissa,
                         self.exponent - other.exponent)

    def __rtruediv__(self, other):
        if not isinstance(other, BigNumber):
            other = BigNumber(other)
        return other / self
    

def run_tests():
    # --- Casting -------------------------------------------------
    a = BigNumber(12345, 2)   # normalized -> 1.2345 × 10^6
    assert int(a) == 1_234_500
    assert abs(float(a) - 1.2345e6) < 1e-9

    # --- Output formatting ---------------------------------------
    small = BigNumber(100000, 0)   # becomes 1.0 × 10^5
    assert small.getNumber() == "100,000"      # exponent < 6
    big = BigNumber(1_000_000, 0)  # becomes 1.0 × 10^6
    assert big.getNumber().endswith("e6")     # exponent ≥ 6

    # --- Addition / Subtraction ----------------------------------
    x = BigNumber(2.5, 3)    # 2500
    y = BigNumber(5.0, 2)    # 500
    s = x + y
    assert abs(float(s) - 3000) < 1e-9

    d = x - y
    assert abs(float(d) - 2000) < 1e-9

    # reflected
    r1 = 100 - x   # __rsub__
    assert abs(float(r1) - (100 - 2500)) < 1e-9

    r2 = 100 + x   # __radd__
    assert abs(float(r2) - (100 + 2500)) < 1e-9

    # --- Multiplication / Division --------------------------------
    m = x * y
    assert abs(float(m) - (2500 * 500)) < 1e-9

    div1 = x / y
    assert abs(float(div1) - (2500 / 500)) < 1e-9

    div2 = 5000 / x   # __rtruediv__
    assert abs(float(div2) - (5000 / 2500)) < 1e-9

    # --- Edge cases -----------------------------------------------
    zero = BigNumber()
    assert int(zero) == 0
    assert float(zero) == 0.0

    tiny = BigNumber(0.00045)       # should normalize up
    assert abs(float(tiny) - 0.00045) < 1e-12

    neg = BigNumber(-12345)         # negative mantissa handled
    assert int(neg) == -12345

    print("✅ All tests passed!")

if __name__ == "__main__":
    from os import system
    system("cls")
    
    run_tests()