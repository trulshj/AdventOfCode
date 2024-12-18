namespace AdventOfCode.Helpers;

public sealed class Coordinate(int y, int x) : IEquatable<Coordinate>
{
    public static readonly Coordinate RightDelta = new(0, 1);
    public static readonly Coordinate LeftDelta = new(0, -1);
    public static readonly Coordinate UpDelta = new(-1, 0);
    public static readonly Coordinate DownDelta = new(1, 0);
    public static readonly Coordinate[] OrthogonalDeltas = [UpDelta, DownDelta, LeftDelta, RightDelta];
    public static readonly Coordinate Zero = new(0, 0);

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

    public bool IsZero()
    {
        return X == 0 && Y == 0;
    }

    public int ManhattanDistance(Coordinate other)
    {
        return Math.Abs(X - other.X) + Math.Abs(Y - other.Y);
    }

    public Coordinate Reverse()
    {
        return new Coordinate(-Y, -X);
    }

    public bool WithinBounds(int height, int width)
    {
        return Y >= 0 && Y < height && X >= 0 && X < width;
    }

    // ReSharper disable once MemberCanBePrivate.Global
    public bool WithinBounds(int minY, int maxY, int minX, int maxX)
    {
        return Y >= minY && Y <= maxY && X >= minX && X <= maxX;
    }

    public bool WithinBounds((int minY, int maxY, int minX, int maxX) bounds)
    {
        return WithinBounds(bounds.minY, bounds.maxY, bounds.minX, bounds.maxX);
    }

    public bool WithinBounds(Coordinate topLeft, Coordinate bottomRight)
    {
        return WithinBounds(topLeft.Y, bottomRight.Y, topLeft.X, bottomRight.X);
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

    public static Coordinate operator *(Coordinate a, int b)
    {
        return new Coordinate(a.Y * b, a.X * b);
    }

    public static Coordinate operator *(int a, Coordinate b)
    {
        return new Coordinate(b.Y * a, b.X * a);
    }

    public override int GetHashCode()
    {
        return HashCode.Combine(Y, X);
    }

    public override string ToString()
    {
        return $"({Y}, {X})";
    }
}