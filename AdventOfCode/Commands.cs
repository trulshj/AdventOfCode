using System.CommandLine;
using AdventOfCode.Engines;

namespace AdventOfCode;

public static class Commands
{
    public static Command SolveCommand()
    {
        var solveCommand = new Command("solve", "Solve all days");

        var dayOption = new Option<int?>(new[] { "--day", "-d" }, "Solve a specific day");
        var latestOption = new Option<bool>(new[] { "--latest", "-l" }, "Solve the latest day");

        solveCommand.AddOption(dayOption);
        solveCommand.AddOption(latestOption);

        solveCommand.SetHandler(HandleSolveCommand, dayOption, latestOption);

        return solveCommand;
    }

    public static RootCommand RootCommand()
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
            var solver = new Solver();

            if (promptUser || action is null)
                action = Prompter.PromptUserForAction();

            switch (action)
            {
                case UserAction.SolveLatest:
                    await solver.SolveLatest();
                    break;
                case UserAction.SolveAll:
                    await solver.SolveAll();
                    break;
                case UserAction.GenerateNextDay:
                    await Generator.GenerateNextDay();
                    break;
                default:
                    throw new InvalidActionException($"Unknown action: {action}");
            }
        }, promptOption, actionOption);

        return rootCommand;
    }

    public static Command GenerateCommand()
    {
        var generateCommand = new Command("generate", "Generate next day");

        generateCommand.AddAlias("gen");

        generateCommand.SetHandler(async () => await Generator.GenerateNextDay());

        return generateCommand;
    }


    private static async Task HandleSolveCommand(int? day, bool latest)
    {
        var solver = new Solver();

        await (day switch
        {
            { } dayValue => solver.SolveSpecific(dayValue),
            _ when latest => solver.SolveLatest(),
            _ => solver.SolveAll()
        });
    }
}