using AdventOfCode.Helpers;

namespace AdventOfCode.Tests;

public class MathElfTests
{
    [Theory]
    [InlineData(new[] { 1, 1, 1 }, 1)]
    [InlineData(new[] { 1, 2, 3 }, 6)]
    [InlineData(new[] { 2, 4, 6 }, 12)]
    [InlineData(new[] { 2, 3, 5 }, 30)]
    [InlineData(new[] { 3, 5, 7 }, 105)]
    [InlineData(new[] { 2, 3, 4 }, 12)]
    [InlineData(new[] { 2, 3, 6 }, 6)]
    public void Lcm_ShouldReturnCorrectResult(int[] numbers, int expected)
    {
        var actual = numbers.Aggregate(MathElf.Lcm);
        Assert.Equal(expected, actual);
    }
}