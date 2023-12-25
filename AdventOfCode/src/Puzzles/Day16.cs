using AdventOfCode.Helpers;

namespace AdventOfCode.Puzzles;

public class Day16 : BaseDay
{
    private Matrix<char> Grid { get; set; } = null!;

    protected override void ParseInput()
    {
        Grid = new Matrix<char>(InputFileAsLines.Select(x => x.ToList()).ToList());
    }

    protected override object SolvePartOne()
    {
        return CalculateEnergized(new Coordinate(0, -1), Coordinate.RightDelta);
    }

    protected override object SolvePartTwo()
    {
        var maximumEnergized = 0;

        for (var y = 0; y < Grid.Height; y++)
        {
            // Try all edges from the left
            maximumEnergized = Math.Max(maximumEnergized,
                CalculateEnergized(new Coordinate(y, -1), Coordinate.RightDelta));

            // Try all edges from the right
            maximumEnergized = Math.Max(maximumEnergized,
                CalculateEnergized(new Coordinate(y, Grid.Width), Coordinate.LeftDelta));
        }

        for (var x = 0; x < Grid.Width; x++)
        {
            // Try all edges from the top
            maximumEnergized = Math.Max(maximumEnergized,
                CalculateEnergized(new Coordinate(-1, x), Coordinate.DownDelta));

            // Try all edges from the bottom
            maximumEnergized = Math.Max(maximumEnergized,
                CalculateEnergized(new Coordinate(Grid.Height, x), Coordinate.UpDelta));
        }

        return maximumEnergized;
    }

    private int CalculateEnergized(Coordinate startingPosition, Coordinate startingDelta)
    {
        HashSet<(Coordinate coordinate, Coordinate delta)> energizedCells = [];
        Queue<(Coordinate coordinate, Coordinate delta)> queue = [];

        queue.Enqueue((startingPosition, startingDelta));

        while (queue.Count > 0)
        {
            var (coordinate, delta) = queue.Dequeue();
            var currentCoordinate = coordinate + delta;

            if (!Grid.WithinBounds(currentCoordinate)) continue;

            var cell = Grid[currentCoordinate];

            if ((cell == '.' ||
                 (cell == '|' && (delta == Coordinate.UpDelta || delta == Coordinate.DownDelta)) ||
                 (cell == '-' && (delta == Coordinate.LeftDelta || delta == Coordinate.RightDelta))) &&
                energizedCells.Add((currentCoordinate, delta)))
            {
                queue.Enqueue((currentCoordinate, delta));
                continue;
            }

            switch (cell)
            {
                case '|' when delta == Coordinate.LeftDelta || delta == Coordinate.RightDelta:
                {
                    if (energizedCells.Add((currentCoordinate, Coordinate.UpDelta)))
                        queue.Enqueue((currentCoordinate, Coordinate.UpDelta));

                    if (energizedCells.Add((currentCoordinate, Coordinate.DownDelta)))
                        queue.Enqueue((currentCoordinate, Coordinate.DownDelta));

                    continue;
                }
                case '-' when delta == Coordinate.UpDelta || delta == Coordinate.DownDelta:
                {
                    if (energizedCells.Add((currentCoordinate, Coordinate.LeftDelta)))
                        queue.Enqueue((currentCoordinate, Coordinate.LeftDelta));

                    if (energizedCells.Add((currentCoordinate, Coordinate.RightDelta)))
                        queue.Enqueue((currentCoordinate, Coordinate.RightDelta));

                    continue;
                }
                case '/':
                    delta = new Coordinate(-delta.X, -delta.Y);
                    break;
                case '\\':
                    delta = new Coordinate(delta.X, delta.Y);
                    break;
            }

            if (energizedCells.Add((currentCoordinate, delta)))
                queue.Enqueue((currentCoordinate, delta));
        }

        return energizedCells.DistinctBy(x => x.coordinate).Count();
    }
}