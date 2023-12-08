using AdventOfCode.Helpers;

namespace AdventOfCode.Engines;

public static class Generator
{
    public static Task GenerateNextDay()
    {
        var dayIndex = GetNextDayIndex();
        return GenerateDay(dayIndex);
    }

    private static uint GetNextDayIndex()
    {
        var daysDirectoryPath = DirectoryElf.GetPath("Puzzles");

        var dayFiles = Directory.GetFiles(daysDirectoryPath, "Day*.cs");
        var dayIndexes = dayFiles.Select(dayFile =>
        {
            var dayFileName = Path.GetFileNameWithoutExtension(dayFile);
            var dayIndex = dayFileName[^2..];

            if (!uint.TryParse(dayIndex, out var dayIndexNumber))
                throw new InvalidOperationException($"Invalid day file name: {dayFileName}");

            return dayIndexNumber;
        }).ToList();

        var lastDayIndex = dayIndexes.Max();
        if (lastDayIndex == 25) throw new InvalidOperationException("All days have been generated.");

        return lastDayIndex + 1;
    }

    private static async Task GenerateDay(uint dayIndex)
    {
        await CreateDayFile(dayIndex);
        await CreateInputFile(dayIndex);
    }

    private static async Task CreateDayFile(uint dayIndex)
    {
        var dayName = $"Day{dayIndex:D2}";

        var daysDirectoryPath = DirectoryElf.GetPath("Puzzles");
        var dayFilePath = Path.Combine(daysDirectoryPath, $"{dayName}.cs");

        if (File.Exists(dayFilePath))
        {
            Console.WriteLine($"Day {dayIndex} already exists.");
            return;
        }

        var templatesDirectoryPath = DirectoryElf.GetPath("Templates");
        var dayTemplatePath = Path.Combine(templatesDirectoryPath, "DayXX.cs");
        if (!File.Exists(dayTemplatePath))
            throw new InvalidOperationException($"Could not find day template: {dayTemplatePath}");

        var dayTemplate = await File.ReadAllTextAsync(dayTemplatePath);
        var dayContents = dayTemplate
            .Replace("DayXX", dayName)
            .Replace("namespace AdventOfCode.Templates;", "namespace AdventOfCode.Puzzles;")
            .Replace("using AdventOfCode.Puzzles;", "");

        await File.WriteAllTextAsync(dayFilePath, dayContents);

        Console.WriteLine($"Created day {dayIndex}.");
    }

    private static async Task CreateInputFile(uint dayIndex)
    {
        var inputsDirectoryPath = DirectoryElf.GetPath("Inputs");
        var inputFilePath = Path.Combine(inputsDirectoryPath, $"{dayIndex:D2}.txt");

        if (File.Exists(inputFilePath))
        {
            Console.WriteLine($"Input file for day {dayIndex} already exists.");
            return;
        }

        await File.WriteAllTextAsync(inputFilePath, string.Empty);

        Console.WriteLine($"Created input file for day {dayIndex}.");
    }
}