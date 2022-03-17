from blackjack.blackjack_score import *
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]

  # Act
  score = blackjack_score(hand)

  # Assert
  assert score == 7

#@pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  hand1 = ['Jack','Queen']
  hand2 = ['King','Queen']

  # Act
  score1 = blackjack_score(hand1)
  score2 = blackjack_score(hand2)

  # Assert 
  assert score1 == 20
  assert score2 == 20

#@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  # Arrange
  hand = [10, 'Ace']

  # Act
  score = blackjack_score(hand)

  # Assert
  assert score == 21


#pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  # Arrange
  hand = [10, 5, 'Ace']

  # Act
  score = blackjack_score(hand)

  # Assert
  assert score == 16

#@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  # Arrange
  hand = ["hello"]

  # Act
  score = blackjack_score(hand)

  # Assert
  assert score == "Invalid"


#@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  # Arrange
  hand = [2,3,4,5,6,7]

  # Act
  score = blackjack_score(hand)

  # Assert
  assert score == "Invalid"

#@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
    # Arrange
  hand = ['Jack', 'Queen', 'King']

  # Act
  score = blackjack_score(hand)

  # Assert
  assert score == "Bust"

def test_returns_12_for_ace_ace_king():
    # Arrange
  hand = ['Ace', 'Ace', 'King']

  # Act
  score = blackjack_score(hand)

  # Assert
  assert score == 12

def test_returns_14_for_ace_ace_ace_ace():
    # Arrange
  hand = ['Ace', 'Ace', 'Ace', 'Ace']

  # Act
  score = blackjack_score(hand)

  # Assert
  assert score == 14