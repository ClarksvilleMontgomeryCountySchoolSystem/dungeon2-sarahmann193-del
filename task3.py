good = r"""
                             \
                              \
                               \\
                                \\
                                 >\/7
                             _.-(6'  \
                            (=___._/` \
                                 )  \ |
                                /   / |
                               /    > /
                              j    < _\
                          _.-' :      ``.
                          \ r=._\        `.
                         <`\\_  \         .`-.
                          \ r-7  `-. ._  ' .  `\
                           \`,      `-.`7  7)   )
                            \/         \|  \'  / `-._
                                       ||    .'
                                        \\  (
                                         >\  >
                                     ,.-' >.'
                                    <.'_.''
                                      <'
"""
bad = r"""
      /)  (\
 )\.:::::::::./(
 \( o       o )/
   '-./ / _.-'`-.
    ( oo  ) / _  \
    |'--'/\/ ( \  \
     \''/  \| \ \  \
      ww   |  '  )  \
           |.' .'   |
          .' .'==|==|
         / .'\    [_]
      .-(/\) |     /
     /.-''''/|    |
     ||    / |    |
     //   |  |    |
     ||   |__|___/
     \\   [__[___]
     // .-'.-'  (
     ||(__(__.-._)
"""
guard_awake = False
if not guard_awake:
    outcome = "Shadow: You are able to sneak past him and out of the dungeon."
    print(good)
else:
    outcome = "Doom: The guard sees you and chases you back to the dungeon."
    print(bad)
print(outcome)