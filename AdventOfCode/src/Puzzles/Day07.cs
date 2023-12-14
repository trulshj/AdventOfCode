namespace AdventOfCode.Puzzles;

public class Day07 : BaseDay
{
    private readonly char[] _cardValues = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'];
    private readonly char[] _jokerCardValues = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'];
    private List<Hand> Hands { get; set; } = null!;

    private int GetCardValue(char cardType, bool joker = false)
    {
        return Array.IndexOf(joker ? _jokerCardValues : _cardValues, cardType);
    }

    protected override void ParseInput()
    {
        Hands = InputFileAsLines
            .Select(line => line.Split(" "))
            .Select(line => new Hand(line[0], int.Parse(line[1])))
            .Select(x => x with { HandType = ClassifyHand(x) })
            .ToList();
    }

    protected override object SolvePartOne()
    {
        ParseInput();

        Hands.Sort((hand1, hand2) => CompareHands(hand1, hand2));

        return Hands
            .Select((hand, index) => hand.Bid * (index + 1))
            .Sum();
    }

    protected override object SolvePartTwo()
    {
        var jokerHands = Hands.Select(x => x with { HandType = ClassifyHand(x, true) }).ToList();

        jokerHands.Sort((hand1, hand2) => CompareHands(hand1, hand2, true));

        return jokerHands
            .Select((hand, index) => hand.Bid * (index + 1))
            .Sum();
    }

    private static HandType ClassifyHand(Hand hand, bool joker = false)
    {
        var cardCounts = new Dictionary<char, int>();
        foreach (var card in hand.Cards)
        {
            cardCounts.TryAdd(card, 0);
            cardCounts[card] += 1;
        }

        if (joker)
        {
            var jokerCount = cardCounts.GetValueOrDefault('J', 0);
            if (jokerCount == 5) return HandType.FiveOfAKind;

            cardCounts.Remove('J');

            var mostCardKey = cardCounts.MaxBy(x => x.Value).Key;
            cardCounts[mostCardKey] += jokerCount;
        }

        var cardCountValues = cardCounts.Values.OrderDescending().ToArray();

        return cardCountValues.Length switch
        {
            5 => HandType.HighCard,
            4 => HandType.Pair,
            1 => HandType.FiveOfAKind,
            3 => cardCountValues[0] == 3 ? HandType.ThreeOfAKind : HandType.TwoPair,
            2 => cardCountValues[0] == 4 ? HandType.FourOfAKind : HandType.FullHouse,
            _ => throw new ArgumentException("Invalid hand")
        };
    }

    private int CompareHands(Hand hand1, Hand hand2, bool joker = false)
    {
        if (hand1.HandType != hand2.HandType) return hand1.HandType - hand2.HandType;

        for (var i = 0; i < hand1.Cards.Length; i++)
        {
            var card1Value = GetCardValue(hand1.Cards[i], joker);
            var card2Value = GetCardValue(hand2.Cards[i], joker);

            if (card1Value == card2Value) continue;
            return card2Value - card1Value;
        }

        return 0;
    }

    private enum HandType
    {
        Unknown = 0,
        HighCard = 1,
        Pair = 2,
        TwoPair = 3,
        ThreeOfAKind = 4,
        FullHouse = 5,
        FourOfAKind = 6,
        FiveOfAKind = 7
    }

    private sealed record Hand(string Cards, int Bid, HandType HandType = HandType.Unknown);
}