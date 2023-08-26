#### Install Extension:

1. Remote - SSH (Instaall)


2. Create key:  windows. 

	ssh-keygen -t rsa
	
	ssh-copy-id root@192.168.71.241
	
	or 
	
	ssh root@192.168.71.185
	
	cd /root/.ssh/
	
	vi authorized_keys
	
	copy and paste (id_rsa.pub)
	
go to Remote - SSH	 +  add 

ssh -i ~/.ssh/id_rsa root@192.168.71.241


Config file  like: 
```bash
	Host 192.168.71.185
		User root
		HostName 192.168.71.185
		IdentityFile ~/.ssh/id_rsa
```		

--------------
	
	
3. Install Extension (Kubernetes)
