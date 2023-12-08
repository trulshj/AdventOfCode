using AdventOfCode.Helpers;

namespace AdventOfCode.Puzzles;

public abstract class BaseDay
{
    private static string ClassPrefix => "Day";
    private static string InputFileExtension => ".txt";
    private string InputFileDirectory { get; } = DirectoryElf.GetPath("Inputs");
    protected string InputFileContents { get; private set; } = string.Empty;
    protected string[] InputFileAsLines { get; private set; } = Array.Empty<string>();


    public uint CalculateProblemIndex()
    {
        var className = GetType().Name;
        var dayIndex = className.IndexOf(ClassPrefix, StringComparison.Ordinal);
        var problemIndex = className[(dayIndex + ClassPrefix.Length)..];
        return uint.Parse(problemIndex);
    }

    public void LoadInputFileContents()
    {
        InputFileContents = File.ReadAllText(InputFilePath());
        InputFileAsLines = File.ReadAllLines(InputFilePath());
    }

    private string InputFilePath()
    {
        var problemIndex = CalculateProblemIndex();

        return Path.Combine(InputFileDirectory, $"{problemIndex:D2}{InputFileExtension}");
    }

    public void CheckInputFileExists()
    {
        var inputFilePath = InputFilePath();
        if (!File.Exists(inputFilePath)) throw new FileNotFoundException($"Input file not found: {inputFilePath}");
    }

    public abstract object SolvePart1();
    public abstract object SolvePart2();
}