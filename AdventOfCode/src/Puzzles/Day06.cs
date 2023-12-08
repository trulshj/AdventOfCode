using System.Text.RegularExpressions;

namespace AdventOfCode.Puzzles;

public partial class Day06 : BaseDay
{
    private long[] Times { get; set; } = Array.Empty<long>();
    private long[] Distances { get; set; } = Array.Empty<long>();

    private void ParseInput()
    {
        var numberLines = InputFileAsLines
            .Select(line => Numbers().Matches(line)
                .Select(match => long.Parse(match.Value))
                .ToArray())
            .ToArray();

        Times = numberLines[0];
        Distances = numberLines[1];
    }

    private static long FindPossibleStarts(long time, long distanceToBeat)
    {
        var lowerBound = (long)Math.Floor((time - Math.Sqrt(time * time - 4L * distanceToBeat)) / 2L) + 1L;
        return time - lowerBound - lowerBound + 1L;
    }

    public override object SolvePart1()
    {
        ParseInput();

        return (int)Times
            .Zip(Distances)
            .Select(x => FindPossibleStarts(x.First, x.Second))
            .Aggregate(1L, (acc, x) => acc * x);
    }

    public override object SolvePart2()
    {
        var time = long.Parse(string.Join("", Times));
        var distanceToBeat = long.Parse(string.Join("", Distances));

        return (int)FindPossibleStarts(time, distanceToBeat);
    }

    [GeneratedRegex(@"(\d+)")]
    private static partial Regex Numbers();
}