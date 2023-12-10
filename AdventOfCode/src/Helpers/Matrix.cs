namespace AdventOfCode.Helpers;

public class Matrix<T>(IList<T[]> matrix)
{
    public int Height => matrix.Count;
    public int Width => matrix[0].Length;

    public T[] this[int y]
    {
        get => matrix[y];
        set => matrix[y] = value;
    }

    public T this[Coordinate coord]
    {
        get => matrix[coord.Y][coord.X];
        set => matrix[coord.Y][coord.X] = value;
    }


    public T Get(Coordinate coord)
    {
        return matrix[coord.Y][coord.X];
    }

    public T Get(int y, int x)
    {
        return matrix[y][x];
    }

    public bool WithinBounds(Coordinate coord)
    {
        return coord.Y >= 0 && coord.Y < Height && coord.X >= 0 && coord.X < Width;
    }

    public IEnumerable<Coordinate> GetCoordinates()
    {
        for (var y = 0; y < Height; y++)
        for (var x = 0; x < Width; x++)
            yield return new Coordinate(y, x);
    }

    public IEnumerable<Coordinate> GetCoordinates(Func<T, bool> predicate)
    {
        for (var y = 0; y < Height; y++)
        for (var x = 0; x < Width; x++)
            if (predicate(matrix[y][x]))
                yield return new Coordinate(y, x);
    }

    public IEnumerable<Coordinate> GetCoordinates(Func<Coordinate, bool> predicate)
    {
        for (var y = 0; y < Height; y++)
        for (var x = 0; x < Width; x++)
            if (predicate(new Coordinate(y, x)))
                yield return new Coordinate(y, x);
    }

    public IEnumerable<Coordinate> GetCoordinates(Func<Coordinate, T, bool> predicate)
    {
        for (var y = 0; y < Height; y++)
        for (var x = 0; x < Width; x++)
            if (predicate(new Coordinate(y, x), matrix[y][x]))
                yield return new Coordinate(y, x);
    }

    public IEnumerable<(Coordinate coordinate, T value)> GetCoordinatesAndValues()
    {
        for (var y = 0; y < Height; y++)
        for (var x = 0; x < Width; x++)
            yield return (new Coordinate(y, x), matrix[y][x]);
    }

    public IEnumerable<(Coordinate coordinate, T value)> GetCoordinatesAndValues(Func<T, bool> predicate)
    {
        for (var y = 0; y < Height; y++)
        for (var x = 0; x < Width; x++)
            if (predicate(matrix[y][x]))
                yield return (new Coordinate(y, x), matrix[y][x]);
    }

    public IEnumerable<(Coordinate coordinate, T value)> GetCoordinatesAndValues(Func<Coordinate, bool> predicate)
    {
        for (var y = 0; y < Height; y++)
        for (var x = 0; x < Width; x++)
            if (predicate(new Coordinate(y, x)))
                yield return (new Coordinate(y, x), matrix[y][x]);
    }

    public IEnumerable<(Coordinate coordinate, T value)> GetCoordinatesAndValues(Func<Coordinate, T, bool> predicate)
    {
        for (var y = 0; y < Height; y++)
        for (var x = 0; x < Width; x++)
            if (predicate(new Coordinate(y, x), matrix[y][x]))
                yield return (new Coordinate(y, x), matrix[y][x]);
    }

    public new string ToString()
    {
        return string.Join("\n", matrix.Select(x => string.Join("", x)));
    }
}

public static class MatrixExtensions
{
    private static readonly Coordinate[] Deltas =
    {
        new(-1, -1), new(-1, 0), new(-1, 1),
        new(0, -1), new(0, 1),
        new(1, -1), new(1, 0), new(1, 1)
    };

    private static readonly Coordinate[] OrthogonalDeltas =
    {
        new(-1, 0),
        new(0, -1),
        new(0, 1),
        new(1, 0)
    };

    public static IEnumerable<Coordinate> GetNeighbors<T>(this Matrix<T> matrix, Coordinate coord)
    {
        return Deltas.Select(x => x + coord).Where(matrix.WithinBounds);
    }

    public static IEnumerable<Coordinate> GetOrthogonalNeighbors<T>(this Matrix<T> matrix, Coordinate coord)
    {
        return OrthogonalDeltas.Select(x => x + coord).Where(matrix.WithinBounds);
    }

    public static (int minY, int maxY, int minX, int maxX) GetBounds(this IEnumerable<Coordinate> coordinates)
    {
        var coordArray = coordinates.ToArray();

        var minY = coordArray.Min(x => x.Y);
        var maxY = coordArray.Max(x => x.Y);
        var minX = coordArray.Min(x => x.X);
        var maxX = coordArray.Max(x => x.X);

        return (minY, maxY, minX, maxX);
    }
}