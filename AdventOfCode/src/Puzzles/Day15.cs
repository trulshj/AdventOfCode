namespace AdventOfCode.Puzzles;

public class Day15 : BaseDay
{
    private Instruction[] Instructions { get; set; } = [];

    protected override void ParseInput()
    {
        Instructions = InputFileContents.Split(',').Select(x =>
        {
            if (x.Contains('-')) return new Instruction(x, x.Split('-')[0], '-', null);
            var split = x.Split('=');
            return new Instruction(x, split[0], '=', int.Parse(split[1]));
        }).ToArray();
    }

    private static int Hash(string input)
    {
        var hashValue = 0;

        foreach (var c in input)
        {
            hashValue += Convert.ToInt32(c);
            hashValue *= 17;
            hashValue %= 256;
        }

        return hashValue;
    }

    protected override object SolvePartOne()
    {
        return Instructions.Select(x => x.Original).Sum(Hash);
    }

    protected override object SolvePartTwo()
    {
        Dictionary<int, List<Lens>> boxes = new();

        foreach (var instruction in Instructions)
        {
            var boxKey = Hash(instruction.Label);
            if (!boxes.ContainsKey(boxKey)) boxes.Add(boxKey, []);

            if (instruction.Operation == '-')
            {
                boxes[boxKey].RemoveAll(x => x.Label == instruction.Label);
                continue;
            }

            var existingLensIndex = boxes[boxKey].FindIndex(x => x.Label == instruction.Label);
            if (existingLensIndex != -1)
                boxes[boxKey][existingLensIndex] = new Lens(instruction.Label, instruction.FocalLength!.Value);
            else
                boxes[boxKey].Add(new Lens(instruction.Label, instruction.FocalLength!.Value));
        }

        return boxes.Sum(box => box.Value.Select((lens, idx) => (idx + 1) * (box.Key + 1) * lens.FocalLength).Sum());
    }

    private sealed record Instruction(string Original, string Label, char Operation, int? FocalLength);

    private sealed record Lens(string Label, int FocalLength);
}