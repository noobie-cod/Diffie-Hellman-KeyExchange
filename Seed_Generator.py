import Seeded_Random_Generator 
seed = int(3336)
def generate_seed(a_private_key,b_private_key,a_peer_public_key,b_peer_public_key):
	a_pkey = int((str(a_private_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x","")).replace(">",""),16)
	b_pkey = int((str(b_private_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x","")).replace(">",""),16)
	a_public_key = int((str(a_peer_public_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x","")).replace(">",""),16)
	b_public_key = int((str(b_peer_public_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x","")).replace(">",""),16)
	x1 = (a_public_key^a_pkey)%b_public_key
	x2 = (a_public_key^b_pkey)%b_public_key
	k1 = (x2^a_pkey)%b_public_key
	k2 = (x1^b_pkey)%b_public_key
	if (k1 == k2):
		seed = int(k1%1111)
	new_seed = Seeded_Random_Generator.reduce(seed)
	print(seed,new_seed)
	Seeded_Random_Generator.random_generator(new_seed)