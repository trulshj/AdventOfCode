namespace AdventOfCode.Puzzles;

public abstract class BaseDay
{
    protected virtual string ClassPrefix { get; } = "Day";
    protected virtual string InputFileDirectory { get; } = "Inputs";
    protected virtual string InputFileExtension { get; } = ".txt";
    private string? InputFileContents { get; set; }
    private string[]? InputFileAsLines { get; set; }


    public virtual uint CalculateProblemIndex()
    {
        var className = GetType().Name;
        var dayIndex = className.IndexOf(ClassPrefix, StringComparison.Ordinal);
        var problemIndex = className[(dayIndex + ClassPrefix.Length)..];
        return uint.Parse(problemIndex);
    }

    protected virtual string InputFilePath()
    {
        var problemIndex = CalculateProblemIndex();
        return Path.Combine(InputFileDirectory, $"{problemIndex:D2}{InputFileExtension}");
    }

    protected virtual async Task<string> ReadInputFileAsync()
    {
        if (InputFileContents is not null) return InputFileContents;

        var inputFilePath = InputFilePath();
        InputFileContents = await File.ReadAllTextAsync(inputFilePath);

        return InputFileContents;
    }

    public virtual async Task<string[]> ReadInputFileAsLinesAsync()
    {
        if (InputFileAsLines is not null) return InputFileAsLines;

        var inputFilePath = InputFilePath();
        InputFileAsLines = await File.ReadAllLinesAsync(inputFilePath);

        return InputFileAsLines;
    }

    public virtual void CheckInputFileExists()
    {
        var inputFilePath = InputFilePath();
        if (!File.Exists(inputFilePath)) throw new FileNotFoundException($"Input file not found: {inputFilePath}");
    }

    public abstract Task<string> SolvePart1Async();
    public abstract Task<string> SolvePart2Async();
}