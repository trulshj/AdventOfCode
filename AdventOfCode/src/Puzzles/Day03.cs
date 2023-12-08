using AdventOfCode.Helpers;

namespace AdventOfCode.Puzzles;

public class Day03 : BaseDay
{
    private const string Numbers = "1234567890";
    private const string NotSymbols = "1234567890.";

    private Matrix<char> Grid { get; set; } = null!;

    private List<Symbol> Symbols { get; } = new();

    public override object SolvePart1()
    {
        Grid = new Matrix<char>(InputFileAsLines.Select(line => line.ToCharArray()).ToArray());

        Symbols.AddRange(Grid.GetCoordinatesAndValues(x => !NotSymbols.Contains(x))
            .Select(x => new Symbol(x.value, x.coordinate)));

        var visited = new HashSet<Coordinate>();

        return Symbols.Select(symbol =>
                Grid.GetNeighbors(symbol.Coord)
                    .Where(coordinate => Numbers.Contains(Grid[coordinate]) && !visited.Contains(coordinate))
                    .Select(coordinate => ScanNumber(coordinate, visited)).Sum())
            .Sum();
    }

    public override object SolvePart2()
    {
        var visited = new HashSet<Coordinate>();

        return Symbols
            .Where(symbol => symbol.Value == '*')
            .Select(symbol =>
                Grid.GetNeighbors(symbol.Coord)
                    .Where(coordinate => Numbers.Contains(Grid[coordinate]) && !visited.Contains(coordinate))
                    .Select(coordinate => ScanNumber(coordinate, visited)).ToArray())
            .Where(numbers => numbers.Length == 2)
            .Select(numbers => numbers[0] * numbers[1])
            .Sum();
    }

    private int ScanNumber(Coordinate start, ISet<Coordinate> visited)
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