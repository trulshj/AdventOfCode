using AdventOfCode.Helpers;

namespace AdventOfCode.Puzzles;

public class Day10 : BaseDay
{
    private static readonly Dictionary<char, Coordinate[]> Neighbors = new()
    {
        ['|'] = new[] { new Coordinate(-1, 0), new Coordinate(1, 0) },
        ['-'] = new[] { new Coordinate(0, -1), new Coordinate(0, 1) },
        ['L'] = new[] { new Coordinate(-1, 0), new Coordinate(0, 1) },
        ['J'] = new[] { new Coordinate(-1, 0), new Coordinate(0, -1) },
        ['7'] = new[] { new Coordinate(1, 0), new Coordinate(0, -1) },
        ['F'] = new[] { new Coordinate(1, 0), new Coordinate(0, 1) },
        ['.'] = Array.Empty<Coordinate>(),
        ['S'] = Array.Empty<Coordinate>()
    };

    private Matrix<char> Grid { get; set; } = null!;
    private HashSet<Coordinate> Loop { get; set; } = null!;

    private void ParseInput()
    {
        Grid = new Matrix<char>(InputFileAsLines.Select(line => line.ToList()).ToList());
    }

    private Coordinate[] GetNeighbors(Coordinate coordinate)
    {
        var pipe = Grid[coordinate];
        return Neighbors[pipe].Select(x => x + coordinate).Where(x => Grid.WithinBounds(x)).ToArray();
    }

    private HashSet<Coordinate>? Bfs(Coordinate start, Coordinate sCoordinate)
    {
        var visited = new HashSet<Coordinate>();
        var queue = new Queue<Coordinate>();

        queue.Enqueue(start);

        while (queue.Count > 0)
        {
            var coordinate = queue.Dequeue();

            visited.Add(coordinate);

            var neighbors = GetNeighbors(coordinate);
            foreach (var neighbor in neighbors)
            {
                if (neighbor == sCoordinate && visited.Contains(sCoordinate))
                    return visited;
                if (visited.Contains(neighbor)) continue;
                queue.Enqueue(neighbor);
            }
        }

        return null;
    }

    public override object SolvePart1()
    {
        ParseInput();

        var sCoordinate = Grid.GetCoordinatesAndValues(x => x == 'S').First().coordinate;

        Loop = Grid.GetOrthogonalNeighbors(sCoordinate).Select(start => Bfs(start, sCoordinate))
            .First(x => x is not null)!;

        return Loop.Count / 2;
    }

    public override object SolvePart2()
    {
        // Get bounding box of loop to avoid checking every coordinate
        var bounds = Loop.GetBounds();

        return Grid
            .GetCoordinates()
            .Where(x => !Loop.Contains(x) && x.WithinBounds(bounds))
            .Count(IsContainedByLoop);
    }

    private bool IsContainedByLoop(Coordinate coordinate)
    {
        var rightDelta = new Coordinate(0, 1);

        var currentCoordinate = coordinate;
        var topCrossings = 0;
        var bottomCrossings = 0;

        while (Grid.WithinBounds(currentCoordinate))
        {
            currentCoordinate += rightDelta;
            if (!Loop.Contains(currentCoordinate)) continue;

            if ("|LJ".Contains(Grid[currentCoordinate])) topCrossings++;

            if ("|7F".Contains(Grid[currentCoordinate])) bottomCrossings++;
        }

        return (topCrossings - bottomCrossings) % 2 == 0 && Math.Min(topCrossings, bottomCrossings) % 2 == 1;
    }
}