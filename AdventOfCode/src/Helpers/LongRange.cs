namespace AdventOfCode.Helpers;

public class LongRange
{
    public LongRange(long start, long length)
    {
        Start = start;
        Length = length;
    }

    public long Start { get; }
    public long Length { get; }

    public long End => Start + Length - 1;

    public LongRange Shift(long offset)
    {
        return new LongRange(Start + offset, Length);
    }

    public bool Contains(long value)
    {
        return value >= Start && value <= End;
    }

    public bool Overlaps(LongRange other)
    {
        return Contains(other.Start) || Contains(other.End) || other.Contains(Start) || other.Contains(End);
    }

    public bool OverlapsOrTouches(LongRange other)
    {
        return Contains(other.Start) || Contains(other.End) ||
               other.Contains(Start) || other.Contains(End) ||
               Start - 1 == other.End || End + 1 == other.Start;
    }

    public LongRange? Intersection(LongRange other)
    {
        if (!Overlaps(other)) return null;

        var startMax = Math.Max(Start, other.Start);
        var endMin = Math.Min(End, other.End);

        return startMax > endMin
            ? null
            : new LongRange(startMax, endMin - startMax + 1);
    }

    public override string ToString()
    {
        return $"[{Start} -> {End}]";
    }

    public static List<LongRange> Merge(IEnumerable<LongRange?> ranges)
    {
        var merged = new List<LongRange>();
        var sorted = ranges.Where(x => x is not null).Select(x => x!).OrderBy(r => r.Start).ToList();

        if (!sorted.Any()) return merged;

        var current = sorted[0];
        for (var i = 1; i < sorted.Count; i++)
        {
            var next = sorted[i];
            if (current.OverlapsOrTouches(next))
            {
                current = current.Union(next);
            }
            else
            {
                merged.Add(current);
                current = next;
            }
        }

        if (merged.Any() && merged.Last().OverlapsOrTouches(current))
            merged[^1] = merged.Last().Union(current);
        else
            merged.Add(current);

        return merged;
    }

    public (LongRange? underflow, LongRange? overlap, LongRange? overflow) GetSegments(LongRange other)
    {
        var overlap = Intersection(other);

        LongRange? underflow = null;
        if (Start < other.Start)
            underflow = overlap is null
                ? Copy()
                : new LongRange(Start, other.Start - Start);

        LongRange? overflow = null;
        if (End > other.End)
            overflow = overlap is null
                ? Copy()
                : new LongRange(other.End + 1, End - other.End);

        return (underflow, overlap, overflow);
    }

    public LongRange Copy()
    {
        return new LongRange(Start, Length);
    }

    private LongRange Union(LongRange other)
    {
        var start = Math.Min(Start, other.Start);
        var end = Math.Max(End, other.End);
        var length = end - start + 1;
        return new LongRange(start, length);
    }
}