namespace AdventOfCode.Puzzles;

public class Day01 : BaseDay
{
    public override async Task<string> SolvePart1Async()
    {
        var input = await ReadInputFileAsync();
        var inputAsLines = await ReadInputFileAsLinesAsync();

        Console.WriteLine("Testing testing");

        return $"Input is {input.Length} characters long";
    }

    public override Task<string> SolvePart2Async()
    {
        throw new NotImplementedException();
    }
}