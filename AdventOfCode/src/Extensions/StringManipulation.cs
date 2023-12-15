namespace AdventOfCode.Extensions;

public static class StringManipulation
{
    public static string ReverseX(this string input)
    {
        return new string(input.Reverse().ToArray());
    }

    public static string[] Transpose(this IEnumerable<string> _grid)
    {
        var grid = _grid.ToArray();
        return Enumerable.Range(0, grid[0].Length)
            .Select(i => string.Concat(grid.Select(row => row[i])))
            .ToArray();
    }

    public static string[] HorizontalFlip(this IEnumerable<string> grid)
    {
        return grid.Select(x => string.Concat(x.Reverse())).ToArray();
    }

    public static string[] RotateLeft(this IEnumerable<string> grid)
    {
        return Transpose(HorizontalFlip(grid));
    }

    public static string[] RotateRight(this IEnumerable<string> grid)
    {
        return HorizontalFlip(Transpose(grid));
    }
}