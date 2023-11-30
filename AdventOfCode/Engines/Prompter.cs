using Spectre.Console;

namespace AdventOfCode.Engines;

public static class Prompter
{
    public static Action PromptUserForAction()
    {
        var actionFromPrompt = AnsiConsole.Prompt(new SelectionPrompt<string>()
            .Title("Select action")
            .AddChoices(Enum.GetNames<Action>()));

        if (Enum.TryParse(actionFromPrompt, out Action action))
            return action;
        throw new ArgumentException($"Invalid action: {actionFromPrompt}");
    }
}

public enum Action
{
    SolveAll,
    GenerateNextDay
}

public class InvalidActionException : Exception
{
    public InvalidActionException(string message) : base(message)
    {
    }
}