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
escaped = True
if escaped:
    outcome = "Legend: Yay! You escaped the dungeon and lived a long happy life."
    print(good)
else:
    outcome = "Doom: You wake up from your dream...still in the dungeon."
    print(bad)
print(outcome)