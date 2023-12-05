namespace AdventOfCode.Helpers;

public static class DirectoryElf
{
    /// <summary>
    ///     Gets the path for a directory in the root project directory, instead of the build output directory
    /// </summary>
    public static string GetPath(string directoryName)
    {
        var projectDirectoryPath = Environment.CurrentDirectory.Contains("bin")
            ? Directory.GetParent(Environment.CurrentDirectory)?.Parent?.Parent?.FullName
            : Environment.CurrentDirectory;

        if (projectDirectoryPath is null || !Directory.Exists(projectDirectoryPath))
            throw new InvalidOperationException($"Could not find project directory: {projectDirectoryPath}");

        var directoryPath = Path.Combine(projectDirectoryPath, directoryName);
        if (!Directory.Exists(directoryPath))
            throw new InvalidOperationException($"Could not find {directoryName} directory: {directoryPath}");

        return directoryPath;
    }
}