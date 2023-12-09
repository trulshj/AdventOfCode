namespace AdventOfCode.Puzzles;

public class Day09 : BaseDay
{
    private int[][] Numbers { get; set; } = Array.Empty<int[]>();

    private void ParseInput()
    {
        Numbers = InputFileAsLines
            .Select(line => line.Split(" ").Select(int.Parse).ToArray())
            .ToArray();
    }

    public override object SolvePart1()
    {
        ParseInput();

        return Numbers.Select(x => FindNext(x) + x.Last()).Sum();
    }

    public override object SolvePart2()
    {
        return Numbers.Select(x => FindPrevious(x) - x.First()).Sum();
    }

    private static int FindNext(IEnumerable<int> numbers)
    {
        var differences = new List<int[]>();

        var currentNumbers = numbers.ToArray();

        while (Array.Exists(currentNumbers, x => x != 0))
        {
            var difference = currentNumbers.Zip(currentNumbers.Skip(1)).Select(x => x.Second - x.First).ToArray();
            differences.Add(difference);
            currentNumbers = difference;
        }

        return differences.Select(x => x.Last()).Sum();
    }

    private static int FindPrevious(IEnumerable<int> numbers)
    {
        var differences = new List<int[]>();

        var currentNumbers = numbers.Reverse().ToArray();

        Console.WriteLine(string.Join(", ", currentNumbers));

        while (Array.Exists(currentNumbers, x => x != 0))
        {
            var difference = currentNumbers.Zip(currentNumbers.Skip(1)).Select(x => x.First - x.Second).ToArray();
            differences.Add(difference);
            currentNumbers = difference;
            Console.WriteLine(string.Join(", ", difference));
        }

        Console.WriteLine(differences.Select(x => x.Last()).Sum());

        return differences.Select(x => x.Last()).Sum();
    }
}