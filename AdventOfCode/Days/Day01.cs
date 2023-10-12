namespace AdventOfCode.Days;

public class Day01 : BaseDay
{
    public override async Task<string> SolvePart1Async()
    {
        var input = await ReadInputFileAsync();

        var position = (x: 0, y: 0);
        var direction = (x: 0, y: 1);

        foreach (var instruction in input.Split(", "))
        {
            var turn = instruction[0];
            var distance = int.Parse(instruction[1..]);

            direction = turn switch
            {
                'L' => (-direction.y, direction.x),
                'R' => (direction.y, -direction.x),
                _ => throw new Exception($"Invalid turn: {turn}")
            };

            position = (position.x + direction.x * distance, position.y + direction.y * distance);
        }

        return (Math.Abs(position.x) + Math.Abs(position.y)).ToString();
    }

    public override Task<string> SolvePart2Async()
    {
        throw new NotImplementedException();
    }
}