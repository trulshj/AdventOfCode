using AdventOfCode.Extensions;

namespace AdventOfCode.Puzzles;

public class Day14 : BaseDay
{
    private string[] Grid { get; set; } = [];

    protected override void ParseInput()
    {
        Grid = InputFileAsLines.ToArray();
    }

    private static int CalculateLoad(IReadOnlyCollection<string> grid)
    {
        return grid.Select((t, i) => t.Count(x => x == 'O') * (grid.Count - i)).Sum();
    }

    private static string[] TiltGrid(IEnumerable<string> grid)
    {
        return grid.Select(x => string.Join('#', x.Split('#').Select(y => string.Concat(y.OrderBy(z => z))))).ToArray();
    }

    private static string[] Cycle(IEnumerable<string> grid)
    {
        for (var i = 0; i < 4; i++) grid = TiltGrid(grid.RotateRight());
        return grid.ToArray();
    }


    protected override object SolvePartOne()
    {
        var tiltedGrid = TiltGrid(Grid.RotateRight()).RotateLeft();

        return CalculateLoad(tiltedGrid);
    }

    protected override object SolvePartTwo()
    {
        var seenGrids = new HashSet<string> { string.Join("", Grid) };
        var grids = new List<string[]> { Grid };
        var cycleIndex = 0;
        var cycleStart = 0;

        var currentGrid = Grid;
        while (true)
        {
            currentGrid = Cycle(currentGrid);
            cycleIndex++;
            if (!seenGrids.Add(string.Join("", currentGrid)))
            {
                cycleStart = grids.FindIndex(x => x.SequenceEqual(currentGrid));
                grids.Add(currentGrid);
                break;
            }

            grids.Add(currentGrid);
        }

        var cycleLength = cycleIndex - cycleStart;
        var targetIndex = (1000000000 - cycleStart) % cycleLength + cycleStart;

        return CalculateLoad(grids[targetIndex]);
    }
}