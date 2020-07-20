# Firemark
Firemark uses ansible to deploy a simple listener to the servers.
It then uses a client to check access to the servers on the port specified.

Ports can be chnaged in the playbooks variable "ports" in 

* ansible/playbooks/server.yml
* ansible/playbooks/client.yml

Vagrantfile can be used to test everything, vagrant up and deploy the server

```
vagrant up
cd ansible
ansible-playbook -i inventory.ini -e "ansible_user=vagrant" playbooks/server.yml
```

Client access to the servers can then be checked with the client playbook

```
ansible-playbook -i inventory.ini -e "ansible_user=vagrant" playbooks/server.yml
```

Once all is tested everything can be cleaned up with the cleanup playbook

```
ansible-playbook -i inventory.ini -e "ansible_user=vagrant" playbooks/cleanup.yml
```

