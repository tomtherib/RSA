# Nástroj pro prolomení šifrované komunikace systému RSA

## Instalace

V souboru `requirements.txt` jsou uloženy všechny knihovny potřebné ke spuštění aplikace `rsa_decrypt.py`. V OS Windows byla navíc pro správné fungování knihovny Crypto - `pycryptodome 3.9.9` potřebná instalace některých základních komponentů `Visual Studia` ( viz. [Pycryptodome - How to install? ](https://pycryptodome.readthedocs.io/en/latest/src/installation.html#windows-from-sources-python-3-5-and-newer)) a využití python distribuce Anaconda.  

## Spuštění
Při spuštění aplikace `rsa_decrypt.py` se objeví menu:  
1. Generate both keys by provided libraries Crypto and show all components including prime numbers
2. Generate modulus n with smaller key size and actually decrypt n to two prime number factors p and q
3. Show credits
4. Exit program  
 
Volba se provádí zapsáním hodnoty dané možnosti jako celého čísla (např: 2). Jelikož je knihovna Crypto schopna generovat pouze klíče o velikosti `1024b, 2048b a 3072b`, bylo by nereálné snažit se takto dlouhý klíč faktorizovat.  
První možnost tedy využije Crypto knihovnu, vygeneruje a vypíše do konzole oba klíče ve formátu `PEM` i s jednotlivými komponenty. Při zvolení druhé možnosti je nutno uvést požadovanou délku klíče v bitech a při potvrzení se objeví náhodně vygenerované komponenty `n, e, p, q`. Následně
je potřeba vybrat algoritmus pro faktorizaci.  
1. Pollard's Rho algoritmus
2. Eratosthenovo síto
3. Brute force algoritmus  

Pro představu vstupů je nejméněm efektivní je využití Eratosthenova síta a nad `20b` již trvá řádově minuty, Brute force trvá přibližně minutu `60b` a Pollard's Rho trvá přibližně minutu `100b`.