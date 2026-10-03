Forensics

<br>
<img width="670" height="645" alt="image" src="https://github.com/user-attachments/assets/bf75d055-c9c4-49dc-a25e-3b6c2011f004" />

<br>

I traced the malicious SVG attachment:

- It reconstructs a PowerShell command.

- The command reads Documents\vault.txt.

- It sends the file contents to https://updates.gctf.local/api/collect.

- The hidden XOR-obfuscated configuration reveals the target document ID:

gctf26{M41L_TR4C3_7H3_P4YL04D}

<br>
<img width="700" height="670" alt="image" src="https://github.com/user-attachments/assets/173b0873-5b2f-4ef6-9d77-a64b93322fb1" />

<br>

Recovered from the deleted Git commit 7e70e9c (fix: added db password).

The committed password was:

db_p4ss_qw3r1234!

gctf26{db_p4ss_qw3r1234!}

<br>
<img width="517" height="564" alt="image" src="https://github.com/user-attachments/assets/4f9c8b28-d280-4a3a-b769-b38a5773287b" />

<br>

The Stripe key survives in an **orphaned stash commit**.

The key evidence is unreachable commit:

321609bee5290f705b9a55e51f0e0d497d670ec0

STRIPE_API_KEY = 'sk_test_s3cr3t_k3y_f0und'

This one was hidden differently from Repo 1: the developer used a Git stash (WIP: integrating stripe payments) and then removed the stash reference, but the underlying commit/object was still recoverable with: git fsck --full --no-reflogs –unreachable

git show 321609bee5290f705b9a55e51f0e0d497d670ec0

reveals the deleted config.py and Stripe key.

gctf26{sk_test_s3cr3t_k3y_f0und}

<br>
<img width="528" height="445" alt="image" src="https://github.com/user-attachments/assets/2c043760-8b0f-4149-b6e1-465c4ed04317" />

<br>

The staged-but-never-committed AWS credentials survived as a **dangling Git blob**:

18941e2d56b3ef57b3b7ad347a15eb6d4559d4e5

Its contents are

\[default\]

aws_access_key_id = AKIA_S3CR3T_K3Y_L34K

aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYzX8Q5r7T2w

You can reproduce it with: git fsck --full --no-reflogs –unreachable

Then inspect the dangling blob: git cat-file -p 18941e2d56b3ef57b3b7ad347a15eb6d4559d4e5

This works because git add writes the file content into Git’s object database even if no commit is ever created.

gctf26{AKIA_S3CR3T_K3Y_L34K}

<br>
<img width="495" height="503" alt="image" src="https://github.com/user-attachments/assets/559aa992-2611-48b3-901e-d0785bbcc640" />

<br>

Querying the artifact metadata in the capture reveals:

- **Filename:** KB5048216.dat

- **Size:** 124219

- **SHA-256:** f34a962044d095bb136b8523d3f51fd665a39f2090aa9b5ba1aba8d9df0642f5

- **Action:** quarantined

But this flag is wrong : gctf26{KB5048216}

So I have to check the virus sha hash in the virustotal

<br>
<img width="742" height="673" alt="image" src="https://github.com/user-attachments/assets/2fef5ded-75d3-469a-ac7c-d9658043ece7" />

<br>

gctf26{Th3_H4sh_R3m3mb3r5}

Osint

<br>
<img width="632" height="539" alt="image" src="https://github.com/user-attachments/assets/2ff7269f-54f7-43db-aba4-cd77a4f3485e" />

<br>

<br>
<img width="666" height="295" alt="image" src="https://github.com/user-attachments/assets/8e9e1da1-21ad-4e58-bb45-7f401ad2301c" />

<br>

 The clue says the hotel was booked **last minute on Trip.com**.

 From the station: **Exit 2 → left ~50 m → right → straight ~500 m**.

 Another clue says there is a **CU convenience store in front** and a **GS25 downstairs**.

 These clues strongly match **Shine Hotel Incheon Airport** near **Unseo Station** in Incheon, South Korea.

 The hotel is located in the **Sky Top (스카이탑) building**, and reviews/listings mention a **GS25 on the ground floor**.

The flag is given by the challenge creator. I have not saved the flag.

Crypto

<br>
<img width="517" height="370" alt="image" src="https://github.com/user-attachments/assets/6c01a3be-1a6d-4477-bcb9-6a43985aee40" />

<br>

The script recursively applies Szudzik’s pairing function to the flag bytes. dropper main Inverting the pairing repeatedly on the supplied signature dropper output reconstructs 41 byte values, which decode directly to the flag above.

gctf26{szudz1k_b1j3c710n_p4ck3r_d3f3473d}

<br>
<img width="509" height="322" alt="image" src="https://github.com/user-attachments/assets/867c8653-3f9b-49c2-97da-ed8189a216ef" />

<br>

Why it works: the file uses the same RSA public exponent e = 11 for 11 different recipients, with the same plaintext encrypted under different moduli. vista output

Using the 11 (n, c) pairs, I combined the ciphertexts with the Chinese Remainder Theorem to obtain the exact value of \\m^{11}\\. Taking the exact integer 11th root produced:

gctf26{h4st4ds_br04dc4st_c4n_b3_d34dly}

MICS

<br>
<img width="495" height="339" alt="image" src="https://github.com/user-attachments/assets/a1794585-a25e-4ba8-a827-9651a6553d52" />

<br>

Evidence: MCC’s May 2025 update says an SSTI workshop was led by **“Boss Udang (Thaqif Hud, MCC2024 alum)”**. A LinkedIn result for Thaqif Hud shows the profile URL as my.linkedin.com/in/thaqif-hud, and the profile snippet includes ud444ng plus “MCC ALUMNI.”

https://cybercamp.my/news/2025/may

gctf26{https://www.linkedin.com/in/thaqif-hud}
