using Spectre.Console;

namespace AdventOfCode.Engines;

public static class Prompter
{
    public static UserAction PromptUserForAction()
    {
        var actionFromPrompt = AnsiConsole.Prompt(new SelectionPrompt<string>()
            .Title("Select action")
            .AddChoices(Enum.GetNames<UserAction>()));

        if (Enum.TryParse(actionFromPrompt, out UserAction action))
            return action;
        throw new ArgumentException($"Invalid action: {actionFromPrompt}");
    }
}

public enum UserAction
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