using System.Text.RegularExpressions;

namespace AdventOfCode.Puzzles;

public partial class Day04 : BaseDay
{
    private List<Card> Cards { get; set; } = [];

    public override object SolvePart1()
    {
        Cards = InputFileAsLines
            .Select(line => CardRegex().Match(line).Groups)
            .Select(group => new Card(
                int.Parse(group[1].Value),
                group[2].Captures.Select(capture => int.Parse(capture.Value)).ToArray(),
                group[3].Captures.Select(capture => int.Parse(capture.Value)).ToArray())).ToList();

        return (int)Cards
            .Select(card => card.ScratchedNumbers.Count(scratched => card.WinningNumber.Contains(scratched)))
            .Where(count => count > 0)
            .Select(count => Math.Pow(2, count - 1))
            .Sum();
    }

    public override object SolvePart2()
    {
        var copies = Cards.ToDictionary(card => card.CardId, _ => 1);

        var wins = Cards
            .Select(card => (cardId: card.CardId,
                count: card.ScratchedNumbers.Count(s => card.WinningNumber.Contains(s))))
            .Where(card => card.count > 0)
            .ToArray();

        foreach (var (cardId, count) in wins)
        {
            var cardCount = copies[cardId];
            for (var i = 1; i <= count; i++) copies[cardId + i] += cardCount;
        }

        return copies
            .Select(copyCount => copyCount.Value)
            .Sum();
    }

    [GeneratedRegex(@"Card +(\d+): +(\d+ +)+\|( *\d+)+")]
    private static partial Regex CardRegex();

    private sealed record Card(int CardId, int[] WinningNumber, int[] ScratchedNumbers);
}