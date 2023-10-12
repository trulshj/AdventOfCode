namespace AdventOfCode;

public abstract class BaseDay
{
    protected virtual string ClassPrefix { get; } = "Day";
    protected virtual string InputFileDirectory { get; } = "Inputs";
    protected virtual string InputFileExtension { get; } = ".txt";

    public virtual uint CalculateProblemIndex()
    {
        var className = GetType().Name;
        var dayIndex = className.IndexOf(ClassPrefix, StringComparison.Ordinal);
        var problemIndex = className[(dayIndex + ClassPrefix.Length)..];
        return uint.Parse(problemIndex);
    }

    public virtual string InputFilePath()
    {
        var problemIndex = CalculateProblemIndex();
        return Path.Combine(InputFileDirectory, $"{problemIndex:D2}{InputFileExtension}");
    }

    public virtual async Task<string> ReadInputFileAsync()
    {
        var inputFilePath = InputFilePath();
        return await File.ReadAllTextAsync(inputFilePath);
    }

    public virtual async Task<string[]> ReadInputFileAsLinesAsync()
    {
        var inputFilePath = InputFilePath();
        return await File.ReadAllLinesAsync(inputFilePath);
    }

    public virtual void CheckInputFileExists()
    {
        var inputFilePath = InputFilePath();
        if (!File.Exists(inputFilePath)) throw new FileNotFoundException($"Input file not found: {inputFilePath}");
    }

    public abstract Task<string> SolvePart1Async();
    public abstract Task<string> SolvePart2Async();
}