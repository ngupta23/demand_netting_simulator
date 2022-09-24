"""Module to test netting cases
"""
from netting_sim import return_netting_outputs

##########################
#### Tests Start Here ####
##########################


def test_cases1():
    """Tests Cases 1"""
    # Case 1-1
    forecast, order, rtf = 150, 0, 100
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 0
    assert new_order == 0
    assert com_fcst == 100
    assert new_fcst == 50
    assert unf_order == 0

    # Case 1-2
    forecast, order, rtf = 100, 0, 150
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 0
    assert new_order == 0
    assert com_fcst == 100
    assert new_fcst == 0
    assert unf_order == 0


def test_cases2():
    """Tests Cases 2"""
    # Case 2-1
    forecast, order, rtf = 150, 50, 0
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 0
    assert new_order == 50
    assert com_fcst == 0
    assert new_fcst == 100
    assert unf_order == 0

    # Case 2-2
    forecast, order, rtf = 100, 150, 0
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 0
    assert new_order == 100
    assert com_fcst == 0
    assert new_fcst == 0
    assert unf_order == 50


def test_cases3():
    """Tests Cases 3"""
    # Case 3-1
    forecast, order, rtf = 0, 100, 150
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 100
    assert new_order == 0
    assert com_fcst == 0
    assert new_fcst == 0
    assert unf_order == 0

    # Case 3-2
    forecast, order, rtf = 0, 150, 100
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 100
    assert new_order == 0
    assert com_fcst == 0
    assert new_fcst == 0
    assert unf_order == 50


def test_cases4():
    """Tests Cases 4"""
    # Case 4-1
    forecast, order, rtf = 100, 0, 0
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 0
    assert new_order == 0
    assert com_fcst == 0
    assert new_fcst == 100
    assert unf_order == 0

    # Case 4-2
    forecast, order, rtf = 0, 0, 100
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 0
    assert new_order == 0
    assert com_fcst == 0
    assert new_fcst == 0
    assert unf_order == 0

    # Case 4-3
    forecast, order, rtf = 0, 100, 0
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 0
    assert new_order == 0
    assert com_fcst == 0
    assert new_fcst == 0
    assert unf_order == 100


def test_cases5():
    """Tests Cases 5"""
    # Case 5-1
    forecast, order, rtf = 150, 50, 100
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 50
    assert new_order == 0
    assert com_fcst == 50
    assert new_fcst == 50
    assert unf_order == 0

    # Case 5-2
    forecast, order, rtf = 100, 50, 100
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 50
    assert new_order == 0
    assert com_fcst == 50
    assert new_fcst == 0
    assert unf_order == 0

    # Case 5-3
    forecast, order, rtf = 150, 50, 50
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 50
    assert new_order == 0
    assert com_fcst == 0
    assert new_fcst == 100
    assert unf_order == 0


def test_cases6():
    """Tests Cases 6"""
    # Case 6-1
    forecast, order, rtf = 150, 100, 50
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 50
    assert new_order == 50
    assert com_fcst == 0
    assert new_fcst == 50
    assert unf_order == 0

    # Case 6-2
    forecast, order, rtf = 100, 150, 50
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 50
    assert new_order == 50
    assert com_fcst == 0
    assert new_fcst == 0
    assert unf_order == 50

    # Case 6-3
    forecast, order, rtf = 50, 150, 100
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 100
    assert new_order == 0
    assert com_fcst == 0
    assert new_fcst == 0
    assert unf_order == 50


def test_cases7():
    """Tests Cases 7"""
    # Case 7-1
    forecast, order, rtf = 100, 50, 150
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 50
    assert new_order == 0
    assert com_fcst == 50
    assert new_fcst == 0
    assert unf_order == 0

    # Case 7-2
    forecast, order, rtf = 50, 100, 150
    com_order, new_order, com_fcst, new_fcst, unf_order = return_netting_outputs(
        forecast=forecast, order=order, rtf=rtf
    )
    assert com_order == 100
    assert new_order == 0
    assert com_fcst == 0
    assert new_fcst == 0
    assert unf_order == 0
