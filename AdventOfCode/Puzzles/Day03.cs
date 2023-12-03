using AdventOfCode.Helpers;

namespace AdventOfCode.Puzzles;

public class Day03 : BaseDay
{
    private const string Numbers = "1234567890";
    private const string NotSymbols = "1234567890.";

    private static readonly Coordinate[] Deltas =
    {
        new(-1, -1), new(-1, 0), new(-1, 1),
        new(0, -1), new(0, 1),
        new(1, -1), new(1, 0), new(1, 1)
    };

    private Matrix2D<char> Grid { get; set; }

    private List<Symbol> Symbols { get; } = new();

    public override string SolvePart1Async()
    {
        Grid = new Matrix2D<char>(InputFileAsLines.Select(line => line.ToCharArray()).ToArray());

        var numbers = new List<int>();

        for (var y = 0; y < Grid.Height; y++)
        for (var x = 0; x < Grid.Width; x++)
            if (!NotSymbols.Contains(Grid[y][x]))
                Symbols.Add(new Symbol(Grid[y][x], new Coordinate(y, x)));

        foreach (var symbol in Symbols)
        {
            var visited = new HashSet<Coordinate>();

            foreach (var delta in Deltas)
            {
                var newCoord = symbol.Coord + delta;

                if (!Grid.WithinBounds(newCoord)) continue;

                if (!Numbers.Contains(Grid.Get(newCoord)) || visited.Contains(newCoord)) continue;

                numbers.Add(ScanNumber(newCoord, visited));
            }
        }

        return numbers.Sum().ToString();
    }

    public override string SolvePart2Async()
    {
        var sum = 0;
        var visited = new HashSet<Coordinate>();

        foreach (var symbol in Symbols)
        {
            if (symbol.Value != '*') continue;

            var numbers = new List<int>();

            foreach (var delta in Deltas)
            {
                var newCoord = symbol.Coord + delta;

                if (!Grid.WithinBounds(newCoord))
                    continue;

                if (!Numbers.Contains(Grid[newCoord.Y][newCoord.X]) || visited.Contains(newCoord)) continue;

                numbers.Add(ScanNumber(newCoord, visited));
            }

            if (numbers.Count == 2)
                sum += numbers[0] * numbers[1];
        }

        return sum.ToString();
    }

    private int ScanNumber(Coordinate start, HashSet<Coordinate> visited)
    {
        var queue = new Queue<Coordinate>();
        queue.Enqueue(start);

        var number = "";
        var deltaLeft = new Coordinate(0, -1);
        var deltaRight = new Coordinate(0, 1);

        while (queue.Count > 0)
        {
            var c = queue.Dequeue();
            visited.Add(c);
            number = c.X <= start.X ? $"{Grid[c]}{number}" : $"{number}{Grid[c]}";

            var left = c + deltaLeft;
            var right = c + deltaRight;

            if (Grid.WithinBounds(left) && Numbers.Contains(Grid[left]) && !visited.Contains(left))
                queue.Enqueue(left);

            if (Grid.WithinBounds(right) && Numbers.Contains(Grid[right]) && !visited.Contains(right))
                queue.Enqueue(right);
        }

        return int.Parse(number);
    }

    private sealed record Symbol(char Value, Coordinate Coord);
}