using System.Diagnostics;
using System.Reflection;
using AdventOfCode.Helpers;
using AdventOfCode.Puzzles;
using Spectre.Console;

namespace AdventOfCode.Engines;

public class Solver
{
    private List<BaseDay> Days { get; } =
        LoadAllDays(Assembly.GetExecutingAssembly()).OrderBy(x => x.CalculateProblemIndex()).ToList();

    private Table Table { get; } = TableElf.CreateTable();

    private async Task Solve(IEnumerable<BaseDay> days)
    {
        await AnsiConsole.Live(Table).StartAsync(async _ =>
        {
            foreach (var day in days)
            {
                await SolveDay(day);
                Table.AddEmptyRow();
            }
        });
    }

    private async Task Solve(BaseDay day)
    {
        await Solve(new[] { day });
    }

    public async Task SolveLatest()
    {
        await Solve(Days.Last());
    }

    public async Task SolveSpecific(int dayIndex)
    {
        await Solve(Days[dayIndex - 1]);
    }

    public async Task SolveAll()
    {
        await Solve(Days);
    }

    private async Task SolveDay(BaseDay day)
    {
        var problemIndex = day.CalculateProblemIndex();
        var problemTitle = $"Day {problemIndex}";

        Table.AddDayTitleRow(problemTitle);

        try
        {
            day.CheckInputFileExists();
        }
        catch (FileNotFoundException)
        {
            Table.AddSolutionRow("1", "Input file not found", 0);
            Table.AddSolutionRow("2", "Input file not found", 0);
            return;
        }

        var (part1Solution, part1ElapsedTime) = await SolvePart(day.SolvePart1Async);
        Table.AddSolutionRow("1", part1Solution, part1ElapsedTime);

        var (part2Solution, part2ElapsedTime) = await SolvePart(day.SolvePart2Async);
        Table.AddSolutionRow("2", part2Solution, part2ElapsedTime);
    }

    private static async Task<(string solution, long elapsedTime)> SolvePart(Func<Task<string>> partFunction)
    {
        Stopwatch stopwatch = new();
        string solution;

        try
        {
            stopwatch.Start();
            solution = await partFunction();
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


    private static IEnumerable<BaseDay> LoadAllDays(Assembly assembly)
    {
        return assembly.GetTypes()
            .Where(type => typeof(BaseDay).IsAssignableFrom(type) &&
                           type is { IsAbstract: false, IsInterface: false } && !type.FullName!.EndsWith("XX"))
            .OrderBy(t => t.FullName)
            .Select(t => Activator.CreateInstance(t) as BaseDay)!;
    }
}