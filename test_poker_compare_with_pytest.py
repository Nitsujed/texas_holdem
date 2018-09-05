import texas_poker


def test_four_beats_two():
    '''
    Testing 4 aces beats two pair
    '''
    table = texas_poker.PokerTable(
        board=['2H', '3S', 'AC', 'AD', 'TS'], player1_hand=['AH', 'AS'], player2_hand=['3C', '2C'])
    assert table.winner.name == 'Player1'


def test_two_pair_beats_high_card():
    '''
    Testing high card loses to two pair
    '''
    table = texas_poker.PokerTable(
        board=['2H', '4S', '6C', '8D', 'TS'], player1_hand=['3H', 'JH'], player2_hand=['2D', '4D'])
    assert table.winner.name == 'Player2'


def test_higher_4_wins():
    '''
    Testing higher 4 of a kind wins
    '''
    table = texas_poker.PokerTable(
        board=['AH', 'KS', 'KC', 'AD', 'TS'], player1_hand=['AC', 'AS'], player2_hand=['KH', 'KD'])
    assert table.winner.name == 'Player1'


def test_full_house_beats_straight():
    '''
    Testing full house beats straight
    '''
    table = texas_poker.PokerTable(
        board=['7H', '8S', '8C', '4D', '3S'], player1_hand=['3C', '8D'], player2_hand=['5H', '6H'])
    assert table.winner.name == 'Player1'


def test_4_beats_full_house():
    '''
    Testing full house loses to 4 of a kind
    '''
    table = texas_poker.PokerTable(
        board=['AH', 'AS', 'AC', '8D', 'TS'], player1_hand=['7C', '7D'], player2_hand=['AD', '7H'])
    assert table.winner.name == 'Player2'


def test_royal_beats_straight_flush():
    '''
    Testing royal flush beats straight flush
    '''
    table = texas_poker.PokerTable(
        board=['TS', 'KS', 'QS', 'JS', '9C'], player1_hand=['AS', '3C'], player2_hand=['9S', '3S'])
    assert table.winner.name == 'Player1'


def test_higher_straight_wins():
    '''
    Testing higher straight wins
    '''
    table = texas_poker.PokerTable(
        board=['3H', '4S', '5C', '6D', '9C'], player1_hand=['2S', 'QH'], player2_hand=['7S', 'QC'])
    assert table.winner.name == 'Player2'


def test_straight_tie():
    '''
    Testing straight tie
    '''
    table = texas_poker.PokerTable(
        board=['3D', '4D', '5D', '6S', 'AC'], player1_hand=['7C', 'KH'], player2_hand=['7S', 'AS'])
    assert table.winner.name == ['Player1', 'Player2']


def test_two_pair_tiebreaker():
    '''
    Testing higher pair of two pair wins
    '''
    table = texas_poker.PokerTable(
        board=['KH', 'KS', '8C', '6D', 'TS'], player1_hand=['6S', '7C'], player2_hand=['8D', '9C'])
    assert table.winner.name == 'Player2'


def test_higher_three_in_full_house_wins():
    '''
    Testing higher 3 of a kind in a full house wins
    '''
    table = texas_poker.PokerTable(
        board=['AH', 'AS', '7C', '7D', '8S'], player1_hand=['7H', 'KH'], player2_hand=['6S', 'AD'])
    assert table.winner.name == 'Player2'


def test_full_house_tie():
    '''
    Testing full house tie
    '''
    table = texas_poker.PokerTable(
        board=['5H', '5S', '4C', '8D', '8H'], player1_hand=['8S', 'KH'], player2_hand=['8C', '4S'])
    assert table.winner.name == ['Player1', 'Player2']


def test_highest_card_in_flush_tie_wins():
    '''
    Testing higher card of a flush wins
    '''
    table = texas_poker.PokerTable(
        board=['3H', '5H', '7H', '8H', 'TD'], player1_hand=['2H', 'KS'], player2_hand=['TH', '8D'])
    assert table.winner.name == 'Player2'


def test_higher_4_wins2():
    '''
    Testing higher card of hand 4 of a kind wins
    '''
    table = texas_poker.PokerTable(
        board=['8H', '8S', '7C', '7D', 'TS'], player1_hand=['8D', '8C'], player2_hand=['7H', '7S'])
    assert table.winner.name == 'Player1'


def test_one_pair_beats_high_card():
    '''
    Testing one pair beats high card
    '''
    table = texas_poker.PokerTable(
        board=['8H', '6S', '4C', '5D', 'TS'], player1_hand=['3D', '3S'], player2_hand=['KH', 'JH'])
    assert table.winner.name == 'Player1'


def test_high_card_tiebreaker():
    '''
    Testing higher card tiebreaker
    '''
    table = texas_poker.PokerTable(
        board=['8H', '5D', '4C', '2D', 'TS'], player1_hand=['7D', '3D'], player2_hand=['9S', '3C'])
    assert table.winner.name == 'Player2'


def test_two_pair_tie():
    '''
    Testing two pair tie
    '''
    table = texas_poker.PokerTable(
        board=['8H', '8D', '4C', '3D', 'TS'], player1_hand=['3S', '6D'], player2_hand=['3H', '6H'])
    assert table.winner.name == ['Player1', 'Player2']


def test_one_pair_tie():
    '''
    Testing one pair tie
    '''
    table = texas_poker.PokerTable(
        board=['8H', '8D', '5C', '4D', 'TS'], player1_hand=['9S', '6H'], player2_hand=['9C', '6C'])
    assert table.winner.name == ['Player1', 'Player2']


def test_high_card_tie():
    '''
    Testing high card tie
    '''
    table = texas_poker.PokerTable(
        board=['2H', '4D', '6C', '8D', 'TS'], player1_hand=['AH', 'KH'], player2_hand=['AS', 'KS'])
    assert table.winner.name == ['Player1', 'Player2']


def test_ace_as_one():
    '''
    Testing ace used as a 1 in a straight
    '''
    table = texas_poker.PokerTable(
        board=['AH', 'TD', '3C', '4D', '5S'], player1_hand=['2C', '7D'], player2_hand=['7S', '7H'])
    assert table.winner.name == 'Player1'


def test_ace_as_one_straight_flush():
    '''
    Testing ace used as a 1 in a straight flush
    '''
    table = texas_poker.PokerTable(
        board=['AH', '9H', '3H', '4H', '5H'], player1_hand=['2H', '7D'], player2_hand=['7S', '7H'])
    assert table.winner.name == 'Player1'


def test_ace_as_one_straight_flush_loses():
    '''
    Testing ace used as a 1 in a straight flush
    '''
    table = texas_poker.PokerTable(
        board=['AH', 'QH', '3H', '4H', '5H'], player1_hand=['7C', '7D'], player2_hand=['2H', 'QD'])
    assert table.winner.name == 'Player2'


def test_ace_as_one_straight_loses():
    '''
    Testing ace used as a 1 in a straight
    '''
    table = texas_poker.PokerTable(
        board=['AD', '8C', '3H', '4C', '5H'], player1_hand=['QD', 'QH'], player2_hand=['9H', '2D'])
    assert table.winner.name == 'Player2'


def test_community_full_house():
    '''
    Testing community full house when one player has two three-of-a-kinds
    '''
    table = texas_poker.PokerTable(
        board=['KH', 'KC', '3S', '3H', '3D'], player1_hand=['8H', 'AH'], player2_hand=['7C', 'KS'])
    assert table.winner.name == 'Player2'


def test_two_pair_tiebreaker():
    '''
    Testing two pair tiebreaker
    '''
    table = texas_poker.PokerTable(
        board=['KH', 'KC', '3S', '3H', '4D'], player1_hand=['8H', '5D'], player2_hand=['7C', 'QS'])
    assert table.winner.name == 'Player2'


def test_community_4_tiebreaker():
    '''
    Testing a community 4 of a kind tiebreaker
    '''
    table = texas_poker.PokerTable(
        board=['KD', 'KC', 'KS', 'KH', '4D'], player1_hand=['8H', '5D'], player2_hand=['9H', '5C'])
    assert table.winner.name == 'Player2'


def test_community_4_tiebreaker2():
    '''
    Testing a community 4 of a kind tiebreaker when 5th community card is highest of all players
    '''
    table = texas_poker.PokerTable(
        board=['KD', 'KC', 'KS', 'KH', 'AD'], player1_hand=['8H', '5D'], player2_hand=['9H', '5C'])
    assert table.winner.name == ['Player1', 'Player2']


def test_community_4_tiebreaker3():
    '''
    Testing a community 4 of a kind tiebreaker when 5th community card is not the highest of all players
    '''
    table = texas_poker.PokerTable(
        board=['KD', 'KC', 'KS', 'KH', '4D'], player1_hand=['8H', '5D'], player2_hand=['9H', '5C'])
    assert table.winner.name == 'Player2'


def test_two_royal_flushes_is_tie():
    '''
    Testing two Royal Flushes equals a Tie
    '''
    table = texas_poker.PokerTable(
        board=['KD', 'AD', 'QD', 'JD', 'TD'], player1_hand=['4H', '5D'], player2_hand=['JH', '5S'])
    assert table.winner.name == ['Player1', 'Player2']


def test_straight_flush_tie():
    '''
    Testing community straight flush tie
    '''
    table = texas_poker.PokerTable(
        board=['QD', 'JD', 'TD', '9D', '8D'], player1_hand=['4H', '5D'], player2_hand=['JH', '5S'])
    assert table.winner.name == ['Player1', 'Player2']
