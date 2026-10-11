player starts with 6 slices and word is python

Test               input    expected result    actual result     pass/fail
correct letter      p        p _ _ _ _ _        p _ _ _ _ _        pass
incorrect letter    z        slice lost          slice lost        pass
repeated letter     p        no slice lost        no slice lost    pass
invalid input      12        input rejected    input rejected      pass
two letters        az        player informed    player informed    pass
blank enter        " "       player informed     player informed   pass
uppercase letter    P        treated as lower    treated as lower  pass

