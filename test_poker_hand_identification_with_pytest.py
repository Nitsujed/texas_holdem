import texas_poker


def test_hc():
    hand = texas_poker.PokerTable(board=['2H', '4S', '6C', '8D', 'TS'], player1_hand=['AH', 'KD'])
    assert hand.player_list[0].best_hand == 'High Card'
    assert hand.player_list[0].get_hand_value()[0] == 100


def test_hc_2():
    hand = texas_poker.PokerTable(board=['8H', '5D', '4C', '2D', 'TS'], player1_hand=['QH', '3C'])
    assert (hand.player_list[0].best_hand == 'High Card')
    assert hand.player_list[0].get_hand_value()[0] == 100


def test_hc_3():
    hand = texas_poker.PokerTable(board=['2H', '4D', '6C', '8D', 'TS'], player1_hand=['KH', '3D'])
    assert (hand.player_list[0].best_hand == 'High Card')
    assert hand.player_list[0].get_hand_value()[0] == 100


def test_hc_4():
    hand = texas_poker.PokerTable(board=['QH', '5D', 'KS', 'TD', '2D'], player1_hand=['3S', '7S'])
    assert (hand.player_list[0].best_hand == 'High Card')
    assert hand.player_list[0].get_hand_value()[0] == 100


def test_op():
    hand = texas_poker.PokerTable(board=['2H', '3S', 'AC', 'AD', 'TS'], player1_hand=['4C', '6S'])
    assert hand.player_list[0].best_hand == 'One Pair'
    assert hand.player_list[0].get_hand_value()[0] == 200


def test_op2():
    hand = texas_poker.PokerTable(board=['8H', '8S', '4C', '5D', 'TS'], player1_hand=['3C', 'QH'])
    assert (hand.player_list[0].best_hand == 'One Pair')
    assert hand.player_list[0].get_hand_value()[0] == 200


def test_op_3():
    hand = texas_poker.PokerTable(board=['8H', '8D', '5C', '4D', 'TS'], player1_hand=['QH', 'KD'])
    assert (hand.player_list[0].best_hand == 'One Pair')
    assert hand.player_list[0].get_hand_value()[0] == 200


def test_op_4():
    hand = texas_poker.PokerTable(board=['8H', 'QD', '5C', '4D', 'TS'], player1_hand=['4H', 'KD'])
    assert (hand.player_list[0].best_hand == 'One Pair')
    assert hand.player_list[0].get_hand_value()[0] == 200


def test_tp():
    hand = texas_poker.PokerTable(board=['KH', 'KS', '8C', '8D', 'TS'], player1_hand=['9C', '2H'])
    assert (hand.player_list[0].best_hand == 'Two Pair')
    assert hand.player_list[0].get_hand_value()[0] == 300


def test_tp_2():
    hand = texas_poker.PokerTable(board=['8H', '8D', '4C', '4D', 'TS'], player1_hand=['9H', '2C'])
    assert (hand.player_list[0].best_hand == 'Two Pair')
    assert hand.player_list[0].get_hand_value()[0] == 300


def test_tp_3():
    hand = texas_poker.PokerTable(board=['QH', 'QD', 'KH', 'KD', 'JD'], player1_hand=['JH', '8C'])
    assert (hand.player_list[0].best_hand == 'Two Pair')
    assert hand.player_list[0].get_hand_value()[0] == 300


def test_tp_4():
    hand = texas_poker.PokerTable(board=['QH', '2D', '7H', 'KD', 'JD'], player1_hand=['KH', 'QC'])
    assert (hand.player_list[0].best_hand == 'Two Pair')
    assert hand.player_list[0].get_hand_value()[0] == 300


def test_3():
    hand = texas_poker.PokerTable(board=['AH', 'AS', 'AC', '8D', 'TS'], player1_hand=['7C', '3H'])
    assert (hand.player_list[0].best_hand == '3 Of A Kind')
    assert hand.player_list[0].get_hand_value()[0] == 400


def test_3_2():
    hand = texas_poker.PokerTable(board=['TS', 'JH', '8S', '9S', 'TC'], player1_hand=['TH', '2S'])
    assert (hand.player_list[0].best_hand == '3 Of A Kind')
    assert hand.player_list[0].get_hand_value()[0] == 400


def test_3_3():
    hand = texas_poker.PokerTable(board=['AH', '4S', 'KC', '3D', 'TS'], player1_hand=['3C', '3H'])
    assert (hand.player_list[0].best_hand == '3 Of A Kind')
    assert hand.player_list[0].get_hand_value()[0] == 400


def test_3_4():
    hand = texas_poker.PokerTable(board=['TD', 'JH', '8S', '9S', '5C'], player1_hand=['TH', 'TS'])
    assert (hand.player_list[0].best_hand == '3 Of A Kind')
    assert hand.player_list[0].get_hand_value()[0] == 400


def test_straight():
    hand = texas_poker.PokerTable(board=['3H', '4S', '5C', '6D', '7S'], player1_hand=['AH', 'QH'])
    assert (hand.player_list[0].best_hand == 'Straight')
    assert hand.player_list[0].get_hand_value()[0] == 500


def test_straight_2():
    hand = texas_poker.PokerTable(board=['3H', '4S', '5C', '6D', '7S'], player1_hand=['TH', 'QH'])
    assert (hand.player_list[0].best_hand == 'Straight')
    assert hand.player_list[0].get_hand_value()[0] == 500


def test_straight_3():
    hand = texas_poker.PokerTable(board=['AH', '2D', '3C', '4D', '8S'], player1_hand=['5S', 'TH'])
    assert (hand.player_list[0].best_hand == 'Straight')
    assert hand.player_list[0].get_hand_value()[0] == 500


def test_straight_4():
    hand = texas_poker.PokerTable(board=['AD', '2C', '3H', 'TD', '5H'], player1_hand=['TH', '4C'])
    assert (hand.player_list[0].best_hand == 'Straight')
    assert hand.player_list[0].get_hand_value()[0] == 500


def test_straight_5():
    hand = texas_poker.PokerTable(board=['AH', 'AS', '3S', '4H', '5D'], player1_hand=['TD', '2C'])
    assert (hand.player_list[0].best_hand == 'Straight')
    assert hand.player_list[0].get_hand_value()[0] == 500


def test_straight_6():
    hand = texas_poker.PokerTable(board=['AH', 'KC', 'QS', 'JH', '7D'], player1_hand=['TH', '7C'])
    assert (hand.player_list[0].best_hand == 'Straight')
    assert hand.player_list[0].get_hand_value()[0] == 500


def test_straight_7():
    hand = texas_poker.PokerTable(board=['6D', 'TD', '3H', '9D', '8D'], player1_hand=['2S', '7S'])
    assert (hand.player_list[0].best_hand == 'Straight')
    assert hand.player_list[0].get_hand_value()[0] == 500


def test_straight_8():
    hand = texas_poker.PokerTable(board=['3D', '4D', '5D', '6S', '7C'], player1_hand=['4C', 'KH'])
    assert (hand.player_list[0].best_hand == 'Straight')
    assert hand.player_list[0].get_hand_value()[0] == 500


def test_flush():
    hand = texas_poker.PokerTable(board=['3H', '5H', '7H', '8H', 'TH'], player1_hand=['9C', 'TC'])
    assert (hand.player_list[0].best_hand == 'Flush')
    assert hand.player_list[0].get_hand_value()[0] == 600


def test_flush_2():
    hand = texas_poker.PokerTable(board=['2C', '4C', '6C', '8C', 'TD'], player1_hand=['TH', 'TC'])
    assert (hand.player_list[0].best_hand == 'Flush')
    assert hand.player_list[0].get_hand_value()[0] == 600


def test_flush_3():
    hand = texas_poker.PokerTable(board=['2D', '4D', '6D', '8D', 'TD'], player1_hand=['TH', '5C'])
    assert (hand.player_list[0].best_hand == 'Flush')
    assert hand.player_list[0].get_hand_value()[0] == 600


def test_flush_4():
    hand = texas_poker.PokerTable(board=['2S', '4S', 'AD', '5S', 'KS'], player1_hand=['AS', 'TD'])
    assert (hand.player_list[0].best_hand == 'Flush')
    assert hand.player_list[0].get_hand_value()[0] == 600


def test_flush_5():
    hand = texas_poker.PokerTable(board=['QH', 'QD', 'KH', 'KD', 'JD'], player1_hand=['3D', '5D'])
    assert (hand.player_list[0].best_hand == 'Flush')
    assert hand.player_list[0].get_hand_value()[0] == 600


def test_fh():
    hand = texas_poker.PokerTable(board=['8H', '8S', '8C', '3D', '3S'], player1_hand=['7C', '9C'])
    assert (hand.player_list[0].best_hand == 'Full House')
    assert hand.player_list[0].get_hand_value()[0] == 700


def test_fh_2():
    hand = texas_poker.PokerTable(board=['AH', 'AS', 'AC', '8D', '8S'], player1_hand=['9H', '2C'])
    assert (hand.player_list[0].best_hand == 'Full House')
    assert hand.player_list[0].get_hand_value()[0] == 700


def test_fh_3():
    hand = texas_poker.PokerTable(board=['5H', '5S', '5C', '8D', '8S'], player1_hand=['9C', '2H'])
    assert (hand.player_list[0].best_hand == 'Full House')
    assert hand.player_list[0].get_hand_value()[0] == 700


def test_fh_4():
    hand = texas_poker.PokerTable(board=['KH', 'KC', '3S', '3H', '3D'], player1_hand=['TH', 'KD'])
    assert (hand.player_list[0].best_hand == 'Full House')
    assert hand.player_list[0].get_hand_value()[0] == 700


def test_4():
    hand = texas_poker.PokerTable(board=['AH', 'AS', 'AC', 'AD', 'TS'], player1_hand=['4C', '5C'])
    assert (hand.player_list[0].best_hand == '4 Of A Kind')
    assert hand.player_list[0].get_hand_value()[0] == 800


def test_4_2():
    hand = texas_poker.PokerTable(board=['8H', '8S', '8C', '8D', 'TS'], player1_hand=['2H', '3C'])
    assert (hand.player_list[0].best_hand == '4 Of A Kind')
    assert hand.player_list[0].get_hand_value()[0] == 800


def test_4_3():
    hand = texas_poker.PokerTable(board=['AH', 'AC', 'QS', 'AS', 'AD'], player1_hand=['TD', 'TH'])
    assert (hand.player_list[0].best_hand == '4 Of A Kind')
    assert hand.player_list[0].get_hand_value()[0] == 800


def test_4_4():
    hand = texas_poker.PokerTable(board=['AH', 'AC', 'TS', 'TC', 'AD'], player1_hand=['TD', 'TH'])
    assert (hand.player_list[0].best_hand == '4 Of A Kind')
    assert hand.player_list[0].get_hand_value()[0] == 800


def test_sf():
    hand = texas_poker.PokerTable(board=['AH', '2H', '3H', 'TH', '5H'], player1_hand=['4H', 'TD'])
    assert (hand.player_list[0].best_hand == 'Straight Flush')
    assert hand.player_list[0].get_hand_value()[0] == 900


def test_sf_2():
    hand = texas_poker.PokerTable(board=['6H', 'TH', '3H', '4H', '5H'], player1_hand=['2H', 'TD'])
    assert (hand.player_list[0].best_hand == 'Straight Flush')
    assert hand.player_list[0].get_hand_value()[0] == 900


def test_sf_3():
    hand = texas_poker.PokerTable(board=['5S', '4S', '3S', '2S', 'AS'], player1_hand=['3C', '3D'])
    assert (hand.player_list[0].best_hand == 'Straight Flush')
    assert hand.player_list[0].get_hand_value()[0] == 900


def test_sf_4():
    hand = texas_poker.PokerTable(board=['5D', '4D', '3D', '6D', '7D'], player1_hand=['AD', '8D'])
    assert (hand.player_list[0].best_hand == 'Straight Flush')
    assert hand.player_list[0].get_hand_value()[0] == 900


def test_rf():
    hand = texas_poker.PokerTable(board=['AS', 'KS', 'QS', 'JS', 'TS'], player1_hand=['2C', '3C'])
    assert (hand.player_list[0].best_hand == 'Royal Flush')
    assert hand.player_list[0].get_hand_value()[0] == 1000


def test_rf_2():
    hand = texas_poker.PokerTable(board=['QH', '3C', 'KH', 'AH', 'JS'], player1_hand=['JH', 'TH'])
    assert (hand.player_list[0].best_hand == 'Royal Flush')
    assert hand.player_list[0].get_hand_value()[0] == 1000


def test_rf_3():
    hand = texas_poker.PokerTable(board=['AS', 'KH', 'QH', 'JH', 'TH'], player1_hand=['AH', '3C'])
    assert (hand.player_list[0].best_hand == 'Royal Flush')
    assert hand.player_list[0].get_hand_value()[0] == 1000


def test_rf_4():
    hand = texas_poker.PokerTable(board=['QC', 'TC', 'KC', 'AC', 'JC'], player1_hand=['9C', '8C'])
    assert (hand.player_list[0].best_hand == 'Royal Flush')
    assert hand.player_list[0].get_hand_value()[0] == 1000
