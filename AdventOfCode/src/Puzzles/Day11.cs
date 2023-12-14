using AdventOfCode.Helpers;

namespace AdventOfCode.Puzzles;

public class Day11 : BaseDay
{
    private List<Coordinate> Galaxies { get; set; } = [];
    private int[] EmptyColumns { get; set; } = [];
    private int[] EmptyRows { get; set; } = [];

    protected override void ParseInput()
    {
        var space = new Matrix<char>(InputFileAsLines.Select(x => x.ToList()).ToList());
        EmptyColumns = space.GetColumnIndexes(x => x == '.').ToArray();
        EmptyRows = space.GetRowIndexes(x => x == '.').ToArray();
        Galaxies = space.GetCoordinates(x => x == '#').ToList();
    }

    protected override object SolvePartOne()
    {
        ParseInput();

        return GetDistances(2L);
    }

    protected override object SolvePartTwo()
    {
        return GetDistances(1_000_000L);
    }

    private long GetDistances(long expansionFactor)
    {
        var pathSum = 0L;

        var adjustedGalaxies = Galaxies.Select(x => (
            y: EmptyRows.Count(row => row < x.Y) * (expansionFactor - 1) + x.Y,
            x: EmptyColumns.Count(col => col < x.X) * (expansionFactor - 1) + x.X)
        ).ToList();

        for (var i = 0; i < Galaxies.Count - 1; i++)
        for (var j = i + 1; j < Galaxies.Count; j++)
        {
            var g1 = adjustedGalaxies[i];
            var g2 = adjustedGalaxies[j];

            pathSum += Math.Abs(g1.x - g2.x) + Math.Abs(g1.y - g2.y);
        }

        return pathSum;
    }
}