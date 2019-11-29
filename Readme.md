mailhog_box
===========

Referencing as dependency using gilt (https://github.com/metacloud/gilt/,  `pip install python-gilt`)

```
# https://gilt.readthedocs.io/en/latest/
  - git: https://github.com/oops-to-devops/mailhog_box.git
    version: master
    dst: deployment/provisioners/mailhog_box/
    post_commands:
      - make
```



Using with vagrant boilerplate (https://github.com/Voronenko/devops-vagrant-ansible-boilerplate)


```

      config.vm.provision "ansible" do |ansible|
          ansible.playbook = "provisioners/mailhog_box/box_bootstrap_only.yml"
          ansible.galaxy_role_file = "provisioners/mailhog_box/requirements.yml"
          ansible.galaxy_roles_path = "deployment/provisioners/mailhog_box/roles"
          ansible.verbose = true
          ansible.groups = {
              "base_box" => [vconfig['vagrant_machine_name']]
          }
          ansible.extra_vars = {
           box_provider: "vagrant",
           env: "vagrant"
          }
      end


```


Using with terraform boilerplate (https://github.com/Voronenko/devops-terraform-ansible-boilerplate)

```tf

resource "null_resource" "mailhogboxed_servers" {
  # Changes to any instance of the cluster requires re-provisioning
  triggers {
    cluster_instance_ids = "${join(",", digitalocean_droplet.web.*.id)}"
  }


  provisioner "local-exec" {
    command = "$INFRASTRUCTURE_ROOT_DIR/provisioners/mailhog_box/provision_box.sh"

    environment {
      REMOTE_HOST = "${digitalocean_droplet.web.ipv4_address}"
      REMOTE_USER_INITIAL = "root"
      REMOTE_PASSWORD_INITIAL = ""
      BOX_DEPLOY_USER = "ubuntu"
      BOX_DEPLOY_PASS = ""
      BOX_PROVIDER = "digitalocean"
    }
  }
}


```
