namespace AdventOfCode.Puzzles;

public class Day09 : BaseDay
{
    private int[][] Numbers { get; set; } = Array.Empty<int[]>();

    protected override void ParseInput()
    {
        Numbers = InputFileAsLines
            .Select(line => line.Split(" ").Select(int.Parse).ToArray())
            .ToArray();
    }

    protected override object SolvePartOne()
    {
        ParseInput();

        return Numbers.Select(FindNext).Sum();
    }

    protected override object SolvePartTwo()
    {
        return Numbers.Select(FindPrevious).Sum();
    }

    private static int FindNext(int[] numbers)
    {
        return numbers.Last() + GetDifferences(numbers)
            .Select(x => x.Last())
            .Sum();
    }

    private static int FindPrevious(int[] numbers)
    {
        return numbers.First() - GetDifferences(numbers)
            .Select(x => x.First())
            .Reverse()
            .Aggregate(0, (acc, x) => x - acc);
    }

    private static List<int[]> GetDifferences(IEnumerable<int> numbers)
    {
        var differences = new List<int[]>();

        var currentNumbers = numbers.ToArray();

        while (Array.Exists(currentNumbers, x => x != 0))
        {
            var difference = currentNumbers.Zip(currentNumbers.Skip(1)).Select(x => x.Second - x.First).ToArray();
            differences.Add(difference);
            currentNumbers = difference;
        }

        return differences;
    }
}