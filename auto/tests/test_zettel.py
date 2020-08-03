import logging
import pytest

from auto.Zettel import Zettel

zettel_folder_sample_file = '200804 - k1,k2 - ref1 - id2.png'

zettelkasten_folder_sample_file = '200804a.png'

logger = logging.getLogger(__name__)


@pytest.fixture
def mocked_all_zettel(mocker):
    mocked_os = mocker.patch('Zettel.os.listdir', autospec=True)
    mocked_os.side_effect = [[zettelkasten_folder_sample_file], [zettel_folder_sample_file]]
    return Zettel()


@pytest.fixture
def mocked_new_zettel(mocker):
    mocked_os = mocker.patch('Zettel.os.listdir', autospec=True)
    mocked_os.side_effect = [[zettel_folder_sample_file, '200804b - something.png', '200804c.png']]
    return Zettel()


def test_should_return_the_list_of_ALL_zettel_card_files(mocked_all_zettel):
    lst = mocked_all_zettel.all_zettel_cards()
    assert len(lst) > 0
    assert zettelkasten_folder_sample_file in lst
    assert zettel_folder_sample_file in lst


def test_should_return_the_list_of_NEW_zettel_card_files(mocked_new_zettel):
    lst = mocked_new_zettel.new_zettel_cards()
    assert len(lst) == 1
    assert zettel_folder_sample_file in lst
    assert zettelkasten_folder_sample_file not in lst


@pytest.mark.parametrize("id,expected", [
    (zettelkasten_folder_sample_file[:6], True),
    (zettel_folder_sample_file[:6], True),
    ('non_valid_id_file', False)])
def test_should_check_if_a_given_id_exists_in_either_zettel_folder(mocked_all_zettel, id, expected):
    result = mocked_all_zettel.idExists(id)
    assert result is expected


def test_should_create_a_uniq_id(mocked_all_zettel):
    sample_id = zettelkasten_folder_sample_file[:6]
    next_id = mocked_all_zettel.make_id(sample_id)
    assert next_id[:7] == sample_id + 'b'
