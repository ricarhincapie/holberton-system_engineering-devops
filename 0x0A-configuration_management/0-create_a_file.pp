# This file creates a new file with some basic settings
file { 'holberton':
ensure  =>  'present',
path    =>  '/tmp/holberton',
content =>  'I love Puppet',
owner   =>  'www-data',
group   =>  'www-data',
mode    =>  '0744',
}
