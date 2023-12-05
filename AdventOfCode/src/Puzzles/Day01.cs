using System.Collections.ObjectModel;
using System.Text.RegularExpressions;

namespace AdventOfCode.Puzzles;

public partial class Day01 : BaseDay
{
    public override int SolvePart1()
    {
        return InputFileAsLines.Select(ParseLine).Sum();

        int ParseLine(string line)
        {
            var nums = Digits().Matches(line).Select(x => x.Value).ToArray();
            return int.Parse(nums.First() + nums.Last());
        }
    }

    public override int SolvePart2()
    {
        return InputFileAsLines.Select(ParseLine).Sum();

        int ParseLine(string line)
        {
            var numbers = Numbers().Matches(line).Select(x => ConvertWord(x.Groups[1].Value)).ToArray();
            return int.Parse(numbers.First() + numbers.Last());
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

    [GeneratedRegex(@"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")]
    private static partial Regex Numbers();

    [GeneratedRegex(@"\d")]
    private static partial Regex Digits();
}