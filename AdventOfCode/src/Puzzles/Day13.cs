namespace AdventOfCode.Puzzles;

public class Day13 : BaseDay
{
    private string[][] Blocks { get; set; } = [];

    protected override void ParseInput()
    {
        Blocks = InputFileContents.Split("\n\n")
            .Select(x => x.Split("\n").ToArray()).ToArray();
    }

    private static int CheckBlocks(string[] block, Func<string[], string[], bool> condition)
    {
        for (var i = 1; i < block.Length; i++)
        {
            var above = block[..i].Reverse().ToArray();
            var below = block[i..];

            if (condition(above, below)) return i;
        }

        return 0;
    }

    private static string[] Transpose(IReadOnlyList<string> block)
    {
        return Enumerable.Range(0, block[0].Length)
            .Select(i => string.Concat(block.Select(row => row[i])))
            .ToArray();
    }

    protected override object SolvePartOne()
    {
        return Blocks.Sum(FindMirror) * 100 + Blocks.Select(Transpose).Sum(FindMirror);

        int FindMirror(string[] block)
        {
            return CheckBlocks(block, (above, below) => above.Zip(below).All(x => x.First == x.Second));
        }
    }

    protected override object SolvePartTwo()
    {
        return Blocks.Sum(FindSmudge) * 100 + Blocks.Select(Transpose).Sum(FindSmudge);

        int FindSmudge(string[] block)
        {
            return CheckBlocks(block, (above, below) =>
                above.Zip(below, (a, b) =>
                        a.Zip(b, (charA, charB) => charA == charB ? 0 : 1).Sum())
                    .Sum() == 1);
        }
    }
}