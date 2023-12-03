namespace AdventOfCode.Helpers;

public class Matrix<T>
{
    private readonly T[][] _matrix;

    public Matrix(T[][] matrix)
    {
        _matrix = matrix;
    }

    public int Height => _matrix.Length;
    public int Width => _matrix[0].Length;

    public T[] this[int y]
    {
        get => _matrix[y];
        set => _matrix[y] = value;
    }

    public T this[Coordinate coord]
    {
        get => _matrix[coord.Y][coord.X];
        set => _matrix[coord.Y][coord.X] = value;
    }


    public T Get(Coordinate coord)
    {
        return _matrix[coord.Y][coord.X];
    }

    public T Get(int y, int x)
    {
        return _matrix[y][x];
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
            if (predicate(_matrix[y][x]))
                yield return new Coordinate(y, x);
    }

    public IEnumerable<(Coordinate, T)> GetCoordinatesAndValues()
    {
        for (var y = 0; y < Height; y++)
        for (var x = 0; x < Width; x++)
            yield return (new Coordinate(y, x), _matrix[y][x]);
    }

    public IEnumerable<(Coordinate coordinate, T value)> GetCoordinatesAndValues(Func<T, bool> predicate)
    {
        for (var y = 0; y < Height; y++)
        for (var x = 0; x < Width; x++)
            if (predicate(_matrix[y][x]))
                yield return (new Coordinate(y, x), _matrix[y][x]);
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

    public static Coordinate[] GetNeighbors<T>(this Matrix<T> matrix, Coordinate coord)
    {
        return Deltas.Select(x => x + coord).Where(matrix.WithinBounds).ToArray();
    }

    public static Coordinate[] GetOrthogonalNeighbors<T>(this Matrix<T> matrix, Coordinate coord)
    {
        return OrthogonalDeltas.Select(x => x + coord).Where(matrix.WithinBounds).ToArray();
    }
}