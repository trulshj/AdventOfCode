using System.Text.RegularExpressions;

namespace AdventOfCode.Puzzles;

public class Day02 : BaseDay
{
    private (int gameId, string[] pulls)[] Games { get; set; } = [];

    protected override object SolvePartOne()
    {
        const int maxReds = 12;
        const int maxGreens = 13;
        const int maxBlues = 14;

        return Games
            .Where(x => IsPossible(x.pulls))
            .Sum(x => x.gameId);

        bool IsPossible(IEnumerable<string> pulls)
        {
            foreach (var pull in pulls)
            {
                var (reds, greens, blues) = GetColors(pull);

                if (reds > maxReds || greens > maxGreens || blues > maxBlues)
                    return false;
            }

            return true;
        }
    }


    protected override object SolvePartTwo()
    {
        var sum = 0;

        foreach (var pulls in Games.Select(x => x.pulls))
        {
            var maxReds = 0;
            var maxGreens = 0;
            var maxBlues = 0;

            foreach (var pull in pulls)
            {
                var (reds, greens, blues) = GetColors(pull);

                maxReds = Math.Max(maxReds, reds);
                maxGreens = Math.Max(maxGreens, greens);
                maxBlues = Math.Max(maxBlues, blues);
            }

            sum += maxReds * maxBlues * maxGreens;
        }

        return sum;
    }

    protected override void ParseInput()
    {
        Games = InputFileAsLines.Select(line =>
        {
            var parts = line.Split(": ");
            var gameId = Convert.ToInt32(parts[0].Split(" ").Last());
            var pulls = parts[1].Split("; ");
            return (gameId, pulls);
        }).ToArray();
    }

    private static Regex GetColor(string color)
    {
        return new Regex($@"(\d+) {color}");
    }

    private static (int reds, int greens, int blues) GetColors(string pull)
    {
        return (
            int.TryParse(GetColor("red").Match(pull).Groups[1].Value, out var reds) ? reds : 0,
            int.TryParse(GetColor("green").Match(pull).Groups[1].Value, out var greens) ? greens : 0,
            int.TryParse(GetColor("blue").Match(pull).Groups[1].Value, out var blues) ? blues : 0
        );
    }
}