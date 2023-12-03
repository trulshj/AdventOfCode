namespace AdventOfCode.Helpers;

public class Matrix2D<T>
{
    private readonly T[][] _matrix;

    public Matrix2D(T[][] matrix)
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
}