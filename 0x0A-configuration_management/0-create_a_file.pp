# This file creates a new file with some basic settings
file { '/tmp/holberton':
ensure  =>  'present',
content =>  'I love Puppet'
owner   =>  'www-data',
group   =>  'www-data',
mode    =>  '0744',
}
