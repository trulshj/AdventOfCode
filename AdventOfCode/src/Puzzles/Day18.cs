using System.Globalization;
using AdventOfCode.Engines;

namespace AdventOfCode.Puzzles;

public class Day18 : BaseDay
{
    private (char direction, long distance, string color)[] Instructions { get; set; } = [];

    protected override void ParseInput()
    {
        Instructions = InputFileAsLines.Select(x => x.Split(' ')).Select(x => (x[0][0], long.Parse(x[1]), x[2]))
            .ToArray();
    }

    protected override object SolvePartOne()
    {
        (long y, long x) currentCoordinate = (0L, 0L);
        List<(long y, long x)> coordinates = [currentCoordinate];

        foreach (var (direction, distance, _) in Instructions)
        {
            var delta = GetDelta(direction);
            currentCoordinate = (currentCoordinate.y + delta.y * distance,
                currentCoordinate.x + delta.x * distance);
            coordinates.Add(currentCoordinate);
        }

        return FindArea(coordinates);
    }

    protected override object SolvePartTwo()
    {
        (long y, long x) currentCoordinate = (0L, 0L);
        List<(long y, long x)> coordinates = [currentCoordinate];

        foreach (var (_, _, color) in Instructions)
        {
            var distance = long.Parse(color[2..^2], NumberStyles.HexNumber);
            var direction = color[^2] switch
            {
                '0' => 'R',
                '1' => 'D',
                '2' => 'L',
                '3' => 'U',
                _ => throw new InvalidActionException("Invalid color")
            };

            var delta = GetDelta(direction);
            currentCoordinate = (currentCoordinate.y + delta.y * distance,
                currentCoordinate.x + delta.x * distance);
            coordinates.Add(currentCoordinate);
        }

        return FindArea(coordinates);
    }

    private static (long y, long x) GetDelta(char direction)
    {
        return direction switch
        {
            'U' => (-1, 0),
            'D' => (1, 0),
            'L' => (0, -1),
            'R' => (0, 1),
            _ => throw new InvalidActionException("Invalid direction")
        };
    }

    // calculate area using shoelace formula + pick's theorem
    private static long FindArea(IReadOnlyList<(long y, long x)> coordinates)
    {
        var area = 0L;
        var boundary = 0L;
        for (var i = 0; i < coordinates.Count - 1; i++)
        {
            area += coordinates[i].x * coordinates[i + 1].y - coordinates[i + 1].x * coordinates[i].y;
            boundary += Math.Abs(coordinates[i].x - coordinates[i + 1].x) +
                        Math.Abs(coordinates[i].y - coordinates[i + 1].y);
        }

        return (Math.Abs(area) + boundary) / 2L + 1L;
    }
}