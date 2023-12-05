using AdventOfCode.Helpers;

namespace AdventOfCode.Tests;

public class LongRangeTests
{
    [Fact]
    public void Shift_Forwards()
    {
        var range = new LongRange(0, 10);
        var shifted = range.Shift(5);

        Assert.Equal(5, shifted.Start);
        Assert.Equal(10, shifted.Length);
    }

    [Fact]
    public void Shift_Backwards()
    {
        var range = new LongRange(5, 10);
        var shifted = range.Shift(-5);

        Assert.Equal(0, shifted.Start);
        Assert.Equal(10, shifted.Length);
    }

    [Fact]
    public void Overlap_WithStart()
    {
        var range = new LongRange(0, 10);
        var other = new LongRange(5, 15);

        Assert.True(range.Overlaps(other));
        Assert.True(other.Overlaps(range));
    }

    [Fact]
    public void Overlap_WithEnd()
    {
        var range = new LongRange(5, 15);
        var other = new LongRange(0, 10);

        Assert.True(range.Overlaps(other));
        Assert.True(other.Overlaps(range));
    }

    [Fact]
    public void Overlap_WithStartAndEnd()
    {
        var range = new LongRange(0, 15);
        var other = new LongRange(5, 10);

        Assert.True(range.Overlaps(other));
        Assert.True(other.Overlaps(range));
    }

    [Fact]
    public void Intersection_WithStart()
    {
        var range = new LongRange(0, 10);
        var other = new LongRange(5, 10);

        var intersection = range.Intersection(other);

        Assert.NotNull(intersection);
        Assert.Equal(5, intersection.Start);
        Assert.Equal(5, intersection.Length);
    }

    [Fact]
    public void Intersection_WithEnd()
    {
        var range = new LongRange(5, 10);
        var other = new LongRange(0, 10);

        var intersection = range.Intersection(other);

        Assert.NotNull(intersection);
        Assert.Equal(5, intersection.Start);
        Assert.Equal(5, intersection.Length);
    }

    [Fact]
    public void Intersection_WithStartAndEnd()
    {
        var range = new LongRange(0, 20);
        var other = new LongRange(5, 10);

        var intersection = range.Intersection(other);

        Assert.NotNull(intersection);
        Assert.Equal(5, intersection.Start);
        Assert.Equal(10, intersection.Length);
    }

    [Fact]
    public void Intersection_WithNoOverlap()
    {
        var range = new LongRange(0, 10);
        var other = new LongRange(15, 10);

        var intersection = range.Intersection(other);

        Assert.Null(intersection);
    }

    [Fact]
    public void TryMerge_WithNoOverlap()
    {
        var ranges = new List<LongRange>
        {
            new(0, 10),
            new(15, 10),
            new(30, 10)
        };

        var merged = LongRange.Merge(ranges);

        Assert.Equal(3, merged.Count);
        Assert.Equal(0, merged[0].Start);
        Assert.Equal(10, merged[0].Length);
        Assert.Equal(15, merged[1].Start);
        Assert.Equal(10, merged[1].Length);
        Assert.Equal(30, merged[2].Start);
        Assert.Equal(10, merged[2].Length);
    }

    [Fact]
    public void TryMerge_WithOverlap()
    {
        var ranges = new List<LongRange>
        {
            new(0, 10),
            new(5, 10),
            new(30, 10)
        };

        var merged = LongRange.Merge(ranges);

        Assert.Equal(2, merged.Count);
        Assert.Equal(0, merged[0].Start);
        Assert.Equal(15, merged[0].Length);
        Assert.Equal(30, merged[1].Start);
        Assert.Equal(10, merged[1].Length);
    }

    [Fact]
    public void TryMerge_WithOverlapAndGaps()
    {
        var ranges = new List<LongRange>
        {
            new(0, 10),
            new(5, 10),
            new(30, 10),
            new(20, 10)
        };

        var merged = LongRange.Merge(ranges);

        Assert.Equal(2, merged.Count);
        Assert.Equal(0, merged[0].Start);
        Assert.Equal(15, merged[0].Length);
        Assert.Equal(20, merged[1].Start);
        Assert.Equal(20, merged[1].Length);
    }

    [Fact]
    public void TryMerge_CompletelyOverlapping()
    {
        var ranges = new List<LongRange>
        {
            new(1, 10),
            new(11, 10),
            new(21, 10)
        };

        var merged = LongRange.Merge(ranges);

        Assert.Single(merged);
        Assert.Equal(1, merged[0].Start);
        Assert.Equal(30, merged[0].Length);
    }

    [Fact]
    public void TryMerge_Identical()
    {
        var ranges = new List<LongRange>
        {
            new(1, 10),
            new(1, 10),
            new(1, 10)
        };

        var merged = LongRange.Merge(ranges);

        Assert.Single(merged);
        Assert.Equal(1, merged[0].Start);
        Assert.Equal(10, merged[0].Length);
    }

    [Theory]
    [InlineData(0L, 5L, 3L, 4L, 0L, 2L, 3L, 4L, 5L, 5L)]
    [InlineData(0L, 5L, 3L, 6L, 0L, 2L, 3L, 5L, null, null)]
    [InlineData(0L, 5L, 6L, 7L, 0L, 5L, null, null, null, null)]
    [InlineData(0L, 5L, 0L, 7L, null, null, 0L, 5L, null, null)]
    [InlineData(0L, 5L, 0L, 4L, null, null, 0L, 4L, 5L, 5L)]
    [InlineData(79L, 92L, 98L, 99L, 79L, 92L, null, null, null, null)]
    public void GetSegments(long thisStart, long thisEnd, long otherStart, long otherEnd, long? underflowStart,
        long? underflowEnd, long? overlapStart, long? overlapEnd, long? overflowStart, long? overflowEnd)
    {
        var @this = new LongRange(thisStart, thisEnd - thisStart + 1L);
        var other = new LongRange(otherStart, otherEnd - otherStart + 1L);

        var (underflow, overlap, overflow) = @this.GetSegments(other);

        if (underflowStart is null)
        {
            Assert.Null(underflow);
        }
        else
        {
            Assert.Equal(underflowStart, underflow!.Start);
            Assert.Equal(underflowEnd, underflow.End);
        }

        if (overlapStart is null)
        {
            Assert.Null(overlap);
        }
        else
        {
            Assert.Equal(overlapStart, overlap!.Start);
            Assert.Equal(overlapEnd, overlap.End);
        }

        if (overflowStart is null)
        {
            Assert.Null(overflow);
        }
        else
        {
            Assert.Equal(overflowStart, overflow!.Start);
            Assert.Equal(overflowEnd, overflow.End);
        }
    }
}