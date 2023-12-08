namespace AdventOfCode.Helpers;

public static class MathElf
{
    public static int Gcd(int a, int b)
    {
        while (b != 0)
        {
            var t = b;
            b = a % b;
            a = t;
        }

        return a;
    }

    public static int Lcm(int a, int b)
    {
        return Math.Abs(a * b) / Gcd(a, b);
    }

    public static long Gcd(long a, long b)
    {
        while (b != 0)
        {
            var t = b;
            b = a % b;
            a = t;
        }

        return a;
    }

    public static long Lcm(long a, long b)
    {
        return Math.Abs(a * b) / Gcd(a, b);
    }
}