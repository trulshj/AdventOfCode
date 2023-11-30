using System.CommandLine;
using AdventOfCode.Engines;

namespace AdventOfCode;

internal static class Program
{
    private static async Task<int> Main(string[] args)
    {
        var promptOption = new Option<bool>(
            new[] { "--promptUser", "-p" },
            description: "Prompt user for action",
            getDefaultValue: () => false);

        var actionOption = new Option<UserAction?>(
            new[] { "--action", "-a" },
            "Specify the action to perform");

        var rootCommand = new RootCommand("Advent of Code");

        rootCommand.AddOption(promptOption);
        rootCommand.AddOption(actionOption);

        rootCommand.SetHandler(async (promptUser, action) =>
        {
            if (promptUser || action is null)
                action = Prompter.PromptUserForAction();

            switch (action)
            {
                case UserAction.SolveAll:
                    await Solver.Solve();
                    break;
                case UserAction.GenerateNextDay:
                    await Generator.GenerateNextDay();
                    break;
                default:
                    throw new InvalidActionException($"Unknown action: {action}");
            }
        }, promptOption, actionOption);

        var solveCommand = new Command("solve", "Solve all days");
        solveCommand.SetHandler(async () => await Solver.Solve());

        var generateCommand = new Command("generate", "Generate next day");
        generateCommand.AddAlias("gen");
        generateCommand.SetHandler(async () => await Generator.GenerateNextDay());

        rootCommand.AddCommand(solveCommand);
        rootCommand.AddCommand(generateCommand);
        return await rootCommand.InvokeAsync(args);
    }
}