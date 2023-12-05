namespace AdventOfCode.Extensions;

public static class StringManipulation
{
    public static string ReverseX(this string input)
    {
        return new string(input.Reverse().ToArray());
    }
}