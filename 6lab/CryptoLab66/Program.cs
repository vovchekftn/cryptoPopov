using System;
using System.Diagnostics;

namespace Init;
class Program
{
    private static void Main()
    {
        CallEuclidFunction();
        //CallBinaryExponentiation();
        //CallEulerTotient();
    }

    private static void CallEuclidFunction()
    {
        int a = 119;
        int b = 544;

        (int gcd, int x, int y) = ExtendedEuclid(a, b);
        Console.WriteLine($"gcd({a}, {b}) = {gcd}");
        Console.WriteLine($"Constants: x = {x}, y = {y}");
    }


    private static void CallBinaryExponentiation()
    {
        long baseNumber = 2;
        long exponent = 10;
        long result = BinaryExponentiation(baseNumber, exponent);
        Console.WriteLine($"{baseNumber}^{exponent} = {result}");
    }

    private static void CallEulerTotient()
    {
        int n = 36;
        Console.WriteLine($"Функція Ейлера для {n} = {EulerTotient(n)}");
    }

    private static long BinaryExponentiation(long baseNumber, long exponent)
    {
        long result = 1;
        while (exponent > 0)
        {
            if (exponent % 2 == 1)
            {
                result *= baseNumber;
            }
            baseNumber *= baseNumber;
            exponent /= 2;
        }
        return result;
    }

    private static (int, int, int) ExtendedEuclid(int a, int b)
    {
        if (b == 0)
            return (a, 1, 0);

        (int gcd, int x1, int y1) = ExtendedEuclid(b, a % b);

        int x = y1;
        int y = x1 - (a / b) * y1;

        return (gcd, x, y);
    }

    static int EulerTotient(int n)
    {
        if (n == 1) return 1;

        int result = n;
        for (int p = 2; p * p <= n; p++)
        {
            if (n % p == 0)
            {
                while (n % p == 0)
                {
                    n /= p;
                }
                result -= result / p;
            }
        }

        if (n > 1)
            result -= result / n;

        return result;
    }
}
