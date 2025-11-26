Task 1

Analysis of Results:

When you run this code with knows_password = False, you will see a success rate roughly around 50%.
In 1 trial, a cheater has a 50% chance of fooling Bob.In 20 trials, the chance of fooling Bob every single time is $0.5^{20}$, which is approximately 1 in a million. This proves the Soundness property of ZKPs: a cheating prover cannot consistently fool the verifier.



Task 2

Manual Obfuscation (Lexical Obfuscation):

I renamed meaningful identifiers like calculate_factorial and number to abstract names like _0x4a1 and _0x1b.

This removes the semantic context. A human reading the code has to trace the logic step-by-step to understand it calculates a factorial, rather than just reading the function name. It defends against casual inspection.


Automatic Obfuscation (Encoding/Packing):

I encoded the entire source code into a Base64 string and used Python's exec() function to decode and run it at runtime.

This hides the entire logic flow and control structure. A static analysis tool or a human cannot see any code instructions (if statements, loops) without first decoding the payload. This is commonly used to protect intellectual property or (maliciously) to hide malware payloads from antivirus scanners.

We can use there online Python obfuscators or libraries like pyarmor.
