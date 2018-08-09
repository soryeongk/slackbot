# from chat_logic import answer
from chat_logic import vm


def test_insert_coin():
    expected = '100원을 넣었습니다.'
    actual = vm('동전 100')
    assert expected == actual

def test_change():
    # expected = '잔액은 0원입니다.'
    # actual = vm('잔액')
    # assert expected == actual
    assert '잔액은 0원입니다.' == vm('잔액')
    vm('동전 100')
    assert '잔액은 100원입니다.' == vm('잔액')

# def test_should_answer_when_be_called():
#     expected = ":dait_happy: : 넴"
#     actual = answer('소령')
#     assert expected == actual
#
#     expected = ":dait_happy: : 넴"
#     actual = answer('소령님')
#     assert expected == actual
#
#
# def test_roll_a_die():
#     expected = {str(i+1) for i in range(6)}
#     # 읽기 쉬운 notation을 위해서 굳이 컴프리헨션을 하지 않는 것이 더 좋을 수도
#     actual = set(answer('주사위') for _ in range(1000))
#     assert expected == actual
#
# def test_do_nothing_for_unknown_patterns():
#     actual = answer('우이앵')
#     assert actual is not None
