using AdventOfCode.Helpers;

namespace AdventOfCode.Puzzles;

public class Day05 : BaseDay
{
    private Map[][] Categories { get; set; } = Array.Empty<Map[]>();
    private long[] Seeds { get; set; } = Array.Empty<long>();

    private void ParseInput()
    {
        var blocks = InputFileContents
            .Split("\n\n")
            .Select(block => block.Split("\n"))
            .ToArray();

        Seeds = blocks[0][0]
            .Split(": ")
            .Last()
            .Split(" ")
            .Select(long.Parse)
            .ToArray();

        Categories = blocks
            .Skip(1)
            .Select(x => x
                .Skip(1)
                .Select(y => y
                    .Split(' ')
                    .Select(long.Parse)
                    .ToArray())
                .Select(z => new Map(z[0] - z[1], new LongRange(z[1], z[2])))
                .ToArray()
            ).ToArray();
    }

    public override int SolvePart1()
    {
        ParseInput();

        var minimumLocation = long.MaxValue;

        foreach (var seed in Seeds)
        {
            var currentValue = seed;
            foreach (var category in Categories)
            foreach (var map in category)
            {
                if (!map.Range.Contains(currentValue)) continue;

                currentValue += map.Offset;
                break;
            }

            if (currentValue < minimumLocation)
                minimumLocation = currentValue;
        }

        return unchecked((int)minimumLocation);
    }

    public override int SolvePart2()
    {
        var seeds = new Stack<LongRange>(Seeds.Chunk(2).Select(x => new LongRange(x[0], x[1])));

        foreach (var category in Categories)
        {
            var mappedSeeds = new List<LongRange>();

            while (seeds.Count > 0)
            {
                var seed = seeds.Pop();
                var mapped = false;

                foreach (var map in category)
                {
                    var segments = seed.GetSegments(map.Range);
                    if (segments.overlap is null) continue;

                    mappedSeeds.Add(segments.overlap.Shift(map.Offset));

                    if (segments.underflow is not null) seeds.Push(segments.underflow);
                    if (segments.overflow is not null) seeds.Push(segments.overflow);

                    mapped = true;
                    break;
                }

                if (!mapped) mappedSeeds.Add(seed);
            }

            foreach (var mappedSeed in LongRange.Merge(mappedSeeds)) seeds.Push(mappedSeed);
        }

        return unchecked((int)seeds.Select(x => x.Start).Min());
    }

    private sealed record Map(long Offset, LongRange Range);
}