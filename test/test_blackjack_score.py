from blackjack.blackjack_score import *


describe 'Blackjack Score' do
  it 'can calculate the score for a pair of number cards' do

    # Arrange
    hand = [3, 4]

    # Act
    score = blackjack_score(hand)

    # Assert <-  You do this part!

  end

  it 'facecards have values calculated correctly' do

  end

  it 'calculates aces as 11 where it does not go over 21' do

  end

  it 'calculates aces as 1, if an 11 would cause the score to go over 21' do

  end

  it 'raises an ArgumentError for invalid cards' do

  end

  it 'raises an ArgumentError for scores over 21' do

  end
end
