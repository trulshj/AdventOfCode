using System.CommandLine;

namespace AdventOfCode;

internal static class Program
{
    private static async Task<int> Main(string[] args)
    {
        var rootCommand = Commands.RootCommand();

        rootCommand.AddCommand(Commands.SolveCommand());
        rootCommand.AddCommand(Commands.GenerateCommand());

        return await rootCommand.InvokeAsync(args);
    }
}