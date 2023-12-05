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

    private void Solve(IEnumerable<BaseDay> days)
    {
        AnsiConsole.Live(Table).Start(_ =>
        {
            foreach (var day in days)
            {
                SolveDay(day);
                Table.AddEmptyRow();
            }
        });
    }

    private void Solve(BaseDay day)
    {
        Solve(new[] { day });
    }

    public void SolveLatest()
    {
        Solve(Days.Last());
    }

    public void SolveSpecific(int dayIndex)
    {
        Solve(Days[dayIndex - 1]);
    }

    public void SolveAll()
    {
        Solve(Days);
    }

    private void SolveDay(BaseDay day)
    {
        var problemIndex = day.CalculateProblemIndex();
        var problemTitle = $"Day {problemIndex}";

        Table.AddDayTitleRow(problemTitle);

        try
        {
            day.CheckInputFileExists();
            day.LoadInputFileContents();
        }
        catch (FileNotFoundException)
        {
            Table.AddSolutionRow("1", "Input file not found", 0);
            Table.AddSolutionRow("2", "Input file not found", 0);
            return;
        }

        var (part1Solution, part1ElapsedTime) = SolvePart(day.SolvePart1);
        Table.AddSolutionRow("1", part1Solution, part1ElapsedTime);

        var (part2Solution, part2ElapsedTime) = SolvePart(day.SolvePart2);
        Table.AddSolutionRow("2", part2Solution, part2ElapsedTime);
    }

    private static (string solution, long elapsedTime) SolvePart(Func<int> partFunction)
    {
        Stopwatch stopwatch = new();
        string solution;

        try
        {
            stopwatch.Start();
            solution = partFunction().ToString();
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