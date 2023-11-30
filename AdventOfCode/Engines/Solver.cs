using System.Diagnostics;
using System.Reflection;
using AdventOfCode.Puzzles;
using Spectre.Console;

namespace AdventOfCode.Engines;

public static class Solver
{
    public static async Task Solve()
    {
        var table = CreateTable();

        var days = LoadAllDays(Assembly.GetExecutingAssembly());

        await AnsiConsole.Live(table).StartAsync(async _ =>
        {
            foreach (var day in days)
            {
                await SolveDay(day, table);
                table.AddEmptyRow();
            }
        });
    }

    private static async Task SolveDay(BaseDay day, Table table)
    {
        var problemIndex = day.CalculateProblemIndex();
        var problemTitle = $"Day {problemIndex}";

        AddDayTitleRow(table, problemTitle);

        try
        {
            day.CheckInputFileExists();
        }
        catch (FileNotFoundException)
        {
            AddRow(table, "1", "Input file not found", 0);
            AddRow(table, "2", "Input file not found", 0);
            return;
        }

        var (part1Solution, part1ElapsedTime) = await SolvePart(true, day);
        AddRow(table, "1", part1Solution, part1ElapsedTime);

        var (part2Solution, part2ElapsedTime) = await SolvePart(false, day);
        AddRow(table, "2", part2Solution, part2ElapsedTime);
    }

    private static async Task<(string solution, long elapsedTime)> SolvePart(bool part1, BaseDay day)
    {
        Stopwatch stopwatch = new();
        string solution;

        try
        {
            stopwatch.Start();
            solution = part1 ? await day.SolvePart1Async() : await day.SolvePart2Async();
        }
        catch (NotImplementedException)
        {
            solution = "Not Implemented";
        }
        catch (Exception e)
        {
            solution = e.Message;
        }
        finally
        {
            stopwatch.Stop();
        }

        var elapsed = stopwatch.ElapsedMilliseconds;

        return (solution, elapsed);
    }

    private static Table CreateTable()
    {
        return new Table()
            .AddColumn("[bold]Day[/]")
            .AddColumn("[bold]Part[/]")
            .AddColumn("[bold]Solution[/]")
            .AddColumn("[bold]Time[/]")
            .BorderColor(Color.Grey);
    }

    private static void AddRow(Table table, string part, string solution, double elapsedTime)
    {
        var formattedTime = FormatTime(elapsedTime);
        table.AddRow("", $"Part {part}", solution.EscapeMarkup(), formattedTime);
    }

    private static void AddDayTitleRow(Table table, string day)
    {
        table.AddRow(day);
    }

    internal static IEnumerable<BaseDay> LoadAllDays(Assembly assembly)
    {
        return assembly.GetTypes()
            .Where(type => typeof(BaseDay).IsAssignableFrom(type) &&
                           type is { IsAbstract: false, IsInterface: false } && !type.FullName!.EndsWith("XX"))
            .OrderBy(t => t.FullName)
            .Select(t => Activator.CreateInstance(t) as BaseDay)!;
    }

    private static string FormatTime(double elapsedMilliseconds)
    {
        var message =
            elapsedMilliseconds switch
            {
                < 1 => $"{elapsedMilliseconds:F} ms",
                < 1_000 => $"{Math.Round(elapsedMilliseconds)} ms",
                < 60_000 => $"{0.001 * elapsedMilliseconds:F} s",
                _ =>
                    $"{Math.Floor(elapsedMilliseconds / 60_000)} min {Math.Round(0.001 * (elapsedMilliseconds % 60_000))} s"
            };

        var color = elapsedMilliseconds switch
        {
            0 => Color.White,
            < 1 => Color.Blue,
            < 10 => Color.Green1,
            < 100 => Color.Lime,
            < 500 => Color.GreenYellow,
            < 1_000 => Color.Yellow1,
            < 10_000 => Color.OrangeRed1,
            _ => Color.Red1
        };

        return $"[{color}]{message}[/]";
    }
}