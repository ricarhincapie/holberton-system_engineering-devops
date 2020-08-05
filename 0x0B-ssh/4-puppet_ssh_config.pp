# This file changes the ssh_config file
file {'ssh_config pass':
  ensure =>  'present',
  path   =>  '/etc/ssh/copy_ssh_config',
  line   =>  '    PasswordAuthentication no',
  match  =>  '^#\s\s\sPass',
}

file {'ssh_config identity':
  ensure =>  'present',
  path   =>  '/etc/ssh/copy_ssh_config',
  line   =>  '    IdentityFile ~/.ssh/holberton',
  match  =>  '^#\s\s\sIdentity',
}
