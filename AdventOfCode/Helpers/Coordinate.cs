namespace AdventOfCode.Helpers;

public class Coordinate
{
    public Coordinate(int y, int x)
    {
        Y = y;
        X = x;
    }

    public int X { get; }
    public int Y { get; }

    public bool WithinBounds(int height, int width)
    {
        return Y >= 0 && Y < height && X >= 0 && X < width;
    }

    public static Coordinate operator +(Coordinate a, Coordinate b)
    {
        return new Coordinate(a.Y + b.Y, a.X + b.X);
    }

    // HashSet
    public override bool Equals(object? obj)
    {
        if (obj is not Coordinate other)
            return false;

        return Y == other.Y && X == other.X;
    }

    // HashSet
    public override int GetHashCode()
    {
        return HashCode.Combine(Y, X);
    }
}