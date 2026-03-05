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
drawbridge_raised = False
if not drawbridge_raised:
    outcome = "Thunder: Awesome! You quickly passed the drawbridge and escaped the dungeon!"
    print(good)
else:
    outcome = "Doom: You try to swim across the moat...but the water is infested with hungry crocodiles."
    print(bad)
print(outcome)