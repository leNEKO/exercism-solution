#[derive(PartialEq, Eq, Debug, PartialOrd)]
enum Suit {
    Spade,
    Heart,
    Club,
    Diamond,
}
impl Suit {
    fn from_str(key: &str) -> Result<Self, &'static str> {
        let suit: Self = match key {
            "S" => Self::Spade,
            "H" => Self::Heart,
            "C" => Self::Club,
            "D" => Self::Diamond,
            _ => return Err("Invalid suit"),
        };

        Ok(suit)
    }
}
#[test]
fn test_suit() {
    assert_eq!(Ok(Suit::Spade), Suit::from_str("S"));
    assert_eq!(Ok(Suit::Heart), Suit::from_str("H"));
    assert_eq!(Ok(Suit::Club), Suit::from_str("C"));
    assert_eq!(Ok(Suit::Diamond), Suit::from_str("D"));
    assert_eq!(Err("Invalid Suit"), Suit::from_str("E"));
}

#[derive(Debug, Eq, PartialEq, PartialOrd)]
enum Rank {
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Jack,
    Queen,
    King,
    Ace,
}
impl Rank {
    fn from_str(key: &str) -> Result<Self, &'static str> {
        let rank: Self = match key {
            "2" => Self::Two,
            "3" => Self::Three,
            "4" => Self::Four,
            "5" => Self::Five,
            "6" => Self::Six,
            "7" => Self::Seven,
            "8" => Self::Eight,
            "9" => Self::Nine,
            "10" => Self::Ten,
            "J" => Self::Jack,
            "Q" => Self::Queen,
            "K" => Self::King,
            "A" => Self::Ace,
            _ => return Err("Invalid Rank"),
        };

        Ok(rank)
    }
}
#[test]
fn test_rank() {
    assert_eq!(Ok(Rank::Two), Rank::from_str("2"));
    assert_eq!(Err("Invalid Rank"), Rank::from_str("O"));
    assert!(Rank::Two < Rank::Three);
    assert!(Rank::Jack > Rank::Four);
    assert!(Rank::Queen == Rank::Queen);
}

#[derive(PartialEq, Eq, Debug, PartialOrd)]
struct Card {
    rank: Rank,
    suit: Suit,
}
impl Card {
    fn from_str(key: &str) -> Result<Self, &str> {
        let split = key.split_at(key.len() - 1);
        let rank = Rank::from_str(split.0)?;
        let suit = Suit::from_str(split.1)?;

        Ok(Self { rank, suit })
    }
}
#[test]
fn test_card() {
    assert_eq!(
        Ok(Card {
            rank: Rank::Ten,
            suit: Suit::Diamond,
        }),
        Card::from_str("10D")
    );
}

#[derive(Debug, Eq, PartialEq, PartialOrd)]
struct Hand {
    cards: Vec<Card>,
}
impl Hand {
    fn from_str(hand: &str) -> Result<Self, &str> {
        let mut cards: Vec<Card> = vec![];
        for key in hand.split(' ') {
            let card = Card::from_str(key)?;
            cards.push(card);
        }
        Ok(Self { cards })
    }
}
#[test]
fn hand_test() {
    let expected = Ok(Hand {
        cards: vec![
            Card {
                rank: Rank::Ten,
                suit: Suit::Diamond,
            },
            Card {
                rank: Rank::Three,
                suit: Suit::Heart,
            },
            Card {
                rank: Rank::Four,
                suit: Suit::Club,
            },
        ],
    });

    let hand = Hand::from_str("10D 4C 3H");
    assert_eq!(expected, hand);
}

/// Given a list of poker hands, return a list of those hands which win.
///
/// Note the type signature: this function should return _the same_ reference to
/// the winning hand(s) as were passed in, not reconstructed strings which happen to be equal.
pub fn winning_hands<'a>(hands: &[&'a str]) -> Vec<&'a str> {
    unimplemented!("Out of {:?}, which hand wins?", hands)
}
