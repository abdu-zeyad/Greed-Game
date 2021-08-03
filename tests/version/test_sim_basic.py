import pytest
<<<<<<< HEAD
from tests.version.flo import diff
from game_of_greed.game import Game

pytestmark = [pytest.mark.version_2]
=======
from tests.flo import diff
from game_of_greed.game import Game

pytestmark = [pytest.mark.version]
>>>>>>> cd9d66655b7ae069290ce87cfe2fff4f69d7df5e


def test_quitter():
    game = Game()
    diffs = diff(game.play, path="tests/version/quitter.sim.txt")
    assert not diffs, diffs

<<<<<<< HEAD

=======
# @pytest.mark.skip("pending")
>>>>>>> cd9d66655b7ae069290ce87cfe2fff4f69d7df5e
def test_one_and_done():
    game = Game()
    diffs = diff(game.play, path="tests/version/one_and_done.sim.txt")
    assert not diffs, diffs

<<<<<<< HEAD

=======
# @pytest.mark.skip("pending")
>>>>>>> cd9d66655b7ae069290ce87cfe2fff4f69d7df5e
def test_single_bank():
    game = Game()
    diffs = diff(
        game.play, path="tests/version/bank_one_roll_then_quit.sim.txt"
    )
    assert not diffs, diffs

<<<<<<< HEAD

=======
# @pytest.mark.skip("pending")
>>>>>>> cd9d66655b7ae069290ce87cfe2fff4f69d7df5e
def test_bank_first_for_two_rounds():
    game = Game()
    diffs = diff(
        game.play, path="tests/version/bank_first_for_two_rounds.sim.txt"
    )
    assert not diffs, diffs