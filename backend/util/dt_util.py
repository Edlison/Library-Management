# @Author  : Edlison
# @Date    : 1/4/21 02:00
import datetime


def add_months(dt,months):
    """
    增加月份

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 02:08
    """
    targetmonth=months+dt.month
    try:
        dt=dt.replace(year=dt.year+int(targetmonth/12),month=(targetmonth%12))
    except:
        dt=dt.replace(year=dt.year+int((targetmonth+1)/12),month=((targetmonth+1)%12),day=1)
        dt+=datetime.timedelta(days=-1)
    return dt