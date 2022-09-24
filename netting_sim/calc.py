from typing import Tuple


def return_netting_outputs(
    forecast: int, order: int, rtf: int
) -> Tuple[int, int, int, int, int]:
    """Return netting outputs

    Parameters
    ----------
    forecast : int
        Forecast for a particular period
    order : int
        Projected orders for the same period as forecast
    rtf : int
        Return to Forecast from the previous period

    Returns
    -------
    Tuple[int, int, int, int, int]
        COM_ORDER, NEW_ORDER, COM_FCST, NEW_FCST, UNF_ORDER
    """
    # Logic: 'new_fcst' is set to 'forecast' initially, then it is incrementally
    # decreased as we net that against 'order' and 'rtf'

    com_order = 0
    new_order = 0
    com_fcst = 0
    new_fcst = forecast
    unf_order = order

    if rtf > 0:
        # Calculate COM_ORDER
        if order < rtf:
            com_order = order
        else:
            com_order = rtf
        remaining_rtf = rtf - com_order
        unf_order = order - com_order
        new_fcst = max(new_fcst - com_order, 0)  # 'new_fcst' can not be negative

        # If RTF remains, then use that to commit forecast
        if remaining_rtf > 0:
            if new_fcst < remaining_rtf:
                com_fcst = new_fcst
            else:
                com_fcst = remaining_rtf
            new_fcst = new_fcst - com_fcst  # Reduce 'new_fcst' by 'com_fcst'

    # If 'new_fcst' remains, then use that to set 'new_order'
    if new_fcst > 0:
        if unf_order < new_fcst:
            new_order = unf_order
        else:
            new_order = new_fcst
        unf_order = unf_order - new_order
        new_fcst = new_fcst - new_order

    return com_order, new_order, com_fcst, new_fcst, unf_order
