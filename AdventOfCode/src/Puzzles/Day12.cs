namespace AdventOfCode.Puzzles;

public class Day12 : BaseDay
{
    private readonly Dictionary<(string, string), long> _cache = new();

    private Nonogram[] Nonograms { get; set; } = [];

    protected override void ParseInput()
    {
        Nonograms = InputFileAsLines.Select(x =>
        {
            var split = x.Split(" ");
            var pattern = split[0];
            var numbers = split[1].Split(",").Select(int.Parse).ToArray();
            return new Nonogram(pattern, numbers);
        }).ToArray();
    }

    private long GetArrangements(string pattern, int[] numbers)
    {
        if (pattern == "") // Have we managed to place all numbers?
            return numbers.Length == 0 ? 1L : 0L;

        if (numbers.Length == 0) // Did we run out of numbers?
            return pattern.Contains('#') ? 0L : 1L;

        var key = (pattern, string.Join(',', numbers));
        if (_cache.TryGetValue(key, out var value)) return value;

        var arrangements = 0L;

        if (pattern[0] is '.' or '?')
            arrangements += GetArrangements(pattern[1..], numbers);

        if (pattern[0] is not ('#' or '?'))
        {
            _cache[key] = arrangements;
            return arrangements;
        }

        var number = numbers[0];

        var isLongEnough = number <= pattern.Length;
        var isPlaceable = !pattern.Take(number).Contains('.');
        var isFitPossible = pattern.Length <= number || pattern[number] != '#';

        if (isLongEnough && isPlaceable && isFitPossible)
            arrangements += GetArrangements(string.Join("", pattern.Skip(number + 1)), numbers[1..]);

        _cache[key] = arrangements;
        return arrangements;
    }


    protected override object SolvePartOne()
    {
        ParseInput();

        return Nonograms.Sum(x => GetArrangements(x.Pattern, x.Numbers));
    }

    protected override object SolvePartTwo()
    {
        return Nonograms
            .Select(x => new Nonogram(
                string.Join('?', Enumerable.Repeat(x.Pattern, 5)),
                Enumerable.Repeat(0, 5).SelectMany(_ => x.Numbers).ToArray()
            ))
            .Sum(x => GetArrangements(x.Pattern, x.Numbers));
    }

    private sealed record Nonogram(string Pattern, int[] Numbers);
}