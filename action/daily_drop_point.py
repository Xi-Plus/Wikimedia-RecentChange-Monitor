import sys
import os
sys.path.insert(0, os.path.realpath(os.path.dirname(os.path.realpath(__file__))+"/../"))
from Monitor import *


M = Monitor()

M.cur.execute(
    """
    SELECT `userhash`, `point` FROM `user_score` WHERE `point` > 0
    """, ())
rows = M.cur.fetchall()

for row in rows:
    userhash = row[0]
    point = row[1]
    print(userhash, point)
    M.cur.execute(
        """UPDATE `user_score` SET `point` = %s
        WHERE `userhash` = %s""",
        (point-1, userhash)
    )
    M.db.commit()
