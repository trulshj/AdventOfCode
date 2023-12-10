namespace AdventOfCode.Helpers;

public sealed class Coordinate(int y, int x) : IEquatable<Coordinate>
{
    public int X { get; } = x;
    public int Y { get; } = y;

    public bool Equals(Coordinate? other)
    {
        if (ReferenceEquals(null, other)) return false;
        if (ReferenceEquals(this, other)) return true;
        return X == other.X && Y == other.Y;
    }

    public override bool Equals(object? obj)
    {
        if (ReferenceEquals(null, obj)) return false;
        if (ReferenceEquals(this, obj)) return true;
        return obj.GetType() == GetType() && Equals((Coordinate)obj);
    }


    public bool WithinBounds(int height, int width)
    {
        return Y >= 0 && Y < height && X >= 0 && X < width;
    }

    public bool WithinBounds(int minY, int maxY, int minX, int maxX)
    {
        return Y >= minY && Y <= maxY && X >= minX && X <= maxX;
    }

    public bool WithinBounds((int minY, int maxY, int minX, int maxX) bounds)
    {
        return WithinBounds(bounds.minY, bounds.maxY, bounds.minX, bounds.maxX);
    }

    public static Coordinate operator +(Coordinate a, Coordinate b)
    {
        return new Coordinate(a.Y + b.Y, a.X + b.X);
    }

    public static bool operator ==(Coordinate a, Coordinate b)
    {
        return a.Equals(b);
    }

    public static bool operator !=(Coordinate a, Coordinate b)
    {
        return !a.Equals(b);
    }

    public override int GetHashCode()
    {
        return HashCode.Combine(Y, X);
    }
}