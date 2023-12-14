using System.Text.RegularExpressions;
using AdventOfCode.Helpers;

namespace AdventOfCode.Puzzles;

public partial class Day08 : BaseDay
{
    private Dictionary<string, (string left, string right)> Paths { get; } = new();
    private string Directions { get; set; } = string.Empty;

    protected override void ParseInput()
    {
        Directions = InputFileAsLines[0];
        foreach (var line in InputFileAsLines.Skip(2))
        {
            var matches = Nodes().Matches(line);
            Paths.Add(matches[0].Value, (matches[1].Value, matches[2].Value));
        }
    }

    protected override object SolvePartOne()
    {
        ParseInput();

        return FindCycleLength("AAA");
    }

    protected override object SolvePartTwo()
    {
        return Paths.Keys
            .Where(x => x.EndsWith('A'))
            .Select(x => FindCycleLength(x, true))
            .Aggregate(MathElf.Lcm);
    }

    private long FindCycleLength(string startingNode, bool part2 = false)
    {
        var currentNode = startingNode;
        var steps = 0;

        while (part2 ? !currentNode.EndsWith('Z') : currentNode != "ZZZ")
        {
            var direction = Directions[steps % Directions.Length];
            var (left, right) = Paths[currentNode];
            currentNode = direction == 'L' ? left : right;
            steps++;
        }

        return steps;
    }

    [GeneratedRegex(@"(\w{3})")]
    private static partial Regex Nodes();
}