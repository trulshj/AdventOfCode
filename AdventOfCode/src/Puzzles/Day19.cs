using System.Text.RegularExpressions;
using AdventOfCode.Engines;

namespace AdventOfCode.Puzzles;

public partial class Day19 : BaseDay
{
    private readonly List<Part> _parts = [];
    private readonly Dictionary<string, Rule[]> _workflows = new();

    protected override void ParseInput()
    {
        var sections = InputFileContents.Split("\n\n");

        foreach (var workflow in sections[0].Split('\n'))
        {
            var x = workflow.Split("{");
            var name = x[0].Trim();
            var rules = x[1].Trim().TrimEnd('}').Split(",").Select(s => new Rule(s)).ToArray();
            _workflows.Add(name, rules);
        }

        foreach (var line in sections[1].Split('\n'))
        {
            var numbers = Numbers().Matches(line).Select(m => int.Parse(m.Value)).ToArray();
            _parts.Add(new Part(numbers[0], numbers[1], numbers[2], numbers[3]));
        }
    }

    protected override object SolvePartOne()
    {
        return _parts.Where(CheckPart).Sum(p => p.X + p.M + p.A + p.S);
    }

    private bool CheckPart(Part part)
    {
        var currentWorkflow = "in";

        while (currentWorkflow is not ("A" or "R"))
        {
            var rules = _workflows[currentWorkflow];
            currentWorkflow = rules.First(r => r.Applies(part)).Target;
        }

        return currentWorkflow == "A";
    }

    protected override object SolvePartTwo()
    {
        Dictionary<char, (int min, int max)> startRange = new()
        {
            { 'x', (1, 4000) },
            { 'm', (1, 4000) },
            { 'a', (1, 4000) },
            { 's', (1, 4000) }
        };

        return FindValidRanges(startRange, "in");
    }

    private long FindValidRanges(IDictionary<char, (int min, int max)> range, string workflow)
    {
        switch (workflow)
        {
            case "R":
                return 0L;
            case "A":
                return range.Aggregate(1L, (current, kvp) => current * (kvp.Value.max - kvp.Value.min + 1L));
        }

        var rules = _workflows[workflow];
        var total = 0L;

        var hasLeftovers = true;
        foreach (var rule in rules[..^1]) // The last rule is always a direct rule
        {
            var (min, max) = range[rule.Property!.Value];
            var check = rule.Value!.Value;

            (int min, int max) failRange, passRange;
            if (rule.Type == RuleType.LessThan)
            {
                passRange = (min, Math.Min(check - 1, max));
                failRange = (Math.Max(check, min), max);
            }
            else // GreaterThan
            {
                passRange = (Math.Max(check + 1, min), max);
                failRange = (min, Math.Min(check, max));
            }

            if (passRange.min <= passRange.max)
            {
                var copy = new Dictionary<char, (int min, int max)>(range) { [rule.Property.Value] = passRange };
                total += FindValidRanges(copy, rule.Target);
            }

            if (failRange.min <= failRange.max)
            {
                range = new Dictionary<char, (int min, int max)>(range) { [rule.Property.Value] = failRange };
            }
            else
            {
                // We have covered all possible values for this property
                hasLeftovers = false;
                break;
            }
        }

        if (hasLeftovers)
            total += FindValidRanges(range, rules.Last().Target);

        return total;
    }

    [GeneratedRegex(@"\d+")]
    private static partial Regex Numbers();

    private sealed partial class Rule
    {
        public Rule(string input)
        {
            if (!input.Contains(':'))
            {
                Type = RuleType.Direct;
                Target = input;
                return;
            }

            var match = PartRegex().Match(input);

            Property = match.Groups[1].Value[0];
            Type = match.Groups[2].Value switch
            {
                "<" => RuleType.LessThan,
                ">" => RuleType.GreaterThan,
                _ => throw new InvalidActionException("Invalid rule type")
            };
            Value = int.Parse(match.Groups[3].Value);
            Target = match.Groups[4].Value;
        }

        public char? Property { get; }
        public RuleType Type { get; }
        public int? Value { get; }
        public string Target { get; }

        public bool Applies(Part input)
        {
            if (Type == RuleType.Direct)
                return true;

            var value = Property switch
            {
                'x' => input.X,
                'm' => input.M,
                'a' => input.A,
                's' => input.S,
                _ => throw new InvalidActionException("Invalid property")
            };

            return Type switch
            {
                RuleType.GreaterThan => value > Value,
                RuleType.LessThan => value < Value,
                RuleType.Direct => true,
                _ => throw new InvalidActionException("Invalid rule type")
            };
        }

        [GeneratedRegex(@"([xmas])(<|>)(\d+):(\w+)")]
        private static partial Regex PartRegex();

        public override string ToString()
        {
            return $"{Property} {Type} {Value} -> {Target}";
        }
    }

    private enum RuleType
    {
        GreaterThan,
        LessThan,
        Direct
    }

    // Having Parts as dictionaries was easier in part 2, probably easier in part 1 as well but I don't feel like changing it
    private sealed record Part(int X, int M, int A, int S);
}