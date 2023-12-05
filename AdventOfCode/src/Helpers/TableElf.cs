using Spectre.Console;

namespace AdventOfCode.Helpers;

public static class TableElf
{
    public static Table CreateTable()
    {
        return new Table()
            .AddColumn("[bold]Day[/]")
            .AddColumn("[bold]Part[/]")
            .AddColumn("[bold]Solution[/]")
            .AddColumn("[bold]Time[/]")
            .BorderColor(Color.Grey);
    }

    public static void AddSolutionRow(this Table table, string part, string solution, double elapsedTime)
    {
        var formattedTime = FormatTime(elapsedTime);
        table.AddRow("", $"Part {part}", solution.EscapeMarkup(), formattedTime);
    }

    public static void AddDayTitleRow(this Table table, string day)
    {
        table.AddRow(day);
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