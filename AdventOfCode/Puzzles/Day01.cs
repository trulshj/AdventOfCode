using System.Collections.ObjectModel;
using System.Text.RegularExpressions;
using AdventOfCode.Extensions;

namespace AdventOfCode.Puzzles;

public partial class Day01 : BaseDay
{
    public override async Task<string> SolvePart1Async()
    {
        var inputAsLines = await ReadInputFileAsLinesAsync();
        return inputAsLines.Select(ParseLine).Sum().ToString();

        int ParseLine(string line)
        {
            var nums = Digits().Matches(line).Select(x => x.Value).ToArray();
            var n = nums.First() + nums.Last();
            return int.Parse(n);
        }
    }

    public override async Task<string> SolvePart2Async()
    {
        var inputAsLines = await ReadInputFileAsLinesAsync();
        return inputAsLines.Select(ParseLine).Sum().ToString();

        int ParseLine(string line)
        {
            var nums = ForwardsNumbers().Matches(line)
                .Select(x => x.Value).ToList();

            var reversedNums = ReversedNumbers().Matches(line.ReverseX())
                .Select(x => x.Value.ReverseX()).ToList();

            var first = ConvertWord(nums.First());
            var snd = ConvertWord(reversedNums.First());

            return int.Parse(first + snd);
        }
    }

    private static string ConvertWord(string word)
    {
        var digitDictionary = new ReadOnlyDictionary<string, string>(new Dictionary<string, string>
        {
            { "one", "1" },
            { "two", "2" },
            { "three", "3" },
            { "four", "4" },
            { "five", "5" },
            { "six", "6" },
            { "seven", "7" },
            { "eight", "8" },
            { "nine", "9" },
            { "zero", "0" }
        });

        return word.Length == 1 ? word : digitDictionary[word];
    }

    [GeneratedRegex(@"\d|one|two|three|four|five|six|seven|eight|nine")]
    private static partial Regex ForwardsNumbers();

    [GeneratedRegex(@"\d|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno")]
    private static partial Regex ReversedNumbers();

    [GeneratedRegex(@"\d")]
    private static partial Regex Digits();
}